# Brain Disease Detection System (BDDS)
BDDS is an AI-based system designed to detect six different brain diseases from MRI images. This system uses Convolutional Neural Networks (CNNs) to analyze and classify MRI images into distinct disease categories. It aims to assist in early diagnosis and improve the treatment process for neurological conditions.

## Features
Supports Detection of Six Brain Diseases:
- Brain Tumor
- Acute Ischemic Stroke
- Alzheimer’s Disease
- Traumatic Brain Injury (TBI)
- Multiple Sclerosis
- Epilepsy
  
Deep Learning Model Architecture:
- Utilizes CNN layers to extract features from MRI images.
- Regularization through dropout layers to prevent overfitting.
- Softmax activation function for multi-class classification.

  Data Augmentation:
  - Random rotations, zooming, shifts, and flips to improve model generalization.
 
Early Stopping & Model Checkpoints:
- Automatically halts training when validation loss stops improving.
- Saves the best model based on validation performance.

## Dataset
The dataset used in this project contains MRI images, categorized into six classes. There are:

- 58,145 training images
- 14,534 validation images
Ensure that the dataset is structured into separate folders for each class (i.e., 'Brain Tumor', 'Alzheimer's', etc.).
