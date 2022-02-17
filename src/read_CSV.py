import csv
import asyncio
import serial, string
import re, struct
from array import *
import os, numpy
import time

#with open("sample wire kit.csv", "r") as csv_file:
#    f = csv.reader(csv_file, delimiter=',')
    
#    for line in f:
#        print(line)

r = 255
r1 = 101
r2 = 102
r3 = 113
r4 = 0
Obj_Num = []
arr = []
Page_Num = []





async def Rio():
    
    if len(arr) >1: 
        Page_Num = arr[0]
        Obj_Num.extend(arr)
        print(Obj_Num)
        Wire_Ga = Obj_Num[4]
    
    '''A seperate routine to read Build Kit One CSV'''
    
    with open ('/home/pi/bstrip/src/BK1.csv', "r") as Build_One:
        f = csv.DictReader(Build_One)
        B1_List = list(f)
        #print(B1_List)
        #print(B1_List[0]['Quantity'])
        #print(B1_List[1]['Quantity'])
        '''Rows below examine wire gauge to know which to one we will use'''
        for row in B1_List:
            #print(row['Quantity'], row['Strip A'])
            #print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-9'])=='1':
                rio_wire_gauge_list.extend(row['Wire Gauge 1-9'])
                print('yes 0')
            #else:
                #print('no')
                
#         for row in B1_List:
#             #print(row['Quantity'], row['Strip A'])
#             #print(row['Quantity'])# == 1:
#             if (row['Wire Gauge 1-5'])=='1':
#                 print('yes 1')
#             #else:
#                 #print('no')
#             
#         for row in B1_List:
#             #print(row['Quantity'], row['Strip A'])
#             #print(row['Quantity'])# == 1:
#             if (row['Wire Gauge 1-5'])=='2':
#                 print('yes 2')
#             #else:
#                 #print('no')
#                 
#         for row in B1_List:
#             #print(row['Quantity'], row['Strip A'])
#             #print(row['Quantity'])# == 1:
#             if (row['Wire Gauge 1-5'])=='3':
#                 print('yes 3')
#             #else:
#                 #print('no')
#                 
#         for row in B1_List:
#             #print(row['Quantity'], row['Strip A'])
#             #print(row['Quantity'])# == 1:
#             if (row['Wire Gauge 1-5'])=='4':
#                 print('yes 4')
#             #else:
#                 #print('no')
#                 
#         for row in B1_List:
#             #print(row['Quantity'], row['Strip A'])
#             #print(row['Quantity'])# == 1:
#             if (row['Wire Gauge 1-5'])=='5':
#                 print('yes 5')
#             #else:
#                 #print('no')
#             #print(line['Wire Guage 1-5'])
         
        
async def Dec():
    '''A seperate routine to read Build Kit Two CSV'''

    with open ('BK2.csv', "r") as Build_Two:
        f2 = csv.DictReader(Build_Two)
        B2_List = list(f2)

        #print(B2_List[0]['Quantity'])
        #print(B2_List[1]['Quantity'])
        '''Rows below examine wire gauge to know which to one we will use'''
        
        for row in B2_List:
            #print(row['Quantity'], row['Strip A'])
            #print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-5'])=='0':
                print('yes')
            #else:
                #print('no')
                
        for row in B2_List:
            #print(row['Quantity'], row['Strip A'])
            #print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-5'])=='1':
                print('yes')
            #else:
                #print('no')
            
        for row in B2_List:
            #print(row['Quantity'], row['Strip A'])
            #print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-5'])=='2':
                print('yes')
            #else:
                #print('no')
                
        for row in B2_List:
            #print(row['Quantity'], row['Strip A'])
            #print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-5'])=='3':
                print('yes')
            #else:
                #print('no')
                
        for row in B2_List:
            #print(row['Quantity'], row['Strip A'])
            #print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-5'])=='4':
                print('yes')
            #else:
                #print('no')
                
        for row in B2_List:
            #print(row['Quantity'], row['Strip A'])
            #print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-5'])=='5':
                print('yes')
            #else:
                #print('no')
            #print(line['Wire Guage 1-5'])
                
async def Commands(arr):
    
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
       #Custom cut program call command
       os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
                  + str(OAL) + ' -s ' + str(strip_a_flt) + ' -c '
                  + str(strip_b_flt) + ' -n ' + str(Quantity)
                  + ' -g ' + str(Wire_Ga))
                
async def Serial():
    
    ser = serial.Serial ("/dev/ttyUSB1",9600, 8, 'N', 1, timeout=.1)
    while True:
        output = ser.readline()

        arr = (list(bytearray(output)))
        arr = list(filter((r).__ne__, arr))
        arr = list(filter((r1).__ne__, arr))
        arr = list(filter((r2).__ne__, arr))
        arr = list(filter((r3).__ne__, arr))
        arr = list(filter((r4).__ne__, arr))
        


async def main():
    ser = serial.Serial ("/dev/ttyUSB1",9600, 8, 'N', 1, timeout=.1)
    while True:
        output = ser.readline()

        arr = (list(bytearray(output)))
        arr = list(filter((r).__ne__, arr))
        arr = list(filter((r1).__ne__, arr))
        arr = list(filter((r2).__ne__, arr))
        arr = list(filter((r3).__ne__, arr))
        arr = list(filter((r4).__ne__, arr))
        #task = asyncio.create_task(Serial())
        #wire_ga = wire_ga_hmi
        
        #print(arr)
        if len(arr) >1 and arr[0]<3:
            await Commands(arr)
            
        if len(arr) >1 and arr[0]>2:
            await Rio()
        
        
        
        #await Dec()
        #await Mng()
        Quantity = []
        Wire_Ga = []
        Strip_A = []
        Strip_B = []
        OAL = []        
        Page_Num = []
        Obj_Num = []


if __name__ == '__main__':
    asyncio.run(main())

