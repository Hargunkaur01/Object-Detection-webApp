import cv2
import os
from datetime import datetime

def draw_results(results):
    return results[0].plot()

def save_frame(frame):
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    filename = datetime.now().strftime("%Y%m%d_%H%M%S.jpg")
    path = os.path.join("outputs", filename)
    cv2.imwrite(path, frame)