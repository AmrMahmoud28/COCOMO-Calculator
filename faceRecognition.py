import face_recognition
import os, sys
import cv2
import numpy as np
import math

import gui


def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return str(round(value, 2)) + '%'


faceLocations = []
faceEncodings = []
faceNames = []
knownFaceEncodings = []
knownFaceNames = []
processCurrentFrame = True


def encodeFaces():
    for image in os.listdir("assets/faces"):
        faceImage = face_recognition.load_image_file(f'assets/faces/{image}')
        faceEncoding = face_recognition.face_encodings(faceImage)[0]

        knownFaceEncodings.append(faceEncoding)
        knownFaceNames.append(image)

    print(knownFaceNames)


def runRecognition():
    global processCurrentFrame, faceLocations, faceNames, isFound
    videoCapture = cv2.VideoCapture(0)
    countMatch = 0
    isFound = False

    if not videoCapture.isOpened():
        sys.exit("Video source not found...")

    while True:
        ret, frame = videoCapture.read()

        if processCurrentFrame:
            smallFrame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgbSmallFrame = smallFrame[:, :, ::-1]

            faceLocations = face_recognition.face_locations(rgbSmallFrame)
            faceEncodings = face_recognition.face_encodings(rgbSmallFrame, faceLocations)

            faceNames = []
            for faceEncoding in faceEncodings:
                matches = face_recognition.compare_faces(knownFaceEncodings, faceEncoding)
                name = "Unknown"
                confidence = "Unknown"

                faceDistances = face_recognition.face_distance(knownFaceEncodings, faceEncoding)
                bestMatchIndex = np.argmin(faceDistances)

                if matches[bestMatchIndex]:
                    name = knownFaceNames[bestMatchIndex]
                    confidence = face_confidence(faceDistances[bestMatchIndex])

                faceNames.append(f'{name.split(".jpg")[0]}')

        processCurrentFrame = not processCurrentFrame

        for (top, right, bottom, left), name in zip(faceLocations, faceNames):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

            print(name)
            for i in range(len(gui.userNames)):
                if name == gui.userNames[i]:
                    if gui.userIndex != i and countMatch > 0:
                        countMatch = 0
                    gui.userIndex = i
                    countMatch += 1

            if countMatch == 3:
                isFound = True
                countMatch = 0
                gui.updateProfile()
                break

        # cv2.imshow("Face Recognition", frame)

        if isFound: # or cv2.waitKey(1) == ord('q'):
            break

    videoCapture.release()
    cv2.destroyAllWindows()


# encodeFaces()
# runRecognition()