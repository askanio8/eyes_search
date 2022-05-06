import cv2
import mediapipe as mp
import numpy


class Iris:
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_face_mesh = mp.solutions.face_mesh
    drawing_spec = mp_drawing.DrawingSpec(thickness=3, circle_radius=3)

    @classmethod
    def draw(cls, image):
        with cls.mp_face_mesh.FaceMesh(
                static_image_mode=True,
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.05) as face_mesh:
            image = numpy.array(image)
            results = face_mesh.process(image)
            if not results.multi_face_landmarks:
                return []
            else:
                return (results.multi_face_landmarks[0].landmark[33].x,
                        results.multi_face_landmarks[0].landmark[263].x,
                        results.multi_face_landmarks[0].landmark[33].y)
            coords = []
            for face_landmarks in results.multi_face_landmarks:
                return (face_landmarks.landmark[33].x, face_landmarks.landmark[263].x,
                               face_landmarks.landmark[33].y)
                # только 1 итерация
