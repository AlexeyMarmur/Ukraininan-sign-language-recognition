# Ukraininan Sign Langugage Recognition

This project presents a real-time Ukrainian Sign Language (USL) recognition system that leverages advanced computer vision and machine learning technologies to facilitate communication for people with hearing impairments.

## Overview

The system captures video data from a camera, processes hand movements using the MediaPipe library to detect 21 key points per hand, and interprets sequences of these movements with a Long Short-Term Memory (LSTM) recurrent neural network model. The model is trained to accurately classify 108 basic Ukrainian sign language gestures, enabling real-time recognition and conversion of gestures into text messages.

The application includes an intuitive graphical user interface developed in Python with Tkinter, which allows users to collect gesture data, train the recognition model, perform live gesture recognition, and build sentences from gesture sequences. The system provides visual feedback on recognition confidence and supports dynamic interaction, facilitating practical usage in everyday communication.

## Key Features

- Data Collection Module:

Enables users to capture gesture sequences through webcam input, storing 3D coordinates of hand landmarks in structured datasets. Each gesture recording consists of a sequence of 30 frames to encapsulate dynamic movement.

- Machine Learning Architecture:

Utilizes an LSTM-based recurrent neural network with dropout layers for training on temporal sequences of hand landmarks. The model outputs class probabilities with confidence scores to filter out uncertain predictions.

- Real-Time Gesture Recognition:

Processes live video input, extracting and analyzing hand movements, continuously generating recognized gestures and updating displayed sentences with confidence filtering to improve reliability.

- User Interface:

Python Tkinter GUI organizes multiple interaction frames for data collection, model training, live recognition, sentence building, and gesture management—supporting a user-friendly experience without requiring advanced technical knowledge.

- Robust Handling of One or Two Hands:

The system accounts for the presence of one or both hands by zero-padding missing landmark data, ensuring consistent input dimensions for the model.

- Visual Feedback:

Overlays hand landmarks and recognition results on the video feed using OpenCV and Pillow, providing live and informative visualization for end-users.

## Technologies Used

- Python: Main programming language for application logic and GUI.
- MediaPipe: High-performance library from Google for hand landmark detection.
- OpenCV: Real-time video capture and image processing.
- TensorFlow / Keras: Neural network development and training framework supporting LSTM architectures.
- Tkinter: Python standard toolkit for GUI implementation.
- NumPy & Pillow: Data handling and image manipulation.

## Methodological Highlights
- Dataset:
  
The system incorporates a dataset of 108 fundamental gestures in Ukrainian Sign Language, covering everyday expressions like greetings, requests, emotions, and common phrases. The dataset is designed to include diverse samples for adequate model training.

- Preprocessing Pipeline:

Converts RGB image frames, extracts 3D hand landmarks, and builds feature vectors concatenating both hands' landmarks per frame. These vectors form sequences representing the gesture temporal dynamics.

- Model Training:

The LSTM model architecture includes two recurrent layers (64 neurons each) with dropout regularization, and a dense softmax output layer, trained using categorical cross-entropy loss on collected gesture sequences.

- Inference and Confidence Scoring:

During recognition, the model generates predictions with confidence scores, where only gestures surpassing a threshold are accepted for output, minimizing false positives.

- Sentence Construction:

Recognized gestures are accumulated into phrases in real-time, with options to delete the last gesture or clear the sentence, enhancing user control over input.

Launch the main application to start real-time gesture recognition.

## Challenges Addressed

Handling variations in user gesture speed and style through robust landmark detection and sequence modeling.
Maintaining accuracy in varied lighting and background conditions with real-time video preprocessing and landmark extraction.

Mitigating errors from incomplete or missing hand data by padding feature vectors appropriately.
Designing a clear, minimal, and accessible user interface for non-expert users.

## Future Directions

- Expanding the vocabulary to include more complex gestures and multi-sign phrases.
  
- Incorporating advanced neural network architectures (e.g., CNN-RNN hybrid, Transformer models) for improved spatial-temporal feature extraction.

- Enhancing mobile compatibility and performance optimization for embedded systems.

- Developing interactive training and gamified applications for learning and promoting Ukrainian Sign Language.

- Exploring augmented reality integration to display translated signs directly in the user’s field of view.


## Contact

Author: Oleksii Marmur

Email: alexeymarmur@gmail.com

