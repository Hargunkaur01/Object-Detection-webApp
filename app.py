import streamlit as st
import numpy as np
import cv2
from PIL import Image
from detector import ObjectDetector

# Page config
st.set_page_config(page_title="YOLO Webcam Detection", layout="wide")

# Title
st.title("🎥 Real-Time Object Detection")

# Load model
detector = ObjectDetector()

st.write("Capture an image using your webcam and detect objects instantly")

# Webcam input
picture = st.camera_input("Take a picture")

if picture is not None:
    # Convert to image
    image = Image.open(picture)

    st.subheader("Captured Image")
    st.image(image, use_container_width=True)

    # Convert to OpenCV format
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Detect objects
    result = detector.detect(img)

    # Convert back for display
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    st.subheader("Detected Output")
    st.image(result, use_container_width=True)

    # Download button
    st.download_button(
        "Download Result",
        data=cv2.imencode('.jpg', result)[1].tobytes(),
        file_name="detected.jpg"
    )