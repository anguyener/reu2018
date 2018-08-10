import cv2 as cv
import os
from converter import createCSV

def processFaces(img_dirs):

    image_width = 48
    d = int(image_width/2)
    for dir in img_dirs:
        for img_file in os.listdir(dir):
            img = cv.imread(os.path.join(dir, img_file), 0)
            top_left = img[0:d, 0:d]
            cv.imwrite(os.path.join('Top_left', dir[:3] + '_tl_' +img_file), top_left)
            bot_left = img[d:,:d]
            cv.imwrite(os.path.join('Bot_left', dir[:3] + '_bl_' +img_file), bot_left)

#When processing datasets, delete images in the target directories Top_left and Bot_left
if __name__=='__main__':
    output_label = 'NVIE'
    img_dirs = ['NVIEConverted']
    processFaces(img_dirs)
    createCSV(output_label + 'top_left.csv', ['emotion', 'pixels'], 'Top_left')
    createCSV(output_label + 'bot_left.csv', ['emotion', 'pixels'], 'Bot_left')
