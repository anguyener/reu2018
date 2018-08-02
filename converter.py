import os
import cv2
import csv
import face_detection as fd

dataset = 'Radbound'
path = os.getcwd()
svpos = 'posed'

if dataset == 'Radbound':
    oldDir = os.path.join(path, 'Research_Datasets\Radbound')
    newDir = os.path.join(path, 'RadboundConverted')
    svpos = 'posed'

if dataset == 'JAFFE':
    oldDir = os.path.join(path, 'Research_Datasets\jaffe')
    newDir = os.path.join(path, 'JAFFEConverted')
    svpos = 'posed'
'''
os.mkdir(newDir)
'''

if dataset == 'CK+':
    newDir = 'CK+Converted'

if dataset == 'NVIE':
    oldDir = os.path.join(path, 'Research_Datasets\\NVIE Database\\5_USTC-ApexVisibleSpontaneousExpressionFrame_AAM Points\\SelectedSamples')
    newDir = 'NVIEConverted'
'''
os.mkdir(newDir)
'''
def squarePicFaceDetected(image, image_name):
    face_img = fd.crop_faces(image, image_name)
    resized = cv2.resize(face_img, (48, 48), interpolation = cv2.INTER_AREA)
    return resized

#crops image to a square crops half the difference off wider axis
def squarePic(image):
    height, width = image.shape[:2] #height then width because numpy
    difference = (height - width)/2
    difference = int(difference)
    if difference < 0: #width is bigger
        cropped = image[0:height, difference:(width - difference)]
    elif difference > 0: #height is bigger
        cropped = image[difference:(height-difference), 0:width]

    return cropped
def newNameFromNvie(name, number):
    num = str(number)
    if name[0] == '1': #hapiness
        return 'img-'+num+'-3.png'
    elif name[0] == '2': #disgust
        return 'img-'+num+'-1.png'
    elif name[0] == '3': #fear
        return 'img-'+num+'-2.png'
    elif name[0] == '4': #surprise
        return 'img-'+num+'-5.png'
    elif name[0] == '5': #anger
        return 'img-'+num+'-0.png'
    elif name[0] == '6': #sadness
        return 'img-'+num+'-4.png'
    else:
        #what do we do if it's not one of the 6 basic emotions?
        return 'skip-'+num+'.png'

#makes new name for converted image with emotion as a number
def newNameFromJaffe(name, number):
    num = str(number)
    if name.find('AN') > -1:
        return 'img-'+num+'-0.png'
    elif name.find('DI') > -1:
        return 'img-'+num+'-1.png'
    elif name.find('FE') > -1:
        return 'img-'+num+'-2.png'
    elif name.find('HA') > -1:
        return 'img-'+num+'-3.png'
    elif name.find('SA') > -1:
        return 'img-'+num+'-4.png'
    elif name.find('SU') > -1:
        return 'img-'+num+'-5.png'
    elif name.find('NE') > -1:
        return 'img-'+num+'-6.png'
    else:
        #what do we do if it's not one of the 6 basic emotions?
        return 'skip-'+num+'.png'

def newNameFromCK(emotion_label, number):
    num = str(number)
    if emotion_label == 1: #anger
        return 'img-'+num+'-0.png'
    elif emotion_label == 3: #disgust
        return 'img-'+num+'-1.png'
    elif emotion_label == 4: #fear
        return 'img-'+num+'-2.png'
    elif emotion_label == 5: #happy
        return 'img-'+num+'-3.png'
    elif emotion_label == 6: # sadness
        return 'img-'+num+'-4.png'
    elif emotion_label == 7: #surprise
        return 'img-'+num+'-5.png'
    elif emotion_label == 0: #neutral
        return 'img-'+num+'-6.png'
    else:
        #what do we do if it's not one of the 6 basic emotions? (contempt)
        return 'skip-'+num+'.png'

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
    if name.find('skip') > -1:
        return -1
    elif name.find('0.') > -1:
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
        return -1

def processCK():
    img_num = 0
    subject_id = ''
    for root, dirs, files in os.walk('Research_Datasets\CK+\Emotion_labels\Emotion'):
        for file in files:
            img_num += 1

            #Isolate directory structure for emotion label
            file_path = os.path.join(root, file)
            dir_list = root.split(os.sep)
            exp_id = '\\'.join(dir_list[4:])

            #Get image file path
            img_root = 'Research_Datasets\CK+\extended-cohn-kanade-images\cohn-kanade-images'
            img_path = os.path.join(img_root, exp_id)
            (file_name, extension) = os.path.splitext(file)
            img_filename = file_name[:17] + '.png'
            img_file = os.path.join(img_path, img_filename)

            cur_subject = file[:4]
            if subject_id != cur_subject:
                subject_id = cur_subject
                img_filename_neutral = file_name[:9] + "00000001.png"
                img_file_neutral = os.path.join(img_path, img_filename_neutral)
                emotion_num = 0
                new_name = newNameFromCK(0, img_num)

                img = cv2.imread(img_file_neutral, cv2.IMREAD_GRAYSCALE)
                face_crop = squarePicFaceDetected(img, file)
                cv2.imwrite(os.path.join('CK+Converted', new_name), face_crop)
                img_num += 1
                print ('processed',subject_id, "neutral")


            #Get emotion label
            f = open(file_path, 'r')
            emotion_num = int(float(f.read().strip(' ')))
            new_name = newNameFromCK(emotion_num, img_num)
            f.close()

            #Process image
            img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
            face_crop = squarePicFaceDetected(img, file)

            cv2.imwrite(os.path.join('CK+Converted', new_name), face_crop)
            if img_num % 20 == 0:
                print('processing...')

#crops images to equal width and height, resizes to 48x48 renames, puts in new directory
def processImages(img_dir, new_dir, dataset):
    numPic = 0
    #Process neutral images from posed dataset
    if dataset == 'NVIE':
        neutral_root = os.path.join(path, 'Research_Datasets\\NVIE Database\\0-PosedExpressionDatabase')
        for root, dirs, files in os.walk(neutral_root):
            for file in files:
                dir_list = root.split(os.sep)

                if len(dir_list) >= 12 and dir_list[10] == 'visible' and dir_list[11] == 'neutral':
                    img_path = os.path.join(root, file)
                    img = cv2.imread(os.path.join(img_dir, img_path), 0) #-1 is imread_unchanged
                    resized= squarePicFaceDetected(img, img_path)
                    new_name = 'img-'+ str(numPic)+'-6.png'
                    cv2.imwrite(os.path.join(new_dir, new_name), resized)
                    numPic += 1





    for img_name in os.listdir(img_dir):
        numPic+=1
        #print ("processing image: " + img_name)

        #warning: even if image path is wrong, no error will be thrown
        if (numPic % 100 == 0):
            print ("Processed", numPic,'images.')

        if dataset=='Radbound':
            if 'Rafd090' in img_name:
                if 'contempt' in img_name:
                    continue

                img = cv2.imread(os.path.join(img_dir, img_name), 0) #-1 is imread_unchanged
                #resized = cv2.resize(squarePic(img), (48, 48), interpolation = cv2.INTER_AREA)
                resized= squarePicFaceDetected(img, img_name)
                #not sure what 3rd param does...
                new_name = newName(img_name, numPic)
                cv2.imwrite(os.path.join(new_dir, new_name), resized)

        elif dataset == 'NVIE':
            img = cv2.imread(os.path.join(img_dir, img_name), 0) #-1 is imread_unchanged
            resized= squarePicFaceDetected(img, img_name)
            new_name = newNameFromNvie(img_name, numPic)
            cv2.imwrite(os.path.join(new_dir, new_name), resized)

        else: # dataset == 'JAFFE':
            img = cv2.imread(os.path.join(img_dir, img_name), 0) #-1 is imread_unchanged
            resized= squarePicFaceDetected(img, img_name)
            new_name = newNameFromJaffe(img_name, numPic)
            cv2.imwrite(os.path.join(new_dir, new_name), resized)

def createCSV(name, categories, img_dir, svpos):
    with open(name, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(categories)
        for img_path in os.listdir(img_dir):
            img = cv2.imread(os.path.join(img_dir, img_path), -1)
            img_pixels = ' '.join(map(str,img.flatten().tolist()))
            filewriter.writerow([emoNum(img_path), img_pixels, svpos])


if dataset == 'CK+':
    processCK()
else:
    processImages(oldDir, newDir, dataset)

createCSV(dataset + 'Converted.csv', ['emotion', 'pixels', 'svpos'], newDir, svpos)
