import numpy as np
from PIL import Image


data=[]



f = open("demofile.txt", "r")
lines = f.readlines()
for line in lines:
    if (line!=""):
        var = line.split("-")
        #print(var)
        level2=[]
        for x in var:
            elem = x.split(" ")
            #print(elem)
            level3=[]
            for j in elem:
                try:
                    k = int(j)
                    #print(k)
                    level3.append(k)
                except ValueError:
                    continue
            #print(level3)
            if(len(level3)!=0):
                level2.append(level3)
        #print(level2)
        data.append(level2)

#print(data)


x = np.array(data)


# create Pillow image
image = Image.fromarray(x.astype(np.uint8))

image.show()
