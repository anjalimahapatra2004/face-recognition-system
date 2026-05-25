import base64
import face_recognition
import numpy as np
import cv2


class FaceService:

    @staticmethod
    def generate_face_encoding(image_data):

        try:

            print("Image Data Received")

            image_bytes = base64.b64decode(image_data)

            print("Bytes Length:", len(image_bytes))

            np_array = np.frombuffer(image_bytes, np.uint8)

            image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

            if image is None:
                print("Image Decode Failed")
                return None

            print("Image Shape:", image.shape)

            # Convert BGR to RGB
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Improve detection accuracy
            rgb_image = cv2.resize(
                rgb_image,
                (0, 0),
                fx=1.5,
                fy=1.5
            )

            face_locations = face_recognition.face_locations(
                rgb_image,
                model="hog"
            )

            print("Faces Found:", len(face_locations))

            if len(face_locations) == 0:
                return None

            encodings = face_recognition.face_encodings(
                rgb_image,
                face_locations
            )

            if len(encodings) == 0:
                return None

            return encodings[0].tolist()

        except Exception as e:

            print("FACE SERVICE ERROR:", e)

            return None