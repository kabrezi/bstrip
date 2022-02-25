import serial
import string
import math

terminator = b'\xff\xff\xff'
command = str.encode('t0.txt=\"hello world\"')


ser = serial.Serial ("/dev/ttyUSB0",9600, 8, 'N', 1, timeout=.1)
while True:
    ser.write(command + terminator)
    #print(nexser.readline())