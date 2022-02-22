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
rio_wire_gauge_list = []
Wire_Ga = []




async def Rio(arr):
    Page_Num = []
    Obj_Num = []
    Page_Num = arr[0]
    Obj_Num.extend(arr)
    Wire_Ga = Obj_Num[3]
    print(Wire_Ga)
    '''A seperate routine to read Build Kit One CSV'''
    
    with open ('/home/pi/bstrip/src/BK1.csv', "r") as Build_One:
        f = csv.DictReader(Build_One)#print(B1_List)#print(B1_List[0]['Quantity'])#print(B1_List[1]['Quantity'])
        B1_List = list(f)           
        '''Rows below examine wire gauge to know which to one we will use'''
        for row in B1_List:#print(row['Quantity'], row['Strip A'])#print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-9'])==str(Wire_Ga):
                rio_wire_gauge_list.append(row)                
                print(rio_wire_gauge_list)
        for row in rio_wire_gauge_list:
            Q =(row['Quantity'])
            W =(row['Wire Gauge 1-9'])
            SA =(row['Strip A'])
            SB =(row['Strip B'])
            OAL =(row['OAL'])
            #sa =SA/10
            print(Q)
            print(W)
            print(SA)
            print(SB)
            print(OAL)
            
            
#             os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
#                   + str(oal) + ' -s ' + str(strip_a_flt) + ' -c '
#                   + str(strip_b_flt) + ' -n ' + str(Quantity)
#                   + ' -g ' + str(Wire_Ga))
        #print(rio_wire_gauge_list[1])
                #print(B1_List[row]['Quantity'])
                #print(B1_List[1]['Quantity'])
                #print(row[B1_List])
                
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
    Page_Num = []
    Obj_Num = []
    
    if len(arr) >1: 
        Page_Num = arr[0]
        Obj_Num.extend(arr)
        print(Obj_Num)
        
    #if Manual feed Forward button is pressed
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==7:
        if len(Obj_Num)> 2:
            #print('advance 3cm')
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a advance_3')
        #else:
            #print('stop')
            
    #if Strip Test button on HMI is pressed populates wire gauge
    if len(Obj_Num) >3 and Page_Num == 2 and Obj_Num[1] ==6:
        Wire_Ga = Obj_Num[3]
        print(Wire_Ga)
        os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a strip_' + str(Wire_Ga))
    
    #if Manual open button on HMI is pressed 
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==5:
        print('Open Stripper')
        os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a release')
        
    #if Manual close button on HMI is pressed 
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==4:
        print('Full Cut')
        os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a break')
    
    #if But button on the Custom Cut page of HMI is pressed
    #then all run data is populated for a custom cut job
    if len(Obj_Num) >6 and Page_Num == 1 and Obj_Num[1] ==6:
       Quantity = Obj_Num[3]
       Wire_Ga = Obj_Num[4]
       Strip_A = (Obj_Num[5] / 10)
       strip_a_flt = numpy.float(Strip_A)
       Strip_B = (Obj_Num[5] / 10)
       strip_b_flt = numpy.float(Strip_B)
       OAL = (Obj_Num[6]/10)
       oal = numpy.float(OAL)
       #Custom cut program call command
       os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
                  + str(oal) + ' -s ' + str(strip_a_flt) + ' -c '
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
    ser = serial.Serial ("/dev/ttyUSB0",9600, 8, 'N', 1, timeout=.1)
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
            
        if len(arr)==5 and arr[0]==5:
            print(arr)
            await Rio(arr)
        
        
        
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

