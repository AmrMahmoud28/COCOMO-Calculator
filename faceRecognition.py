import face_recognition
import os, sys
import cv2
import numpy as np
import math


def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'


class FaceRecognition:
    faceLocations = []
    faceEncodings = []
    faceNames = []
    knownFaceEncodings = []
    knownFaceNames = []
    processCurrentFrame = True

    def __init__(self):
        self.encodeFaces()

    def encodeFaces(self):
        for image in os.listdir("assets/faces"):
            faceImage = face_recognition.load_image_file(f'assets/faces/{image}')
            faceEncoding = face_recognition.face_encodings(faceImage)[0]

            self.knownFaceEncodings.append(faceEncoding)
            self.knownFaceNames.append(image)

        print(self.knownFaceNames)


    def runRecognition(self):
        videoCapture = cv2.VideoCapture(0)

        if not videoCapture.isOpened():
            sys.exit("Video source not found...")

        while True:
            ret, frame = videoCapture.read()

            if self.processCurrentFrame:
                smallFrame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                rgbSmallFrame = smallFrame[:, :, ::-1]

                self.faceLocations = face_recognition.face_locations(rgbSmallFrame)
                self.faceEncodings = face_recognition.face_encodings(rgbSmallFrame, self.faceLocations)

                self.faceNames = []
                for faceEncoding in self.faceEncodings:
                    matches = face_recognition.compare_faces(self.knownFaceEncodings, faceEncoding)
                    name = "Unknown"
                    confidence = "Unknown"

                    faceDistances = face_recognition.face_distance(self.knownFaceEncodings, faceEncoding)
                    bestMatchIndex = np.argmin(faceDistances)

                    if matches[bestMatchIndex]:
                        name = self.knownFaceNames[bestMatchIndex]
                        confidence = face_confidence(faceDistances[bestMatchIndex])

                    self.faceNames.append(f'{name.split(".jpg")[0]} ({confidence})')

            self.processCurrentFrame = not self.processCurrentFrame

            for (top, right, bottom, left), name in zip(self.faceLocations, self.faceNames):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)
                # print(name)

            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        videoCapture.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    fr = FaceRecognition()
    fr.runRecognition()
