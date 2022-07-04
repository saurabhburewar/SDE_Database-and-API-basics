import cv2
import numpy as np


def detect_faces(file):

    filestr = file.read()
    npimg = np.fromstring(filestr, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # frontal_face = "./haarcascade_frontalface_alt.xml"
    frontal_face = "./haarcascade_frontalface_default.xml"
    front_detector = cv2.CascadeClassifier(frontal_face)
    rects = front_detector.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(
        30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    rects = [(int(x), int(y), int(x + w), int(y + h))
             for (x, y, w, h) in rects]

    data = {"num_faces": len(rects), "faces": rects}

    return data
