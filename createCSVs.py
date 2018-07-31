import os
import cv2
import csv

dataset_dir = os.path.join(os.getcwd(), 'Research_Datasets\\JAFFEConverted')

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

def svposNum(name):
    if name.find('spont') > -1:
        return 0
    elif name.find('posed') > -1:
        return 1
    else:
        return -1

def emoCSV(img_dir):
    name = os.path.join(os.path.split(img_dir)[1]+'emo.csv')
    print name
    with open(name, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['emotion', 'pixels'])
        for img_path in os.listdir(img_dir):
            img = cv2.imread(os.path.join(img_dir, img_path), -1)
            img_pixels = ' '.join(map(str,img.flatten().tolist()))
            filewriter.writerow([emoNum(img_path), img_pixels])

def svposCSV(img_dir):
    name = os.path.join(os.path.split(img_dir)[1]+'svpos.csv')
    print name
    with open(name, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['svpos', 'pixels'])
        for img_path in os.listdir(img_dir):
            img = cv2.imread(os.path.join(img_dir, img_path), -1)
            img_pixels = ' '.join(map(str,img.flatten().tolist()))
            filewriter.writerow([svposNum(img_path), img_pixels])

emoCSV(dataset_dir)
svposCSV(dataset_dir)
