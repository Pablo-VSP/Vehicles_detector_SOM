import cv2
from config import VIDEO_PATH


class CameraService:

    def __init__(self, source=VIDEO_PATH):
        self.cap = cv2.VideoCapture(source)

        if not self.cap.isOpened():
            raise RuntimeError("Cannot open camera")

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()