import cv2
import numpy as np
from tensorflow.keras.models import load_model
from ultralytics import YOLO

violence_model = load_model(r'MODELS\model_v_nv\model.h5')
gender_model = YOLO(r"MODELS\best.pt")

cap = cv2.VideoCapture(0)

# We're using MobileNEt set Image SIZse
input_size = (128, 128)  

violence_threshold = 60  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = cv2.resize(frame, input_size)
    img = img / 255.0  
    img = np.expand_dims(img, axis=0)

    prediction = violence_model.predict(img)
    class_label = np.argmax(prediction, axis=1) 
    confidence = np.max(prediction) * 100 

    labels = ['Violent', 'Non-Violent']
    label = labels[class_label[0]]

    results = gender_model(frame) 
    annotated_frame = results[0].plot()  

    if label == 'Violent' and confidence > violence_threshold:
        cv2.putText(annotated_frame, 'VIOLENCE', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

    cv2.namedWindow('Live Video Feed', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Live Video Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Live Video Feed', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
