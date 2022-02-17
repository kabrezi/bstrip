#/home/pi/bstrip/src/MainWithCutwire.py

import serial, string
import re, struct
from array import *
import os, numpy
import time, asyncio




#output =" "
r = 255
r1 = 101
r2 = 102
r3 = 113
r4 = 0
#BL = []
#Page_Num = []
Obj_Num = []
#Quantity = []
#Wire_Ga = []
#Strip_A = []
#Strip_B = []
#OAL = []
#flt=[]
#Build_List = []
#Custom_cut_list = []
# arr = array('i',[])
# n = int(input("Enter the length of the array"))

# for i in range(n):
#     x = int(input("Enter the next value"))
#     arr.append(x)
    
# print(arr)

ser = serial.Serial ("/dev/ttyUSB1",9600, 8, 'N', 1, timeout=.1)
while True:# main while loop

    output = ser.readline()

    arr = (list(bytearray(output)))

    arr = list(filter((r).__ne__, arr))
    arr = list(filter((r1).__ne__, arr))
    arr = list(filter((r2).__ne__, arr))
    arr = list(filter((r3).__ne__, arr))
    arr = list(filter((r4).__ne__, arr))
    #print(arr)
    
    #populates page number and the entire object number
    if len(arr) >1: 
        Page_Num = arr[0]
        Obj_Num.extend(arr)
        print(Obj_Num)
    
    #if Manual feed Forward button is pressed
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==7:
        if Obj_Num[1] ==10:
            print('advance 3cm')
        else:
            print('stop')
            
    #if Manual feed Reverse button is pressed
    #if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==7:
        #if Obj_Num[1] ==9:
            #print('Reverse 3cm')
       # else:
           # print('stop')
   
   #if Strip Test button on HMI is pressed populates wire gauge
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==6:
        Wire_Ga = Obj_Num[3]
    
    #if Manual open button on HMI is pressed 
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==5:
        print('Open Stripper')
        
    #if Manual close button on HMI is pressed 
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==4:
        print('Full Cut')
    
    #if But button on the Custom Cut page of HMI is pressed
    #then all run data is populated for a custom cut job
    if len(Obj_Num) >0 and Page_Num == 1 and Obj_Num[1] ==6:
       Quantity = Obj_Num[3]
       Wire_Ga = Obj_Num[4]
       Strip_A = (Obj_Num[5] / 10)
       strip_a_flt = numpy.float(Strip_A)
       Strip_B = (Obj_Num[5] / 10)
       strip_b_flt = numpy.float(Strip_B)
       OAL = Obj_Num[6]
     
    
    def main():
        
        #Custom cut program call command
        if len(Obj_Num) >0 and Page_Num == 1 and Obj_Num[1] ==6:
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
                      + str(OAL) + ' -s ' + str(strip_a_flt) + ' -c '
                      + str(strip_b_flt) + ' -n ' + str(Quantity)
                      + ' -g ' + str(Wire_Ga))
        
        #Manual Strip Test program call command, with Gauge
        if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==8:
            print(Wire_Ga)
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a strip_' + str(Wire_Ga))
        
        #Manual Open of cutter program call
        if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==7:
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a release')
        
        #Manual Close of cutter program call
        if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==6:
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a break')
            
        #Manual feed Forward program call, increment forward by 3cm
        if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==10:
            if Obj_Num[1] ==10:
                os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a advance_3')
            else:
                print('stop')
                
        #Manual feed Reverse program call, increment backwards by 3cm
        if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==9:
            if Obj_Num[1] ==9:
                os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a advance_-3')
            else:
                print('stop')
        
    main()
        
        
        
        
        
    Quantity = []
    Wire_Ga = []
    Strip_A = []
    Strip_B = []
    OAL = []        
    Page_Num = []
    Obj_Num = []
    #BL = []

  
        

    

