import cv2

def crop_faces(colored_img, scaleFactor = 1.1):

    #load cascade classifier training file for haarcascade
    #Either need to find or make model for side-face detection in generalized/Radbound datasets
    haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    #just making a copy of image passed, so that passed image is not changed 
    img_copy = colored_img.copy()

    #convert the test image to gray image as opencv face detector expects gray images
    #gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    gray = img_copy
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = haar_face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5)

    #go over list of faces and draw them as rectangles on original colored img


    for (x, y, w, h) in faces:
        s = max(w,h)
        #cv2.rectangle(img_copy, (x, y), (x+s, y+s), (0, 255, 0), 2)
        img_crop = gray[y:y+s, x:x+s]
        img_crop = cv2.resize(img_crop, (48, 48))
        return img_crop
    return img_copy
