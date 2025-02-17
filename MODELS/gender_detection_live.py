from ultralytics import YOLO
import cv2

# Load your custom YOLO model
model = YOLO(r"best.pt")

# Load the video file (replace 'video.mp4' with your file path)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Make predictions on the current frame
    results = model(frame)

    # Extract and annotate bounding boxes and labels
    annotated_frame = results[0].plot()  # plot() adds bounding boxes and labels to the frame

    # Display the annotated frame
    cv2.imshow('YOLO Gender Classification on Video Feed', annotated_frame) 

    # Break the loop with 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close display window
cap.release()
cv2.destroyAllWindows()
