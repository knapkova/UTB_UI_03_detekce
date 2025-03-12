import time

import cv2

video = "imgsrc/zlin.mp4"

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

cap = cv2.VideoCapture(video)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_roi = gray_image[y:y + h, x:x + w]

        eyes = eyes_classifier.detectMultiScale(face_roi)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

        smiles = smile_classifier.detectMultiScale(face_roi)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(frame, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (100, 100, 90), 2)

    time.sleep(0.03)
    cv2.imshow('Video', frame)


cap.release()
cv2.destroyAllWindows()