# Threading programming test
# /home/pi/bstrip/src/
# Start Date 2/23/22

from threading import Thread
import time
import csv
import asyncio
import serial, string
import re, struct
from array import *
import os, numpy

global ready_rio
global rio_stop
global ready_mng
global mng_stop
global ready_dec
global dec_stop
global butt_text
global message
global begin_aph
global final_aph
global tetra_stop
global ready_tetra

r = 255
r1 = 101
r2 = 102
r3 = 113
r4 = 0
Page_Num = []
Obj_Num = []
rio_stop = []
ready_rio = 0
mng_stop = []
ready_mng = 0
dec_stop = []
ready_dec = 0
tetra_stop = 0
ready_tetra = 0
terminator = b'\xff\xff\xff'
start_text = str.encode("t0.txt=\"Online Test..\"")
good = str.encode("t0.txt=\"Successful\"")
end_text = str.encode("b0.txt=\"Complete\"")
begin_aph = str.encode("b0.aph=127")
final_aph = str.encode("b0.aph=0")


# butt_text = str.encode('b0.txt=\'+str(r)')
# butt_text = str.encode('b0.txt=\''+str(r))


def strip(Wire_Ga):
    os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a strip_' + str(Wire_Ga))


def advance():
    os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -a advance_10')
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
    OAL = (Obj_Num[6] / 10)
    oal = numpy.float(OAL)
    # Custom cut program call command
    os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
              + str(oal) + ' -s ' + str(strip_a_flt) + ' -c '
              + str(strip_b_flt) + ' -n ' + str(Quantity)
              + ' -g ' + str(Wire_Ga))


def RIO_PNL(arr):
    rio_wire_gauge_list = []
    Page_Num = []
    Obj_Num = []
    Page_Num = arr[0]
    Obj_Num.extend(arr)
    Wire_Ga = Obj_Num[3]
    mult = Obj_Num[4]

    global ready_rio
    ready_rio = 0
    global rio_stop
    rio_stop = 0
    global message
    global butt_text
    global begin_aph
    global final_aph
    length = 0
    ser.write(begin_aph + terminator)
    '''A seperate routine to read Build Kit One CSV'''

    with open('/home/pi/bstrip/src/RIO.csv', "r") as Build_One:
        f = csv.DictReader(Build_One)  # print(B1_List)#print(B1_List[0]['Quantity'])#print(B1_List[1]['Quantity'])
        B1_List = list(f)
        '''Rows below examine wire gauge to know which to one we will use'''
        for row in B1_List:  # print(row['Quantity'], row['Strip A'])#print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-9']) == str(Wire_Ga):
                rio_wire_gauge_list.append(row)

        for row in rio_wire_gauge_list:
            Q = (row['Quantity'])
            W = (row['Wire Gauge 1-9'])
            SA = float(row['Strip A'])
            SB = float(row['Strip B'])
            OAL = float(row['OAL'])
            exq = Q * mult
            message = str(OAL)
            butt_text = str.encode("b0.txt=\"" + message + " in. next\"")
            ser.write(butt_text + terminator)
            print(butt_text + terminator)
            while ready_rio == 0:
                time.sleep(.25)
            if rio_stop == 1:
                print('stop_pressed')
                break
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
                      + str(OAL) + ' -s ' + str(SA) + ' -c '
                      + str(SB) + ' -n ' + str(exq)
                      + ' -g ' + str(W))

            prev_text = str.encode("t0.txt=\"" + message + " in. Done\"")
            ser.write(prev_text + terminator)
            ready_rio = 0
            Q = []
            W = []
            SA = []
            SB = []
            OAL = []
            ser.write(end_text + terminator)
            if rio_stop == 1:
                print('stop_pressed')
                break

        ser.write(final_aph + terminator)


def MNG_PNL(arr):
    mng_wire_gauge_list = []
    Page_Num = []
    Obj_Num = []
    Page_Num = arr[0]
    Obj_Num.extend(arr)
    Wire_Ga = Obj_Num[3]
    mult = Obj_Num[4]

    global ready_mng
    ready_mng = 0
    global mng_stop
    mng_stop = 0
    global message
    global butt_text
    global begin_aph
    global final_aph
    length = 0
    '''A seperate routine to read Build Kit One CSV'''

    with open('/home/pi/bstrip/src/MNG.csv', "r") as Build_Two:
        f = csv.DictReader(Build_Two)  # print(B1_List)#print(B1_List[0]['Quantity'])#print(B1_List[1]['Quantity'])
        B2_List = list(f)
        '''Rows below examine wire gauge to know which to one we will use'''
        for row in B2_List:  # print(row['Quantity'], row['Strip A'])#print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-9']) == str(Wire_Ga):
                mng_wire_gauge_list.append(row)

        for row in mng_wire_gauge_list:
            Q = (row['Quantity'])
            W = (row['Wire Gauge 1-9'])
            SA = float(row['Strip A'])
            SB = float(row['Strip B'])
            OAL = float(row['OAL'])
            exq = Q * mult
            message = str(OAL)
            butt_text = str.encode("b0.txt =\"" + message + " in. next\"")
            ser.write(butt_text + terminator)
            print(butt_text + terminator)
            while ready_mng == 0:
                time.sleep(.25)
            if mng_stop == 1:
                print('stop_pressed')
                break
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
                      + str(OAL) + ' -s ' + str(SA) + ' -c '
                      + str(SB) + ' -n ' + str(exq)
                      + ' -g ' + str(W))

            prev_text = str.encode("t0.txt=\"" + message + "in. Done\"")
            ser.write(prev_text + terminator)
            ready_mng = 0
            Q = []
            W = []
            SA = []
            SB = []
            OAL = []
            ser.write(end_text + terminator)
            if mng_stop == 1:
                print('stop_pressed')
                break
        ser.write(final_aph + terminator)

def DEC_PNL(arr):


    dec_wire_gauge_list = []
    Page_Num = []
    Obj_Num = []
    Page_Num = arr[0]
    Obj_Num.extend(arr)
    Wire_Ga = Obj_Num[3]
    mult = Obj_Num[4]

    global ready_dec
    ready_dec = 0
    global dec_stop
    dec_stop = 0
    global message
    global butt_text
    global begin_aph
    global final_aph
    length = 0
    ser.write(begin_aph + terminator)
    '''A seperate routine to read Build Kit One CSV'''

    with open('/home/pi/bstrip/src/DEC.csv', "r") as Build_Three:
        f = csv.DictReader(Build_Three)  # print(B1_List)#print(B1_List[0]['Quantity'])#print(B1_List[1]['Quantity'])
        B3_List = list(f)
        '''Rows below examine wire gauge to know which to one we will use'''
        for row in B3_List:  # print(row['Quantity'], row['Strip A'])#print(row['Quantity'])# == 1:
            if (row['Wire Gauge 1-9']) == str(Wire_Ga):
                dec_wire_gauge_list.append(row)

        for row in dec_wire_gauge_list:
            Q = (row['Quantity'])
            W = (row['Wire Gauge 1-9'])
            SA = float(row['Strip A'])
            SB = float(row['Strip B'])
            OAL = float(row['OAL'])
            exq = Q * mult
            message = str(OAL)
            butt_text = str.encode("b0.txt=\"" + message + " in.next\"")
            ser.write(butt_text + terminator)
            print(butt_text + terminator)
            while ready_dec == 0:
                time.sleep(.25)
            if dec_stop == 1:
                print('stop_pressed')
                break
            os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
                      + str(OAL) + ' -s ' + str(SA) + ' -c '
                      + str(SB) + ' -n ' + str(exq)
                      + ' -g ' + str(W))
            prev_text = str.encode("t0.txt=\"" + message + " in.Done\"")
            ser.write(prev_text + terminator)
            ready_dec = 0
            Q = []
            W = []
            SA = []
            SB = []
            OAL = []
            ser.write(end_text + terminator)
            if dec_stop == 1:
                print('stop_pressed')
                break

        ser.write(final_aph + terminator)


def Tetra(arr):
    print(arr)

    Page_Num = []
    Obj_Num = []
    Obj_Num.extend(arr)
    Wire_L = Obj_Num[2]
    Quantity = Obj_Num[3]
    #print(Obj_Num)
    global ready_tetra
    ready_tetra = 0
    global tetra_stop
    tetra_stop = 0
    global message
    global butt_text
    global begin_aph
    global final_aph
    ser.write(final_aph + terminator)

    if Wire_L == 1:
        oal = 6 * 2.54
    if Wire_L == 2:
        oal = 12 * 2.54
    if Wire_L == 3:
        oal = 24 * 2.54
    if Wire_L == 4:
        oal = 30 * 2.54
    if Wire_L == 5:
        oal = 36 * 2.54
    if Wire_L == 6:
        oal = 42 * 2.54
    if Wire_L == 7:
        oal = 48 * 2.54
    if Wire_L == 8:
        oal = 54 * 2.54
    if Wire_L == 9:
        oal = 60 * 2.54
    if Wire_L == 10:
        oal = 66 * 2.54
    if Wire_L == 11:
        oal = 72 * 2.54
    if Wire_L == 12:
        oal = 78 * 2.54
    if Wire_L == 13:
        oal = 84 * 2.54

    print(oal)
    # Tetra PAk program call
    os.system('sudo python3 /home/pi/bstrip/src/Cutwire1.py -l '
              + str(oal) + ' -s 1.2 -c 1.2 -n ' + str(Quantity)
              + ' -g 3')

    ser.write(final_aph + terminator)

def status():
        ser.write(start_text + terminator)
        time.sleep(2)
        ser.write(good + terminator)

ser = serial.Serial ("/dev/ttyUSB0", 9600, 8, 'N', 1, timeout=.1)
while True:
    output = ser.readline()

    arr = (list(bytearray(output)))
    arr = list(filter((r).__ne__, arr))
    arr = list(filter((r1).__ne__, arr))
    arr = list(filter((r2).__ne__, arr))
    arr = list(filter((r3).__ne__, arr))
    arr = list(filter((r4).__ne__, arr))
#     print(arr)
    if len(arr) > 1:
        Obj_Num.extend(arr)

    #     `TASK 1`
    task1 = Thread(target=advance, args=[])  # task to advance wire 3 cm

    if len(Obj_Num) > 0 and Page_Num == 2 and Obj_Num[1] == 7:
        if len(Obj_Num) > 2:
            task1.start()

    #     ```TASK 2```
    if len(Obj_Num) > 3 and Page_Num == 2 and Obj_Num[1] == 6:
        Wire_Ga = Obj_Num[3]
        task2 = Thread(target=strip, args=[Wire_Ga])
        print(Wire_Ga)
        task2.start()

    #     ```TASK 3```
    task3 = Thread(target=release, args=[])  # task to open cutter

    if len(Obj_Num) > 0 and Page_Num == 2 and Obj_Num[1] == 5:
        print('Open Stripper')
        task3.start()

    #     ```TASK 4```
    task4 = Thread(target=fullcut, args=[])  # task to cut completely through the wire

    if len(Obj_Num) > 0 and Page_Num == 2 and Obj_Num[1] == 4:
        print('Full Cut')
        task4.start()

    #     ```TASK 5```
    task5 = Thread(target=custom, args=[Obj_Num])  # task to perform a custom cut

    if len(Obj_Num) > 6 and Page_Num == 1 and Obj_Num[1] == 6:
        task5 = Thread(target=custom, args=[Obj_Num])
        task5.start()

    #     ```TASK 6```
    task6 = Thread(target=RIO_PNL, args=[arr])  # task to perform build cut

    if len(arr) > 3 and arr[0] == 5:
        task6.start()

    if len(arr) > 1 and arr[0] == 5 and arr[1] == 5:
        rio_stop = 1

    if len(arr) > 1 and arr[0] == 5 and arr[1] == 8:
        ready_rio = 1

    #     ```TASK 7```
    task7 = Thread(target=MNG_PNL, args=[arr])  # task to perform build cut

    if len(arr) > 3 and arr[0] == 6:
        task7.start()

    if len(arr) > 1 and arr[0] == 6 and arr[1] == 5:
        mng_stop = 1

    if len(arr) > 1 and arr[0] == 6 and arr[1] == 8:
        ready_mng = 1

    #     ```TASK 8```
    task8 = Thread(target=DEC_PNL, args=[arr])  # task to perform build cut

    if len(arr) > 3 and arr[0] == 7:
        task8.start()

    if len(arr) > 1 and arr[0] == 7 and arr[1] == 5:
        dec_stop = 1

    if len(arr) > 1 and arr[0] == 7 and arr[1] == 8:
        ready_dec = 1

    #     ```TASK 9```
    task9 = Thread(target=Tetra, args=[arr]) # task to perform length based auto cuts for Tetra Pak
    
    if len(arr) == 1:
        Page_Num = arr[0]
#     if Page_Num == 10 and Obj_Num[0] == 3:
#         task9.start()
    #print(Page_Num)
    if len(arr) > 1 and Page_Num ==10 and Obj_Num[0] == 3:
        task9.start()
        Page_Num = []
    
    if len(arr) > 1 and arr[0] == 10 and arr[1] == 4:
        tetra_stop =1

    if len(arr) > 1 and arr[0] == 10 and arr[1] == 7:
        ready_tetra = 1

    #   ```Status Check```
    task10 = Thread(target=status)
    
    if len(arr) > 1 and arr[0] == 5 and arr[1] == 1:
        task10.start()


    
    Obj_Num = []