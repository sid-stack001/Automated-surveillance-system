from flask import Flask, Response, render_template, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from ultralytics import YOLO # you only look once 
import threading
from datetime import datetime

app = Flask(__name__)

camera = None
output_frame = None
lock = threading.Lock()
alerts = []



            break
            
        img = cv2.resize(frame, input_size)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        
        prediction = violence_model.predict(img)
        confidence = np.max(prediction) * 100
        class_label = np.argmax(prediction, axis=1)
        label = 'Violent' if class_label[0] == 0 else 'Non-Violent'

        gender_results = gender_model(frame)
        annotated_frame = gender_results[0].plot()
   
        if label == 'Violent' and confidence > violence_threshold:
            cv2.putText(annotated_frame, 'VIOLENCE DETECTED', (10, 70),
                       cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            
            alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            detected_objects = gender_results[0].boxes.data.tolist()
            gender_counts = {'Male': 0, 'Female': 0}
            for detection in detected_objects:
                class_id = int(detection[5])
                gender = 'Male' if class_id == 1 else 'Female'
                gender_counts[gender] += 1
            
            alert_info = {
                "time": alert_time,
                "violence_confidence": f"{confidence:.2f}%",
                "males_detected": gender_counts['Male'],
                "females_detected": gender_counts['Female']
            }
            alerts.append(alert_info)
            alerts = alerts[-10:] 
        
        # Add violence confidence display
       n' + output_frame + b'\r\n')

@app.route('/')
def index():
    return render_template('nindex.html')

@app.route('/video_feed')
def video_feed():
 
def get_status():
    if camera is None or not camera.isOpened():
        status = "Camera Offline"
    else:
        status = "Active Monitoring"
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)