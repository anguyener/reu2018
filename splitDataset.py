import os
import cv2
import random
from createCSVs import emoNum, svposNum, shuffle
from shutil import copyfile

###Splits dataset according to percentage wanted in training
#####Training dataset is selected randomly and evenly according to emotion and svpos
#######Test is whatever is leftover.
##########Creates image directories not CSVs

dataset_dir = os.path.join(os.getcwd(), 'reu2018\\Research_Datasets\\compiledDataset')
train_dir = os.path.join(os.getcwd(), 'reu2018\\Research_Datasets\\compiledDatasetTrain')
test_dir = os.path.join(os.getcwd(), 'reu2018\\Research_Datasets\\compiledDatasetTest')
train_percentage = 50

def dir_stats(directory):
    emo = [0, 0, 0, 0, 0, 0, 0]
    svpos = [0, 0]
    for img_path in os.listdir(directory):
        #print (img_path)
        emo[emoNum(img_path)] = emo[emoNum(img_path)] + 1
        svpos[svposNum(img_path)] = svpos[svposNum(img_path)] + 1
    return (emo, svpos)

def train_size(emo, svpos, train_percentage):
    size = (svpos[0]+svpos[1]) * train_percentage / 100
    target_svpos = size / 2
    target_emo = size / 7
    return (target_emo, target_svpos)

def split_dataset(emo_size, svpos_size, data_dir):
    emo = [0, 0, 0, 0, 0, 0, 0]
    svpos = [0, 0]
    imgs = shuffle(data_dir)
    os.mkdir(train_dir)
    os.mkdir(test_dir)
    for i in imgs:
        if emo[emoNum(i)] > emo_size or svpos[svposNum(i)] > svpos_size:
            copyfile(os.path.join(data_dir, i), os.path.join(test_dir, i))
        else:
            copyfile(os.path.join(data_dir, i), os.path.join(train_dir, i))
            emo[emoNum(i)] = emo[emoNum(i)] + 1
            svpos[svposNum(i)] = svpos[svposNum(i)] + 1
            
emo, svpos = dir_stats(dataset_dir)
es, ss = train_size(emo, svpos, train_percentage)
split_dataset(es, ss, dataset_dir)
