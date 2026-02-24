class SimpleTracker:

    def __init__(self):
        self.objects = []

    def update(self, detections):
        # Aquí puedes poner SORT / DeepSORT si quieres
        self.objects = detections
        return self.objects