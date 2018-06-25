#use cv2 3.2.0 and os for image/file processing stuff

# os.getcwd() returns string of current working directory
# os.listdir(path) returns list of entries in dir given by path, arbitrary order
# os.mkdir(path) makes new directory (new dir for new images...)
# os.rename(src, dst) renames file or directory
# os.path.split(path) -> (head, tail) head is path, tail is everything after last \
# os.path.join(path, *path) concat

#cv2.imwrite('Path/newName.jpg', curr_img_reference)

#get path and image list using os, create new dir
#process images one at a time,(crop and resize) using cv2
#regExp on name to pull out emotion-type
#move and change name to something useful and easily regExped using cv2?

#make sure it makes copy, doesn't modify original image...
###pretty sure you can modify and not save and its fine.

#Next, go through newDir of renamed images, and make CSV
#import csv

#with open('persons.csv', 'wb') as csvfile:
    #filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',
                            #quoting=csv.QUOTE_MINIMAL)
    #filewriter.writerow(['emotion', 'pixels'])
    #for img:
        #filewriter.writerow(['some regEx to pull emo num out of file_name',
                            #image as pixel list: img_str = ' '.join(map(str,img.flatten().tolist()))
