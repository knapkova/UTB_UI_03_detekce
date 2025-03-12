import cv2
import matplotlib.pyplot as plt

# img = cv.imread("imgsrc/misan.jpeg")
imgsrc = "imgsrc/snipers.jpeg"

img = cv2.imread(imgsrc)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eyes_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)
eyes = eyes_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)
#detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Get the face ROI
face_roi = gray_image[y:y+h, x:x+w]

#detect eyes
eyes = eye_cascade.detectMultiScale(face_roi)

for x in [eyes, face]:
    for (x, y, w, h) in x:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(20,10))
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.show()

