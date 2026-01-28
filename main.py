import os
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import numpy as np

st.title("AI Face Detection Web App")

# XML Model path setting
base_path = os.getcwd()
xml_path = os.path.join(base_path, 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(xml_path)

def transform(frame):
    # Frame ko array mein badalna (Yahan ghalti thi jo theek kar di hai)
    img = frame.to_ndarray(format="bgr24")
    
    # Gray scale mein convert karna
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Faces detect karna
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Faces count likhna video ke upar
    cv2.putText(img, f"Faces: {len(faces)}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Box banana
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    return img

# Streamer setup
webrtc_streamer(
    key="face-detection", 
    video_frame_callback=transform,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)
