import time
import cv2

from detection.engine import ONNXDetector
from tracking.tracker import SimpleTracker
from services.camera import CameraService

def main():

    detector = ONNXDetector()
    tracker = SimpleTracker()
    camera = CameraService()  # Cambia si es IP


    while True:
        frame = camera.read()
        if frame is None:
            break

        start = time.time()

        detections = detector.infer(frame)
        tracked_objects = tracker.update(detections)

        end = time.time()
        fps = 1 / (end - start)

        cv2.putText(
            frame,
            f"FPS: {fps:.2f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # cv2.imshow("YOLO i.MX95 NPU", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()