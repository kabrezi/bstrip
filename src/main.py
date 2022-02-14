#/home/pi/Segnix/test.py

import serial, string
import re, struct
from array import *



# s = '\x1f\x01\q\x01\x00\x00\x00'
# result = map(ord,s)
# print (list(result))
# t = map(ord, s)
# struct.unpack('7S', s)
# print (t)
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
    print ("----")
    #while output != "": #HMI Input Loop
    output = ser.readline()
        #print(output)
#        print(ser.readline())
#         a = output
#         result = bytearray(output)
    arr = (list(bytearray(output)))
        #arr = [x for x in arr if x !=255 !=113]
        #print(arr)
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
    if len(arr) >1:
            Obj_Num.extend(arr)
    if len(Obj_Num) >0 and Obj_Num[0] ==8:
       Quantity = Obj_num[2]
       Wire_Ga = Obj_num[3]
       Strip_A = Obj_num[4]
       Strip_B = Obj_num[4]
       OAL = Obj_num[5]
    while len(Page_Num) ==1
        
        
        
        
        
        
       Quantity = []
       Wire_Ga = []
       Strip_A = []
       Strip_B = []
       OAL = []        
       Page_Num = []
       Obj_Num = []        
        #if len(arr) ==0 and len(BL) >1:
           # Build_List.extend(BL)
           # BL = []
        #if len(Build_List) >0 and len(BL) ==0:
          #  print(Build_List)
#             print(BL[5])
        #arr.remove(255)
        #print(bytearray.val)
        #print(list(result))
        #result = map(ord, a)
        ##print(list(result))
        #print (output)

        #output = " "
print(Build_List)        
#        print (result)
#         print ()
        
        
def hex_parser(line):
            result = ':'.join([f"{ord(hex_value):02X}"for hex_value in line if hex_value not in ['\\','\n',',']])
            tmp_1 = l.encode('utf24').hex()
            if len(tmp_1) == 1:
                tmp = '0' + tmp_1
                result = result + tmp_1
            return result
    
    
