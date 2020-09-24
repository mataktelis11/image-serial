import sys
import serial
import time
ser = serial.Serial('COM10', 115200, timeout=0)


a=b'\x41\x42\x32\x01\x06\x04\x07\x08\x09\x10'
print (type(a))

print (sys.getsizeof(a))


ser.write(a)

ser.close()
