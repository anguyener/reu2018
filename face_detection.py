import cv2

def crop_faces(img, img_name, scaleFactor = 1.1):

    #load cascade classifier training file for haarcascade
    #Either need to find or make model for side-face detection in generalized/Radbound datasets
    haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    faces = haar_face_cascade.detectMultiScale(img, scaleFactor=scaleFactor, minNeighbors=5)
    if len(faces) == 0:
        print("Did not detect face in image", img_name)
        return False
    else:
        face_crops=[]
        for (x, y, w, h) in faces:
            s = max(w,h)
            #cv2.rectangle(img_copy, (x, y), (x+s, y+s), (0, 255, 0), 2)
            face_crop = img[y:y+s, x:x+s]
            face_crop = cv2.resize(face_crop, (48, 48))
            if len(faces) == 1:
                return face_crop
            face_crops.append(face_crop)
        for i, face in enumerate(face_crops):
            cv2.imshow("Face" + str(i), face)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        x = input("Which image was a face? (0,1,2,...): ")
        x = int(x)
        return face_crops[x]
