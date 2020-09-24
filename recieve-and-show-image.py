import sys
import serial
import time
ser = serial.Serial('COM5', 115200, timeout=0)
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['toolbar'] = 'None'


def showImage(dim,inarray):
        
    #testing if array has valid number of elements
    #if not it is filled with zeros
    if ((len(inarray))== dim*dim):
        print("No elements missing")
    else:
        for i in range(dim*dim - (len(inarray))):
            inarray.append(0)

    print(inarray)
    '''
    n = int(math.sqrt(total))

    x = [inarray[i:i + n] for i in range(0, len(inarray), n)]  
    print(x) 
    '''
    #create numpy array
    Y = np.array(inarray)
    print(Y)

    #reshape to square matrix
    Y = Y.reshape(dim,dim)

    #display
    plt.gray()
    plt.imshow(Y, cmap="gray", vmin=0, vmax=255)
    #plt.axis('off')
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    return


while 1:
    try:
        #print (ser.readline())
        rec = ser.readline()
        print(rec)
        print(type(rec))
        print(rec.hex())
        info = [rec.hex()[i:i+2] for i in range(0, len(rec.hex()), 2)]
        print(info)
        print(type(info))
        intinfo = [int(i) for i in info]
        showImage(10,intinfo)
        time.sleep(1)
    except ser.SerialTimeoutException:
        print('Data could not be read')
ser.close()
