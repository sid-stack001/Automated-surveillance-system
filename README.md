## 📌 Overview  
This project is an innovative AI-driven surveillance system designed to enhance **women’s safety** through **real-time CCTV monitoring**. It detects **potential threats**, such as a woman being alone at night or surrounded by multiple men, and **triggers instant alerts** for a rapid response.  

## 🔍 Problem Statement  
Women’s safety in public spaces is a growing concern. we address this issue by leveraging **AI-powered analysis of CCTV feeds**, allowing authorities to take **preventive action before incidents occur**.  

## 🚀 Features  
- 🎥 **24/7 Video Monitoring** – Continuous surveillance for threat detection  
- 👩‍🦰 **Gender Classification** – Uses **RCNN** to identify individuals' gender  
- ⚠️ **Real-Time Threat Detection** – Analyzes male-to-female ratio, especially at night  
- 📊 **Risk Score Calculation** – Factors in time, location, and surroundings  
- 🔥 **Hotspot Identification** – Identifies high-risk zones using historical data  
- ✋ **Gesture Recognition** – Detects distress signals like frantic waving or **SOS gestures**  
- 🚨 **Instant Alerts** – Sends real-time notifications to authorities  

## 🛠 Tech Stack  
- **Python** 🐍 – Core development language  
- **PyTorch** 🔥 – Model training & real-time updates  
- **Mobile VNet** 🖼️ – Feature extraction from CCTV frames  
- **Fine-Tuned YOLO** 👤 – Gender classification  
- **Vision Transformers (ViTs)** ⚡ – High-level feature extraction  
- **MediaPipe** 🎥 – Gesture recognition  
- **CUDA-Enabled GPUs** ⚙️ – Accelerated video processing  

## ⚙️ How It Works  
1. **Frame Preprocessing** – Resizes and normalizes CCTV frames *(640×640×3)*  
2. **Feature Extraction** – CSP-Darknet 53 generates detailed feature maps  
3. **Gender Detection** – RCNN classifies individuals with bounding boxes  
4. **Risk Assessment** – Computes risk scores based on time, location, and crowd composition  
5. **Hotspot Detection** – Identifies high-risk areas  
6. **Alerting System** – Sends **real-time alerts** for detected threats  

![image](https://github.com/user-attachments/assets/fd81c1cc-359f-4368-98f8-b96e54b5d861)



 
