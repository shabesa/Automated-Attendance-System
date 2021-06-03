import face_recognition
import os
import cv2
import numpy

class Recog:
    def __init__(self):
        path = 'images'
        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)


int1 = Recog()