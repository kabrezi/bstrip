# Threading programming test
#/home/pi/bstrip/src/
# Start Date 2/23/22

from threading import Thread
import time
import csv
import asyncio
import serial, string
import re, struct
from array import *
import os, numpy


r = 255
r1 = 101
r2 = 102
r3 = 113
r4 = 0
Page_Num = []
Obj_Num = []
rio_stop=[]
ready_rio=0
x=0
terminator = b'\xff\xff\xff'
butt_text = str.encode('b0.txt=\"begin\"')
# butt_text = str.encode('b0.txt=\'+str(r)')
# butt_text = str.encode('b0.txt=\''+str(r))


def strip(Wire_Ga):
    os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a strip_' + str(Wire_Ga))


def advance():
    os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a advance_3')
    print('done')
    
def release():
    os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a release')

def fullcut():
    os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a break')
    
def custom(Obj_Num):
    
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
    
def RIO_PNL(arr, rio_stop, ready_rio, x):
    
    rio_wire_gauge_list = []
    Page_Num = []
    Obj_Num = []
    Page_Num = arr[0]
    Obj_Num.extend(arr)
    Wire_Ga = Obj_Num[3]
    mult=Obj_Num[4]
    #print(Wire_Ga)
    #print(rio_stop)
    '''A seperate routine to read Build Kit One CSV'''
    
    with open ('/home/pi/bstrip/src/BK1.csv', "r") as Build_One:
        f = csv.DictReader(Build_One)#print(B1_List)#print(B1_List[0]['Quantity'])#print(B1_List[1]['Quantity'])
        B1_List = list(f)
        #print(B1_List)
        '''Rows below examine wire gauge to know which to one we will use'''
        for row in B1_List:#print(row['Quantity'], row['Strip A'])#print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-9'])==str(Wire_Ga):
                rio_wire_gauge_list.append(row)
                
                #print(rio_wire_gauge_list)
        for row in rio_wire_gauge_list:
            Q =(row['Quantity'])
            W =(row['Wire Gauge 1-9'])
            SA =float(row['Strip A'])
            SB =float(row['Strip B'])
            OAL =float(row['OAL'])
            #sa =SA/10
            exq =Q*mult
            print(Q, W, SA, SB, OAL)
            ser.write(butt_text + terminator)
#             print('sleeping')
# #             if ready_rio==0:
# #                 print(x)
# #                 time.sleep(x)
#             if ready_rio==0:
# #                 x = x+.25
#                 print(x)
#             time.sleep(x)
#             print('ready pressed')
            #while ready_rio==0:
                #print(ready_rio)
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
                  + str(OAL) + ' -s ' + str(SA) + ' -c '
                  + str(SB) + ' -n ' + str(exq)
                  + ' -g ' + str(W))
#                 elseif:
#                     sleep(5)
                #ready_rio=1
                #print(ready_rio)
#             ready_rio=0
            Q=[]
            W=[]
            SA=[]
            SB=[]
            OAL=[]
            if rio_stop==1:
                print('stop_pressed')
                break

ser = serial.Serial ("/dev/ttyUSB0",9600, 8, 'N', 1, timeout=.1)
while True:
    output = ser.readline()

    arr = (list(bytearray(output)))
    arr = list(filter((r).__ne__, arr))
    arr = list(filter((r1).__ne__, arr))
    arr = list(filter((r2).__ne__, arr))
    arr = list(filter((r3).__ne__, arr))
    arr = list(filter((r4).__ne__, arr))
    #print(arr)
    task1 = Thread(target=advance, args=[])
    task3 = Thread(target=release, args=[])
    task4 = Thread(target=fullcut, args=[])
    task5 = Thread(target=custom, args=[Obj_Num])
    task6 = Thread(target=RIO_PNL, args=[arr,rio_stop,ready_rio,x])
    Page_Num=[]
    Obj_Num=[]
    #ready_rio=0
    
    if len(arr) >1:
        Page_Num = arr[0]
        Obj_Num.extend(arr)
    
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==7:
        if len(Obj_Num)> 2:
            task1.start()
    
    if len(Obj_Num) >3 and Page_Num == 2 and Obj_Num[1] ==6:
        Wire_Ga = Obj_Num[3]
        task2 = Thread(target=strip, args=[Wire_Ga])
        print(Wire_Ga)
        task2.start()
    
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==5:
        print('Open Stripper')
        task3.start()
        
    if len(Obj_Num) >0 and Page_Num == 2 and Obj_Num[1] ==4:
        print('Full Cut')
        task4.start()
        
    if len(Obj_Num) >6 and Page_Num == 1 and Obj_Num[1] ==6:
        task5 = Thread(target=custom, args=[Obj_Num])
        task5.start()
        
    if len(arr) >3 and arr[0]==5:
        task6.start()
        
    if len(arr) >1 and arr[0]==5 and arr[1]==5:
        rio_stop=1
    #if not len(arr) >1 and arr[0]==5 and arr[1]==8:

#         ready_rio=0
#         time.sleep(5)
    #if len(arr) >1 and arr[0]==5 and arr[1]==8:
        #ready_rio=1
        
#     if len(arr) >1:
#         if arr[0]==5 and arr[1]==8:
#             ready_rio=1
#             x=0
#             print(x)
#     if ready_rio==0:
#         x = x+.25
#         print(x)
#         ready_rio=0
    


# def say_after(delay, what):
#     print(time.time(),'Start say_after(%s, %s)' % (delay,what))
#     time.sleep(delay)
#     print(time.time(),what)
# 
# start_time = time.time()
# print(start_time, 'Before creating tasks.')
# task1 = Thread(target=say_after, args=[1, 'hello'])
# task2 = Thread(target=say_after, args=[2, 'world'])
# task1.start()
# task2.start()   
# print(time.time(),"Before delay - after creating tasks")
# time.sleep(3)
# print(time.time(),"After delay - before await tasks")
# task1.join()
# task2.join()
# end_time = time.time()
# print('Total time elapsed: %.2f seconds' % (end_time - start_time)) 