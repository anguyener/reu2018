import os
import cv2
import csv
import random

##Takes dataset and makes two CSVs out of it:
#####For whole-face emotion classification 1-6
#####For spontaneous vs posed classification 0-1

dataset_dir = os.path.join(os.getcwd(), 'Research_Datasets\\compiledDataset')

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

def shuffle(img_dir):
    imgs = []
    for img_path in os.listdir(img_dir):
        imgs.append(img_path)
    random.shuffle(imgs)
    return imgs

def emoCSV(img_dir):
    name = os.path.join(os.path.split(img_dir)[1]+'emo2.csv')
    with open(name, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['emotion', 'pixels'])
        shuffled_dir = shuffle(img_dir)
        for img_path in shuffled_dir:
            img = cv2.imread(os.path.join(img_dir, img_path), -1)
            img_pixels = ' '.join(map(str,img.flatten().tolist()))
            filewriter.writerow([emoNum(img_path), img_pixels])

def svposCSV(img_dir):
    name = os.path.join(os.path.split(img_dir)[1]+'svpos2.csv')
    with open(name, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                                quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['svpos', 'pixels'])
        shuffled_dir = shuffle(img_dir)
        for img_path in shuffled_dir:
            img = cv2.imread(os.path.join(img_dir, img_path), -1)
            img_pixels = ' '.join(map(str,img.flatten().tolist()))
            filewriter.writerow([svposNum(img_path), img_pixels])

emoCSV(dataset_dir)
#svposCSV(dataset_dir)
