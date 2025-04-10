import os

import cv2
import matplotlib.pyplot as plt

imgs = os.listdir("imgsrc")
for filename in imgs:
    imgsrc = "imgsrc/" + filename
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eyes_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
    smile_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

    img = cv2.imread(imgsrc)
    if img is None:
        print("Error: Image not read from source.")
    else:
        # grayscale
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        # Detect faces
        faces = face_classifier.detectMultiScale(
            gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            face_roi = gray_image[y:y + h, x:x + w]

            eyes = eyes_classifier.detectMultiScale(face_roi)
            smiles = smile_classifier.detectMultiScale(face_roi)

            #draw rectangles
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
            #for (ex, ey, ew, eh) in smiles:
                #cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (100, 100, 90), 2)

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.figure(figsize=(20, 10))
        plt.imshow(img_rgb)
        plt.axis('off')
        plt.show()