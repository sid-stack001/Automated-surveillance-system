import cv2
import numpy as np
from tensorflow.keras.models import load_model
from ultralytics import YOLO

# Load the trained violence detection model
violence_model = load_model(r'F:\MODELS\model_v_nv\model.h5')

# Load the custom YOLO model for gender detection
gender_model = YOLO(r"best.pt")

# Set up video capture (0 for default camera, adjust as needed)
cap = cv2.VideoCapture(0)

# Define the input size for MobileNet
input_size = (128, 128)  # Adjust based on your model's input size

# Set threshold for classification (in percentage)
violence_threshold = 50  # Set threshold as 90%

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame for violence detection
    img = cv2.resize(frame, input_size)
    img = img / 255.0  # Normalize if your model was trained with normalized inputs
    img = np.expand_dims(img, axis=0)

    # Make prediction for violence detection
    prediction = violence_model.predict(img)
    class_label = np.argmax(prediction, axis=1)  # Get the predicted class
    confidence = np.max(prediction) * 100  # Get the confidence level as a percentage

    # Define labels for violence detection
    labels = ['Violent', 'Non-Violent']
    label = labels[class_label[0]]

    # Perform gender detection
    results = gender_model(frame)  # Make predictions on the current frame
    annotated_frame = results[0].plot()  # Annotate the frame with bounding boxes and labels

    # Display the label "VIOLENCE" in red if the confidence exceeds the threshold
    if label == 'Violent' and confidence > violence_threshold:
        cv2.putText(annotated_frame, 'VIOLENCE', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    # Display the annotated frame in full-screen
    cv2.namedWindow('Live Video Feed', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Live Video Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Live Video Feed', annotated_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
