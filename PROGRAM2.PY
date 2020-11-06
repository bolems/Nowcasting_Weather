  
from PIL import Image 
import os
import cv2
count = 1
directory = r'C:/Users/hp/Desktop/abc/'
for filename in os.listdir(directory):
    if filename.endswith(".gif"):
        #print(os.path.join(directory, filename))
        #print (directory +filename)
        imagename = directory +filename
        cimage = imagename.replace('.gif','c')
        #print (imagename)
        Image.open(imagename).convert('RGB').save(cimage+".jpg")
        #print (cimage)
        img = cv2.imread(cimage+".jpg" ) 
        crop_img = img[0:690, 0:520]
        ss = str(count)
        filenm = directory+ss+'.jpg'
        cv2.imwrite(filenm, crop_img)
        count += 1
    else:
      continue
        
        

        