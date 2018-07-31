import os

img_dir = os.path.join(os.getcwd(), 'Research_Datasets\\NVIE\\NVIEConverted')

for img_path in os.listdir(img_dir):
    old = os.path.join(img_dir, img_path)
    new = old.replace('posed', 'spont')
    os.rename(old, new)
