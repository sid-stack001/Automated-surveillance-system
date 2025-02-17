💡 Overview
HERSHIELD is an AI-driven surveillance solution designed to enhance women’s safety by monitoring CCTV feeds in real-time. It detects risky situations, such as women being alone at night or in the presence of multiple men, and triggers instant alerts to ensure swift police response.

🔍 Problem Statement
Women’s safety in public spaces remains a pressing concern. HERSHIELD combines advanced AI algorithms with continuous CCTV analysis, allowing authorities to prevent incidents before they occur.

🚀 Features
✅ 🎥 24/7 Video Monitoring – Continuous surveillance for risk detection
✅ 👩‍🦰 Gender Classification – RCNN-based gender identification
✅ ⚠️ Real-Time Threat Detection – Monitors male-to-female ratio, especially at night
✅ 📊 Risk Score Calculation – Assesses risk using time, location, and environmental factors
✅ 🔥 Hotspot Identification – Identifies high-risk areas via historical & real-time data
✅ ✋ Gesture Recognition – Detects distress signals like frantic waving or SOS gestures
✅ 🚨 Instant Alerts – Sends automatic notifications to authorities in case of threats

🛠️ Tech Stack
Python 🐍 – Core development language
PyTorch 🔥 – Model training and real-time updates
Mobile VNet 🖼️ – Extracts detailed feature maps from CCTV frames
Fine-Tuned YOLO 👤 – Gender classification
Vision Transformers (ViTs) ⚡ – High-level feature extraction
MediaPipe 🎥 – Multimodal ML pipelines for gesture recognition
CUDA-Enabled GPUs ⚙️ – Accelerated video processing
⚙️ How It Works
1️⃣ Frame Preprocessing – Resizes & normalizes CCTV frames (640×640×3)
2️⃣ Feature Extraction – CSP-Darknet 53 generates detailed feature maps
3️⃣ Gender Detection – RCNN classifies individuals with bounding boxes
4️⃣ Risk Assessment – Computes risk scores based on multiple factors
5️⃣ Hotspot Detection – Identifies high-risk areas
6️⃣ Alerting System – Sends real-time alerts for detected threats

![image](https://github.com/user-attachments/assets/fd81c1cc-359f-4368-98f8-b96e54b5d861)



 
