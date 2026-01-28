import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import numpy as np
import os

st.title("AI Face Detection Web App")


base_path = os.getcwd()
xml_path = os.path.join(base_path, 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(xml_path)

def transform(frame):
    st.write(f"Total Faces Detected:{len(faces)"}
    img = frame.to_ndarray(format="bgr24")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    return img


webrtc_streamer(key="example", video_frame_callback=transform)




