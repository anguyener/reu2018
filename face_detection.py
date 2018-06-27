import cv2

def crop_faces(img, scaleFactor = 1.1):

    #load cascade classifier training file for haarcascade
    #Either need to find or make model for side-face detection in generalized/Radbound datasets
    haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    faces = haar_face_cascade.detectMultiScale(img, scaleFactor=scaleFactor, minNeighbors=5)

    for (x, y, w, h) in faces:
        s = max(w,h)
        #cv2.rectangle(img_copy, (x, y), (x+s, y+s), (0, 255, 0), 2)
        img_crop = img[y:y+s, x:x+s]
        img_crop = cv2.resize(img_crop, (48, 48))
        return img_crop
    return img
