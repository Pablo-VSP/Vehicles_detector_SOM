# import cv2
# from config import VIDEO_PATH


# class CameraService:

#     def __init__(self, source=VIDEO_PATH):
#         self.cap = cv2.VideoCapture(source)

#         if not self.cap.isOpened():
#             raise RuntimeError("Cannot open camera")

#     def read(self):
#         ret, frame = self.cap.read()
#         if not ret:
#             return None
#         return frame

#     def release(self):
#         self.cap.release()
#------------------------------------ Para alternativa de video mp4
import cv2
from config import VIDEO_PATH


class CameraService:

    def __init__(self, source=VIDEO_PATH):
        # Forzamos backend FFMPEG en vez de GStreamer
        self.cap = cv2.VideoCapture(source, cv2.CAP_FFMPEG)

        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open video source: {source}")

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        self.cap.release()