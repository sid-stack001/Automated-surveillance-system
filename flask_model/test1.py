import tkinter as tk
from tkinter import ttk
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from ultralytics import YOLO
from PIL import Image, ImageTk
import threading
import time
from datetime import datetime

class RedTheme(ttk.Style):
    def __init__(self):
        super().__init__()
        
        # Enhanced color scheme
        self.primary_bg = '#1a0505'
        self.secondary_bg = '#2b0808'
        self.accent_red = '#cf1515'
        self.text_color = '#ff9999'
        self.highlight_red = '#ff3333'
        
        # Configure main styles with enhanced visual properties
        self.configure('Main.TFrame', background=self.primary_bg)
        self.configure('Secondary.TFrame', background=self.secondary_bg)
        
        self.configure('Main.TLabel', 
                      background=self.primary_bg, 
                      foreground=self.text_color,
                      font=('Helvetica', 10))
                      
        self.configure('Header.TLabel',
                      background=self.primary_bg,
                      foreground=self.text_color,
                      font=('Helvetica', 28, 'bold'))
                      
        self.configure('Subheader.TLabel',
                      background=self.primary_bg,
                      foreground=self.text_color,
                      font=('Helvetica', 14, 'bold'))
        
        # Enhanced button styles
        self.configure('Main.TButton', 
                      background=self.accent_red,
                      foreground=self.text_color,
                      padding=(15, 12),
                      font=('Helvetica', 11, 'bold'))
                      
        self.configure('Alert.TButton',
                      background='#ff0000',
                      foreground=self.text_color,
                      padding=(15, 12),
                      font=('Helvetica', 11, 'bold'))
                      
        self.configure('Record.TButton',
                      background=self.highlight_red,
                      foreground=self.text_color,
                      padding=(15, 12),
                      font=('Helvetica', 11, 'bold'))

class ViolenceDetectionUI:
    def __init__(self, window):
        self.window = window
        self.window.title("HER SHIELD - Personal Safety System")
        self.window.configure(bg='#1a0505')
        self.window.state('zoomed')  # Start maximized
        
        self.style = RedTheme()
        
        self.violence_model = load_model(r'F:\MODELS\model_v_nv\model.h5')
        self.gender_model = YOLO(r"best.pt")
        
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        self.input_size = (128, 128)
        self.violence_threshold = 50
        self.is_recording = False
        self.alert_active = False
        
        self.setup_ui()
        
        self.process_thread = threading.Thread(target=self.process_video, daemon=True)
        self.process_thread.start()

    def setup_ui(self):
        # Main container with padding
        container = ttk.Frame(self.window, style='Main.TFrame')
        container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header section with improved layout
        header_frame = ttk.Frame(container, style='Main.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Logo and title with enhanced styling
        header_text = ttk.Label(header_frame, 
                              text="🛡️ HER SHIELD",
                              style='Header.TLabel')
        header_text.pack()
        
        subtitle = ttk.Label(header_frame,
                           text="Personal Safety Monitoring System",
                           style='Subheader.TLabel')
        subtitle.pack(pady=(5, 0))
        
        # Main content area with flexible layout
        content_frame = ttk.Frame(container, style='Main.TFrame')
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Video frame with border effect
        video_frame = ttk.Frame(content_frame, style='Secondary.TFrame')
        video_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        video_container = ttk.Frame(video_frame, style='Main.TFrame')
        video_container.pack(padx=2, pady=2)  # Creates border effect
        
        self.video_label = ttk.Label(video_container, style='Main.TLabel')
        self.video_label.pack()
        
        # Control panel with improved organization
        control_frame = ttk.Frame(content_frame, style='Secondary.TFrame')
        control_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=2, pady=2)
        
        control_inner = ttk.Frame(control_frame, style='Main.TFrame')
        control_inner.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Status indicator with enhanced visibility
        status_frame = ttk.Frame(control_inner, style='Main.TFrame')
        status_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.status_indicator = ttk.Label(status_frame, 
                                        text="⬤",
                                        style='Main.TLabel',
                                        foreground="#00ff00",
                                        font=('Helvetica', 14))
        self.status_indicator.pack(side=tk.LEFT)
        
        ttk.Label(status_frame, 
                 text="System Active",
                 style='Subheader.TLabel').pack(side=tk.LEFT, padx=10)
        
        # Action buttons with improved spacing and hierarchy
        button_frame = ttk.Frame(control_inner, style='Main.TFrame')
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.record_btn = ttk.Button(button_frame, 
                                   text="🎥 START RECORDING",
                                   style='Record.TButton',
                                   command=self.toggle_recording)
        self.record_btn.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(button_frame, 
                  text="👮 CONTACT POLICE",
                  style='Main.TButton',
                  command=lambda: self.trigger_alert("Police contacted")).pack(fill=tk.X, pady=5)
        
        ttk.Button(button_frame,
                  text="🏥 CONTACT HOSPITAL",
                  style='Main.TButton',
                  command=lambda: self.trigger_alert("Hospital contacted")).pack(fill=tk.X, pady=5)
        
        ttk.Button(button_frame,
                  text="⚠ EMERGENCY ALERT",
                  style='Alert.TButton',
                  command=lambda: self.trigger_alert("Manual alert activated")).pack(fill=tk.X, pady=(5, 0))
        
        # Alert log with improved visibility
        alert_frame = ttk.Frame(control_inner, style='Main.TFrame')
        alert_frame.pack(fill=tk.BOTH, expand=True, pady=(20, 0))
        
        ttk.Label(alert_frame,
                 text="📋 Recent Alerts",
                 style='Subheader.TLabel').pack(pady=(0, 10))
        
        self.alerts_text = tk.Text(alert_frame,
                                 height=12,
                                 width=35,
                                 bg=self.style.secondary_bg,
                                 fg=self.style.text_color,
                                 font=('Consolas', 10),
                                 relief=tk.FLAT,
                                 padx=10,
                                 pady=10)
        self.alerts_text.pack(fill=tk.BOTH, expand=True)

    def process_frame(self, frame):
        start_time = time.time()
        
        # Violence detection
        img = cv2.resize(frame, self.input_size)
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        prediction = self.violence_model.predict(img, verbose=0)
        class_label = np.argmax(prediction, axis=1)
        confidence = np.max(prediction) * 100
        
        # Gender detection
        results = self.gender_model(frame, verbose=False)
        
        for result in results:
            boxes = result.boxes.cpu().numpy()
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0]
                cls = box.cls[0]
                gender = "Female" if cls == 0 else "Male"
                color = (0, 0, 255) if gender == "Female" else (255, 0, 0)
                
                # Enhanced detection boxes
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                
                # Improved label display
                label = f"{gender} ({conf:.1%})"
                label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                cv2.rectangle(frame, (x1, y1-25), (x1 + label_size[0], y1), color, -1)
                cv2.putText(frame, label, (x1, y1-6),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        if class_label[0] == 0 and confidence > self.violence_threshold:
            # Enhanced warning display
            overlay = frame.copy()
            cv2.putText(overlay, 'VIOLENCE DETECTED', (50, 50),
                       cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 0, 255), 4)
            cv2.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)
            
            if not self.alert_active:
                self.trigger_alert("Violence detected!")
                self.status_indicator.configure(foreground="red")
                self.window.after(1000, lambda: self.status_indicator.configure(foreground="#00ff00"))
        
        # Enhanced performance display
        process_time = (time.time() - start_time) * 1000
        cv2.putText(frame, f"Processing: {process_time:.1f}ms", (10, frame.shape[0]-10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        return frame

    def process_video(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
                
            frame = self.process_frame(frame)
            
            if self.is_recording:
                # Enhanced recording indicator
                overlay = frame.copy()
                cv2.circle(overlay, (30, 30), 15, (0, 0, 255), -1)
                cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            img_tk = ImageTk.PhotoImage(image=img)
            
            self.video_label.configure(image=img_tk)
            self.video_label.image = img_tk

    def toggle_recording(self):
        self.is_recording = not self.is_recording
        if self.is_recording:
            self.record_btn.configure(text="⏹ STOP RECORDING")
            self.trigger_alert("Recording started")
        else:
            self.record_btn.configure(text="🎥 START RECORDING")
            self.trigger_alert("Recording stopped")

    def trigger_alert(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.alerts_text.insert('1.0', f"[{timestamp}] {message}\n")
        self.alerts_text.see('1.0')  # Auto-scroll to latest alert
        self.alert_active = True
        self.window.after(5000, self.reset_alert)

    def reset_alert(self):
        self.alert_active = False

    def cleanup(self):
        self.cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = ViolenceDetectionUI(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (app.cleanup(), root.destroy()))
    root.mainloop()