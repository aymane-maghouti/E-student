import cv2
import time
from PIL import Image,ImageTk
import numpy as np
import tkinter as tk

def detectFaces(photo):
    # Load the Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # photo=Image.open('humanface2.jpg')
    # Load the image
    img = np.array(photo)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

def cropFace(photo,faces):
    # If a face is detected, crop the image to the region containing the face
    img = np.array(photo)
    (x, y, w, h) = faces[0]
    pading = min(int(w/5),int(h/5))
    cropped_img = img[y-pading:y+h+pading, x-pading:x+w+pading]
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Resize the cropped image to a square with the specified dimensions
    size = 400 # Change this value to adjust the dimensions of the square image
    resized_img = cv2.resize(cropped_img, (size, size), interpolation=cv2.INTER_AREA)

    # Save the resized image
    cv2.imwrite('output_image.jpg', resized_img)

def numpyToStr(npImage):
    photo = tk.PhotoImage(width=npImage.shape[1], height=npImage.shape[0])
    photo.put("{" + " ".join(str(x) for x in np.ravel(npImage)) + "}", to=(0, 0))


photo=Image.open('humanface.jpg')
faces=detectFaces(photo)
cropFace(photo,faces)