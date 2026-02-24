import onnxruntime as ort
import numpy as np
import cv2
from config import MODEL_PATH, PROVIDERS, INPUT_SIZE

class ONNXDetector:

    def __init__(self):
        print("Available providers:", ort.get_available_providers())

        self.session = ort.InferenceSession(
            MODEL_PATH,
            providers=PROVIDERS
        )

        print("Using providers:", self.session.get_providers())

        self.input_name = self.session.get_inputs()[0].name

    def preprocess(self, frame):
        img = cv2.resize(frame, (INPUT_SIZE, INPUT_SIZE))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.astype(np.float32) / 255.0
        img = np.transpose(img, (2, 0, 1))
        img = np.expand_dims(img, axis=0)
        return img

    def infer(self, frame):
        input_tensor = self.preprocess(frame)
        outputs = self.session.run(None, {self.input_name: input_tensor})
        return outputs