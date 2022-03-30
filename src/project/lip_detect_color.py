'''Detect lips with its landmark using dlib and haarcascde'''
import cv2
import numpy as np
import dlib
import os

def read_image(file_path):
    '''Read and return the image from a given file path'''

    if not os.path.isfile(file_path):
        print("The entered file path is invalid, please enter a valid file path")

    img = cv2.imread(file_path)
    return img

def get_lip_landmark(img):
    '''Finding lip landmark and return list of corresponded coordinations'''

    img = img
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Perform landmark detection for whole face
    faces = detector(gray_img)
    for face in faces:
        x1,y1 = face.left(),face.top()
        x2,y2 = face.right(),face.bottom()
        landmarks = predictor(gray_img,face)
        lmPoints = []
    #obtain landmark coordinations for lips only, since lips landmark ranging from point 48 to 68
        for n in range(48,68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            lmPoints.append([x,y])
            #cv2.circle(img,(x,y),0,(0,255,0),cv2.FILLED)
    #cv2.imshow("lip landmark", img)
    return lmPoints

def coloring_lip(imgOriginal,lmPoints,r,g,b):
    '''Coloring the lip base on given coordinarion'''

    img = imgOriginal.copy()

    #Optain exact coordination of the lips
    poly1=np.array(lmPoints[:12], np.int32).reshape((-1,1,2))
    poly2=np.array(lmPoints[12:], np.int32).reshape((-1,1,2))

    #Fill in the color base on the coordination by fillPoly
    colored= cv2.fillPoly(img, [poly1,poly2], (r,g,b))
    #Smoothen the image by GaussianBlur
    colored = cv2.GaussianBlur(colored,(7,7),0)

    #kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40,40))
    #colored = cv2.morphologyEx(colored, cv2.MORPH_CLOSE, kernel, 1)
    #colored = cv2.GaussianBlur(colored,(15,15),cv2.BORDER_DEFAULT)
    #final_colored_lip = cv2.bitwise_and(colored,imgOriginal)

    # blend colored lips and the original picture together
    cv2.addWeighted(colored, 0.3, imgOriginal, 0.7 , 0, colored)
    cv2.imshow("Colored lip", colored)
    cv2.imshow("Original lip", imgOriginal)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
