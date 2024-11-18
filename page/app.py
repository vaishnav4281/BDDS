from flask import Flask, render_template, request, redirect, url_for, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load pre-trained model
model = load_model('bdc.h5')

# Map severity to diseases
severity_to_disease = {
    0: "No significant issues detected",
    1: "Mild Migraine",
    2: "Moderate Headache Disorders",
    3: "Severe Brain Tumor Risk",
    4: "Critical Neurological Disorder",
    5: "Acute Brain Disease"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    if request.method == 'POST':
        # Collect MCQ responses and calculate severity
        mcq_data = [
            int(request.form.get("question1", 0)),
            int(request.form.get("question2", 0)),
            int(request.form.get("question3", 0))
        ]
        severity = sum(mcq_data) // len(mcq_data)
        disease = severity_to_disease.get(severity, "Unknown Condition")
        
        # Store severity and disease in session
        session['severity'] = severity
        session['disease'] = disease
        return redirect(url_for('booking'))
    return render_template('symptoms.html')

@app.route('/booking')
def booking():
    disease = session.get('disease', "Unknown Condition")
    return render_template('booking.html', disease=disease)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        scan_type = request.form['scan_type']
        file = request.files['scan_image']
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Analyze MRI image
            if scan_type == "MRI":
                img = load_img(filepath, target_size=(224, 224))
                img_array = img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                prediction = model.predict(img_array)
                predicted_class = np.argmax(prediction, axis=1)[0]
                class_names = ['Class 1', 'Class 2', 'Brain Tumor', 'Epilepsy', 'Class 5', 'Class 6']
                scan_result = f"Predicted Disease: {class_names[predicted_class]}"
            else:
                scan_result = "Analysis not available for this scan type yet"

            # Store scan results in session
            session['scan_result'] = scan_result
            return redirect(url_for('scan_results'))
    return render_template('upload.html')

@app.route('/symptom_results')
def symptom_results():
    severity = session.get('severity', "N/A")
    disease = session.get('disease', "N/A")
    result = f"Severity Level: {severity}\nCondition: {disease}"
    return render_template('res.html', result=result)

@app.route('/scan_results')
def scan_results():
    scan_result = session.get('scan_result', "No result available")
    return render_template('results.html', scan_result=scan_result)
    
@app.route('/clear_session')
def clear_session():
    session.clear()  # This clears all session data
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
