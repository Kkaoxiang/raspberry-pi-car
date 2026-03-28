import cv2
from src.face_detect import FaceDetector


class CameraStream:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)
        self.face_detector = FaceDetector()

    def read_and_detect(self):
        ok, frame = self.cap.read()
        if not ok:
            print("[CAMERA] Failed to read frame")
            return None

        faces = self.face_detector.detect_faces(frame)
        frame = self.face_detector.draw_faces(frame, faces)
        return frame

    def preview_loop(self):
        while True:
            frame = self.read_and_detect()
            if frame is None:
                continue

            cv2.imshow("Face Detection", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        self.cap.release()
        cv2.destroyAllWindows()