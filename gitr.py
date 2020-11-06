from PIL import Image 
import os
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
        #Image.open('C:/Users/hp/Desktop/abc/a.gif').convert('RGB').save('C:/Users/hp/Desktop/abc/prev2.jpg')
        #Image.open(filename).convert('RGB').save(count+".jpg")
        count += 1
    else:
        continue
        
        
        
        