MODEL_PATH = "/app/app/yolov8n.onnx"

PROVIDERS = [
    "NeutronExecutionProvider",
    "CPUExecutionProvider"
]

INPUT_SIZE = 640
CONF_THRESHOLD = 0.25

TARGET_CLASSES = [0, 1, 2, 3, 5, 7]
LINE_Y = 400
VIDEO_PATH = '/app/app/traffic.mp4'
# VIDEO_PATH = 0
