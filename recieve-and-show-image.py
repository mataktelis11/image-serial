import sys
import serial
import time
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['toolbar'] = 'None'                #matplotlib will have no toolbar

ser = serial.Serial('COM5', 115200, timeout=0)  #create object for serial

#function paramaters: dimention of image and array of ints and fil value
def showImage(dim,inarray,val):
        
    #testing if array has valid number of elements
    #if not it is filled with fil value
    if ((len(inarray))== dim*dim):
        print("No elements missing")
    elif((len(inarray))> dim*dim):      #if array is bigger take the first elements
        inarray = inarray[:dim*dim]
    else:
        for i in range(dim*dim - (len(inarray))):
            inarray.append(val)

    #print(inarray)
    '''
    n = int(math.sqrt(total))

    x = [inarray[i:i + n] for i in range(0, len(inarray), n)]  
    print(x) 
    '''
    #create numpy array
    Y = np.array(inarray)
    #print(Y)

    #reshape to square matrix
    Y = Y.reshape(dim,dim)

    #display
    #plt.gray()
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
        #print(rec)
        #print(type(rec))
        #print(rec.hex())
        info = [rec.hex()[i:i+2] for i in range(0, len(rec.hex()), 2)]
        #print(info)
        #print(type(info))
        intinfo = [int(i,16) for i in info]
        showImage(10,intinfo,0)
        time.sleep(0.5)
    except ser.SerialTimeoutException:
        print('Data could not be read')
ser.close()
