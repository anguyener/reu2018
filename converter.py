#from shutil import copytree
import os
import cv2
import csv
import face_detection as fd

#oldDir = '..\Research_Datasets\Radbound'
oldDir = '..\Research_Datasets\jaffe'
path = os.getcwd()
#newDir = os.path.join(path, 'RadboundConverted')
newDir = os.path.join(path, 'JAFFEConverted')
#os.mkdir(newDir) #causes error when directory already exists
#copytree(DSdir, newDir)
numPic = 0

#load cascade classifier training file for haarcascade
#Either need to find or make model for side-face detection in Radbound dataset
haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')


#loop for processing images
for img_path in os.listdir(oldDir):
    numPic+=1
    img = cv2.imread(os.path.join(oldDir, img_path), -1) #-1 is imread_unchanged
    #warning: even if image path is wrong, no error will be thrown

    #crops square image of face from image
    face_img = fd.crop_faces(haar_face_cascade, img)

    #resized = cv2.resize(squarePic(img), (48, 48), interpolation = cv2.INTER_AREA)
    resized = cv2.resize(face_img, (48, 48), interpolation = cv2.INTER_AREA)
    #not sure what 3rd param does...

    #os.rename(img, newName(img_path, numPic)) #should this be img or img_path??
    #cv2.imwrite(os.path.join(newDir, newName), resized)
    cv2.imwrite(os.path.join(newDir, str(numPic) + '.jpg'), resized) #for testing

#creates csv
with open('RadboundConverted.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['emotion', 'pixels'])
    for img_path in os.listdir(newDir):
        img = cv2.imread(os.path.join(newDir, img_path), -1)
        img_pixels = ' '.join(map(str,img.flatten().tolist()))
        filewriter.writerow([emoNum(img_path), img_pixels])

#crops image to a square crops half the difference off wider axis
def squarePic(image):
    height, width = img.shape #height then width because numpy
    difference = (height - width)/2

    if difference < 0: #width is bigger
        cropped = image[0:height, difference:(width - difference)]
    elif difference > 0: #height is bigger
        cropped = image[difference:(height-difference), 0:width]

    return cropped

#makes new name for converted image with emotion as a number
def newName(name, number):
    num = str(number)
    if name.find('angry') > -1:
        return 'img-'+num+'-0.jpg'
    elif name.find('disgusted') > -1:
        return 'img-'+num+'-1.jpg'
    elif name.find('fearful') > -1:
        return 'img-'+num+'-2.jpg'
    elif name.find('happy') > -1:
        return 'img-'+num+'-3.jpg'
    elif name.find('sad') > -1:
        return 'img-'+num+'-4.jpg'
    elif name.find('surprised') > -1:
        return 'img-'+num+'-5.jpg'
    elif name.find('neutral') > -1:
        return 'img-'+num+'-6.jpg'
    else:
        #what do we do if it's not one of the 6 basic emotions?
        return 'skip-'+num+'.jpg'

#scans image name for emotion number (last number before extention) returns it as int
def emoNum(name):
    if name.find('0.') > -1: #does the '.' need an escape character?
        return 0
    elif name.find('1.') > -1:
        return 1
    elif name.find('2.') > -1:
        return 2
    elif name.find('3.') > -1:
        return 3
    elif name.find('4.') > -1:
        return 4
    elif name.find('5.') > -1:
        return 5
    elif name.find('6.') > -1:
        return 6
    else:
        return -1 #this will probably cause mistakes later...
