import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load the trained model
model = tf.keras.models.load_model('bdc.h5')

# Class labels corresponding to the six classes
class_labels = [
    "Alzheimers",
    "Acute Ischemic Stroke",
    "Multiple Sclerosis",
    "Brain Tumor",
    "Epilepsy",
    "Traumatic Brain Injury"
]

# Function to preprocess input image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Load image and resize
    img_array = image.img_to_array(img)  # Convert image to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
    return img_array

# Function to predict disease type
def predict_disease(img_path):
    img_array = preprocess_image(img_path)
    prediction = model.predict(img_array)  # Get prediction from model
    predicted_class_index = np.argmax(prediction, axis=1)[0]  # Get index of highest probability
    predicted_class_label = class_labels[predicted_class_index]  # Map index to class label
    confidence = np.max(prediction)  # Get the confidence score
    return predicted_class_label, confidence

# Test on an MRI image
test_image_path = 'Sample\\TBI.png'  # Replace with your image path
predicted_disease, confidence = predict_disease(test_image_path)

# Display the result
print(f"Predicted Disease: {predicted_disease}")
print(f"Confidence: {confidence * 100:.2f}%")

# Optional: Display the input image
img = image.load_img(test_image_path, target_size=(224, 224))
plt.imshow(img)
plt.title(f"Predicted: {predicted_disease} ({confidence * 100:.2f}%)")
plt.axis('off')
plt.show()
