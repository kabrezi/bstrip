#/home/pi/bstrip/src/MainWithCutwire.py

import serial, string
import re, struct
from array import *
import os, numpy


output =" "
r = 255
r1 = 101
r2 = 102
r3 = 113
r4 = 0
BL = []
Page_Num = []
Obj_Num = []
Quantity = []
Wire_Ga = []
Strip_A = []
Strip_B = []
OAL = []
flt=[]
Build_List = []
Custom_cut_list = []
# arr = array('i',[])
# n = int(input("Enter the length of the array"))

# for i in range(n):
#     x = int(input("Enter the next value"))
#     arr.append(x)
    
# print(arr)

ser = serial.Serial ("/dev/ttyUSB0",9600, 8, 'N', 1, timeout=.1)
while True:# main while loop
    #print ("----")
    #while output != "": #HMI Input Loop
    output = ser.readline()
        #print(output)
#        print(ser.readline())
#         a = output
#         result = bytearray(output)
    arr = (list(bytearray(output)))
        #arr = [x for x in arr if x !=255 !=113]
    #print(arr)
    #print(flt)
    arr = list(filter((r).__ne__, arr))
    arr = list(filter((r1).__ne__, arr))
    arr = list(filter((r2).__ne__, arr))
    arr = list(filter((r3).__ne__, arr))
    arr = list(filter((r4).__ne__, arr))
    #print(arr)
        #if len(arr) == 0:
        #if arr !="":
            #print(arr[0])
        #if ((arr[0])!=1):
        #    print("emptyif len(empty_list) == 0:")
    #if len(arr) != 0:
        #BL.extend(arr)
    if len(arr) ==1:
            Page_Num.extend(arr)
    if len(arr) >1: #and len(arr) ==0:
        Obj_Num.extend(arr)
    if len(Obj_Num) >0 and Obj_Num[1] ==7:
       Quantity = Obj_Num[3]
       Wire_Ga = Obj_Num[4]
       Strip_A = (Obj_Num[5] / 10)
       strip_a_flt = numpy.float(Strip_A)
       Strip_B = (Obj_Num[5] / 10)
       strip_b_flt = numpy.float(Strip_B)
       OAL = Obj_Num[6]
       print(strip_a_flt)
       #print( '-l  + OAL[0] + ' -s ' + Strip_A[0] + ' -c ' + Stip_B[0] + ' -n ' + Quantity[0])
    #print('sudo /home/pi/bstrip/src/Cutwire1.py -a advance_' + str(OAL))
    
    def main():
        if len(Obj_Num) >0:
            os.system('sudo /home/pi/bstrip/src/Cutwire1.py -l '  + str(OAL) + ' -s ' + str(strip_a_flt) + ' -c ' + str(strip_b_flt) + ' -n ' + str(Quantity))
            
    main()
    #while len(Page_Num) ==1
        
        
        
        
        
        
    Quantity = []
    Wire_Ga = []
    Strip_A = []
    Strip_B = []
    OAL = []        
    Page_Num = []
    Obj_Num = []
    #BL = []

  
        

    

