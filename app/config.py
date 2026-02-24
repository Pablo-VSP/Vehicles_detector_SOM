import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "yolov8n.onnx")
MODEL_PATH = os.path.abspath(MODEL_PATH)

PROVIDERS = [
    "NeutronExecutionProvider",
    "CPUExecutionProvider"
]

INPUT_SIZE = 640
CONF_THRESHOLD = 0.25

TARGET_CLASSES = [0, 1, 2, 3, 5, 7]
LINE_Y = 400
VIDEO_PATH = 'traffic.mp4'
# VIDEO_PATH = 0
