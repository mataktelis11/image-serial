import numpy as np
from PIL import Image
img_data = Image.open('sample3.jpg' )
img_arr = np.array(img_data) 
print(img_arr)

list1 = img_arr.tolist()

list12 = [[[23,22,31],[1,2,3],[4,5,6]],[[1,2,3],[1,33,3],[1,2,3]]]

f = open("demofile.txt", "w")

for i in range(len(list1)):
    for j in range(len(list1[i])):
        for z in range(len(list1[i][j])):            
            f.write(str(list1[i][j][z]))
            f.write(" ")
        f.write("-")
    f.write("\n")
f.close()
