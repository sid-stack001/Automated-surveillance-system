import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model(r'MODELS\model_v_nv\model.h5')

# Set up video capture (0 is typically the default camera)
cap = cv2.VideoCapture(0)

# Define the input size for MobileNet
input_size = (128, 128)  # Adjust based on your model's input size

# Set threshold for classification (in percentage)
non_violent_threshold = 10  # Set threshold as 10%

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Preprocess the frame
    img = cv2.resize(frame, input_size)
    img = img / 255.0  # Normalize if your model was trained with normalized inputs
    img = np.expand_dims(img, axis=0)

    # Make prediction
    prediction = model.predict(img)
    class_label = np.argmax(prediction, axis=1)  # Get the predicted class
    confidence = np.max(prediction) * 100  # Get the confidence level as a percentage

    # Set initial label based on the predicted class
    labels = ['Violent', 'Non-Violent']  # Modify according to your dataset
    label = labels[class_label[0]]

    # Display the label with confidence
    display_text = f"{label} ({confidence:.2f}%)"
    cv2.putText(frame, display_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Check if violence confidence is greater than 90% and display "VIOLENCE" in red
    if label == 'Violent' and confidence > 60:
        cv2.putText(frame, 'VIOLENCE', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow('Live Video Feed', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
