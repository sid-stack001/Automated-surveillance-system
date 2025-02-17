💡 Overview
HERSHIELD is an innovative, AI-powered surveillance solution designed to enhance women's safety through real-time monitoring of CCTV feeds. The system detects risky situations, like being alone at night or surrounded by men, and triggers instant alerts to ensure rapid police response.

🔍 Problem Statement
Women's safety in public spaces is a significant issue today. HERSHIELD addresses this by combining advanced AI algorithms with continuous CCTV analysis, empowering authorities to act before harm occurs.

🚀 Features
🎥 24/7 Video Monitoring: Continuously monitors CCTV feeds for risk detection
👩‍🦰 Gender Classification: Utilizes RCNN to identify individuals' gender and assess risk factors
⚠️ Real-Time Threat Detection: Tracks male-to-female ratios, especially at night
📊 Risk Score Calculation: Generates risk scores based on time, location, and environmental factors
🔥 Hotspot Identification: Pinpoints high-risk zones through historical and real-time data
✋ Gesture Recognition: Detects distress signals such as frantic waving or SOS gestures
🚨 Instant Alerts: Sends immediate notifications to authorities
🛠️ Tech Stack
Python 🐍: Primary language
PyTorch 🔥: Neural network training and real-time model updates
Mobile VNet 🖼️: Detailed feature maps from CCTV frames
Finetuned YOLO 👤: Gender-based classification
Vision Transformers (ViTs) ⚡: High-level feature extraction
MediaPipe 🎥: Multimodal ML pipelines
CUDA-Enabled GPUs ⚙️: Accelerated video processing
⚙️ How It Works
Frame Preprocessing: CCTV frames are resized and normalized (640x640x3)
Feature Extraction: CSP-Darknet 53 generates detailed feature maps
Gender Detection: RCNN classifies individuals with bounding boxes
Risk Assessment: Calculates risk scores based on multiple factors
Hotspot Detection: Tracks potential danger zones
Alerting System: Sends immediate notifications for detected threats

![image](https://github.com/user-attachments/assets/fd81c1cc-359f-4368-98f8-b96e54b5d861)



 
