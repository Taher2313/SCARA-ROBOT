import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import time
import os
LANG="en_US.UTF-8"


def keep_in_range(val, min_val, max_val):
    return min(max_val, max(min_val, val))


def round_T(T, f):  # this is a function used for rounding the 4x4 matrix by value f
    T[0, 0] = round(T[0, 0], f)
    T[0, 1] = round(T[0, 1], f)
    T[0, 2] = round(T[0, 2], f)
    T[0, 3] = round(T[0, 3], f)

    T[1, 0] = round(T[1, 0], f)
    T[1, 1] = round(T[1, 1], f)
    T[1, 2] = round(T[1, 2], f)
    T[1, 3] = round(T[1, 3], f)

    T[2, 0] = round(T[2, 0], f)
    T[2, 1] = round(T[2, 1], f)
    T[2, 2] = round(T[2, 2], f)
    T[2, 3] = round(T[2, 3], f)

    T[3, 0] = round(T[3, 0], f)
    T[3, 1] = round(T[3, 1], f)
    T[3, 2] = round(T[3, 2], f)
    T[3, 3] = round(T[3, 3], f)

    return (T)


root = tk.Tk()
canvas = tk.Canvas(root,width=1300,height=525, bg = "#777777")
canvas.pack(expand = YES , fill = BOTH  )


## set the title of the window
title  =root.title("Scara Robot")

## put the Scara robot icon beside the title
root.iconbitmap("the400_e6i_icon.ico")


##create multiple frame so i can use them to insert input fields

## row ====>  0
frame0 = tk.Frame(root)
frame0.place(relwidth = 0.5384615385, relheight = 0.07 , relx= 0.038461538,rely= 0.08)
label0 = Label(frame0, text=''' Scara Robot " RRPR "''' , bg= "#68f558")
label0.place(relwidth = 1,relheight = 1)

## =======================> row 1 <=============================
frame1 = tk.Frame(root)
frame1.place(relwidth = 0.1057692308, relheight = 0.05 , relx= 0.038461538 ,  rely= 0.2)
frame2 = tk.Frame(root)
frame2.place(relwidth = 0.1057692308, relheight = 0.05 , relx= 0.1826923077 , rely= 0.2)
frame3 = tk.Frame(root)
frame3.place(relwidth = 0.1057692308, relheight = 0.05 , relx= 0.3269230769 ,  rely= 0.2)
frame17 = tk.Frame(root)
frame17.place(relwidth = 0.1057692308, relheight = 0.05 , relx= 0.4711538462 , rely= 0.2)

thelabel = Label(frame1, text=''' {}1 "in degrees" '''.format(str("\u03F4")))
thelabel2 = Label(frame2,text=''' {}2 "in degrees" '''.format(str("\u03F4")))
thelabel3 = Label(frame3, text=''' D3 "in mm" ''')
thelabel7 = Label(frame17, text=''' {}4 "in degrees" '''.format(str("\u03F4")))

thelabel.place(relwidth = 1,relheight = 1)
thelabel2.place(relwidth = 1,relheight = 1)
thelabel3.place(relwidth = 1,relheight = 1)
thelabel7.place(relwidth = 1,relheight = 1)



## =======================> row 2 <=============================
frame4 = tk.Frame(root)
frame4.place(relwidth = 0.1057692308, relheight = 0.05 , relx= 0.038461538 , rely= 0.27)
frame5 = tk.Frame(root)
frame5.place(relwidth = 0.1057692308, relheight = 0.05 , relx= 0.1826923077 , rely= 0.27)
frame6 = tk.Frame(root)
frame6.place(relwidth = 0.1057692308, relheight = 0.05 , relx= 0.3269230769 , rely= 0.27)
frame16 = tk.Frame(root)
frame16.place(relwidth = 0.1057692308, relheight = 0.05 , relx= 0.4711538462 , rely= 0.27)


## entries
entry1 = Entry(frame4,width = 20 )
entry2 = Entry(frame5,width = 30 )
entry3 = Entry(frame6,width = 30 )
entry4 = Entry(frame16,width = 30 )


entry1.place(relwidth = 1,relheight = 1)
entry2.place(relwidth = 1,relheight = 1)
entry3.place(relwidth = 1,relheight = 1)
entry4.place(relwidth = 1,relheight = 1)


## =======================> row 7 <=============================
frame13 = tk.Frame(root)
frame13.place(relwidth = 0.5384615385, relheight = 0.05 , relx= 0.038461538 , rely= 0.73)
frame14 = tk.Frame(root)
frame14.place(relwidth = 0.5384615385, relheight = 0.05 , relx= 0.038461538 , rely= 0.8)
frame15 = tk.Frame(root)
frame15.place(relwidth = 0.5384615385, relheight = 0.05 , relx= 0.038461538, rely= 0.87)

## =======================> row 5 <=============================
frame9 = tk.Frame(root)
frame9.place(relwidth = 0.1538461538, relheight = 0.05 , relx= 0.038461538 ,  rely= 0.56)
frame10 = tk.Frame(root)
frame10.place(relwidth = 0.1538461538, relheight = 0.05 , relx= 0.2307692308 , rely= 0.56)
frame11 = tk.Frame(root)
frame11.place(relwidth = 0.1538461538, relheight = 0.05 , relx= 0.4230769231 , rely= 0.56)

## prepare calculations
# constants in meters "from tha datasheet of the THP700 type"
L1 = 350;
L2 = 300;
d1 = 200;
d4 = 40;
# constrains on the range, all are +ve or -ve, in degrees and meters
rangeAxis1 = 148;
rangeAxis2 = 150;
rangeAxis3 = 210;
rangeAxis4 = 720;
##open image file
##Nada###

SCARA_RB = ImageTk.PhotoImage(
    Image.open('BLUUUP - Copy'
                '\ScaraRobot' + '1000' + '.png'))
label110 = Label(root, image=SCARA_RB)

label110.place(relx=0, rely=0, relheight=0.0001 , relwidth= 0.0001)


SCARA_RB2 = ImageTk.PhotoImage(
    Image.open('BLUUUP - Copy'
                '\ScaraRobot' + '1000' + '.png'))
label111 = Label(root, image=SCARA_RB2)

label111.place(relx=0, rely=0, relheight=0.0001 , relwidth= 0.0001)

label112= Label(root, image=SCARA_RB2)
label112.place(relx=0, rely=0, relheight=0.0001 , relwidth= 0.0001)

label113= Label(root, image=SCARA_RB2)
label113.place(relx=0, rely=0, relheight=0.0001 , relwidth= 0.0001)


R1 = 0
R2 =0
P = 0
R1N = 0
R2N = 0
PN = 0

def calc():
    global SCARA_RB
    global SCARA_RB2
    global SCARA_Isoo
    global SCARA_Topo
    global label112
    global label113
    global canvas
    global R1
    global R2
    global P
    global R1N
    global R2N
    global PN


    R1N = z1 = float(entry1.get())
    R2N = z2 = float(entry2.get())
    PN = d3 = float(entry3.get())
    z4 = float(entry4.get())

    z1 = keep_in_range(z1, -rangeAxis1, rangeAxis1);
    A1 = np.matrix([[round(np.cos(z1 * np.pi / 180), 5), round(-1 * np.sin(z1 * np.pi / 180), 5), 0,
                     round(L1 * np.cos(z1 * np.pi / 180), 5)],
                    [round(np.sin(z1 * np.pi / 180), 5), round(np.cos(z1 * np.pi / 180), 5), 0,
                     round(L1 * np.sin(z1 * np.pi / 180), 5)],
                    [0, 0, 1, d1],
                    [0, 0, 0, 1]])
    z2 = keep_in_range(z2, -rangeAxis2, rangeAxis2);
    A2 = np.matrix([[round(np.cos(z2 * np.pi / 180), 5), round(np.sin(z2 * np.pi / 180), 5), 0,
                     round(L2 * np.cos(z2 * np.pi / 180), 5)],
                    [round(np.sin(z2 * np.pi / 180), 5), round(-1 * np.cos(z2 * np.pi / 180), 5), 0,
                     round(L2 * np.sin(z2 * np.pi / 180), 5)],
                    [0, 0, -1, 0],
                    [0, 0, 0, 1]])

    d3 = keep_in_range(d3, -

    rangeAxis3, rangeAxis3);
    A3 = np.matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, d3],
                    [0, 0, 0, 1]])
    z4 = keep_in_range(z4, -rangeAxis4, rangeAxis4);
    A4 = np.matrix([[round(np.cos(z4 * np.pi / 180), 5), round(-1 * np.sin(z4 * np.pi / 180), 5), 0, 0],
                    [round(np.sin(z4 * np.pi / 180), 5), round(np.cos(z4 * np.pi / 180), 5), 0, 0],
                    [0, 0, 1, d4],
                    [0, 0, 0, 1]])

    T = np.dot(np.dot(A1, A2), np.dot(A3, A4))

    R1N = z1 * (120 / 148 )
    R2N = z2 * (145 / 150 )
    PN = d3  * (150 / 210)
    z4 = float(entry4.get())

    if R1N > 120:
        R1N = 120
    if R1N < -120:
        R1N = -120

    if R2N > 145:
        R2N = 145
    if R2N < -145:
        R2N = -145

    if PN > 150:
        PN = 150
    if PN < 0:
        PN = 0
    z0 = R1N
    z1 = R2N
    d3 = PN
    R1_IMGN = round(R1N / 15) + 8
    R2_IMGN = round(R2N / 14.5) + 10
    P_IMGN = round(PN / 30)

    R1_IMG = round(R1 / 15) + 8
    R2_IMG = round(R2 / 14.5) + 10
    P_IMG = round(P / 30)


    num = int(round(R1 / 15) + 8 + round(R2 / 14.5 + 10) * 17 + round(P / 30) * 357)

    numtop = num % 357

    numstriso = num.__str__()
    numstrtop = numtop.__str__()

    if num < 1000:
        numstriso = "0" + numstriso

    if num < 100:
        numstriso = "0" + numstriso

    if num < 10:
        numstriso = "0" + numstriso

    if numtop < 1000:
        numstrtop = "0" + numstrtop

    if numtop < 100:
        numstrtop = "0" + numstrtop

    if numtop < 10:
        numstrtop = "0" + numstrtop

    SCARA_Iso = ImageTk.PhotoImage(
        Image.open('BLUUUP - Copy'
                   + '/ScaraRobot' + numstriso + '.png'))

    SCARA_Top = ImageTk.PhotoImage(
        Image.open('BLUP - Copy - Copy'
                   + '/ScaraRobot' + numstrtop + '.png'))

    label110 = Label(canvas, image=SCARA_Iso ,bg= "#777777")

    label110.place(relx=0.6153846154, rely=0, relheight=0.5 , relwidth = 0.3846153846)

    label111 = Label(canvas, image=SCARA_Top, bg="#777777")

    label111.place(relx=0.6153846154, rely=0.5, relheight=0.5, relwidth=0.3846153846)

    time.sleep(1)

    label110.destroy()
    label111.destroy()

    while R1_IMGN > R1_IMG:

        numstriso = num.__str__()
        numstrtop = numtop.__str__()

        if num < 1000:
            numstriso = "0" + numstriso

        if num < 100:
            numstriso = "0" + numstriso

        if num < 10:
            numstriso = "0" + numstriso

        if numtop < 1000:
            numstrtop = "0" + numstrtop

        if numtop < 100:
            numstrtop = "0" + numstrtop

        if numtop < 10:
            numstrtop = "0" + numstrtop

        SCARA_Iso = ImageTk.PhotoImage(
            Image.open('BLUUUP - Copy'
                       + '/ScaraRobot' + numstriso + '.png'))
        label110 = Label(canvas, image=SCARA_Iso, bg="#777777")

        label110.place(relx=0.6153846154, rely=0, relheight=0.5, relwidth=0.3846153846)

        SCARA_Top = ImageTk.PhotoImage(
            Image.open('BLUP - Copy - Copy'
                       + '/ScaraRobot' + numstrtop + '.png'))
        label111 = Label(canvas, image=SCARA_Top, bg="#777777")

        label111.place(relx=0.6153846154, rely=0.5, relheight=0.5, relwidth=0.3846153846)

        time.sleep(0.1)
        num = num + 1
        R1_IMG = R1_IMG + 1
        numtop = numtop + 1
        root.update()

        label110.destroy()
        label111.destroy()

    while R1_IMGN < R1_IMG:

        numstriso = num.__str__()
        numstrtop = numtop.__str__()

        if num < 1000:
            numstriso = "0" + numstriso

        if num < 100:
            numstriso = "0" + numstriso

        if num < 10:
            numstriso = "0" + numstriso

        if numtop < 1000:
            numstrtop = "0" + numstrtop

        if numtop < 100:
            numstrtop = "0" + numstrtop

        if numtop < 10:
            numstrtop = "0" + numstrtop

        SCARA_Iso = ImageTk.PhotoImage(
            Image.open('BLUUUP - Copy'
                       + '/ScaraRobot' + numstriso + '.png'))
        label110 = Label(canvas, image=SCARA_Iso, bg="#777777")

        label110.place(relx=0.6153846154, rely=0, relheight=0.5, relwidth=0.3846153846)

        SCARA_Top = ImageTk.PhotoImage(
            Image.open('BLUP - Copy - Copy'
                       + '/ScaraRobot' + numstrtop + '.png'))
        label111 = Label(canvas, image=SCARA_Top, bg="#777777")

        label111.place(relx=0.6153846154, rely=0.5, relheight=0.5, relwidth=0.3846153846)

        time.sleep(0.1)
        num = num - 1
        R1_IMGN = R1_IMGN + 1
        numtop = numtop - 1
        root.update()

        label110.destroy()
        label111.destroy()

    while R2_IMGN > R2_IMG:

        numstriso = num.__str__()
        numstrtop = numtop.__str__()

        if num < 1000:
            numstriso = "0" + numstriso

        if num < 100:
            numstriso = "0" + numstriso

        if num < 10:
            numstriso = "0" + numstriso

        if numtop < 1000:
            numstrtop = "0" + numstrtop

        if numtop < 100:
            numstrtop = "0" + numstrtop

        if numtop < 10:
            numstrtop = "0" + numstrtop

        SCARA_Iso = ImageTk.PhotoImage(
            Image.open('BLUUUP - Copy'
                       + '/ScaraRobot' + numstriso + '.png'))
        label110 = Label(canvas, image=SCARA_Iso, bg="#777777")

        label110.place(relx=0.6153846154, rely=0, relheight=0.5, relwidth=0.3846153846)

        SCARA_Top = ImageTk.PhotoImage(
            Image.open('BLUP - Copy - Copy'
                       + '/ScaraRobot' + numstrtop + '.png'))
        label111 = Label(canvas, image=SCARA_Top, bg="#777777")

        label111.place(relx=0.6153846154, rely=0.5, relheight=0.5, relwidth=0.3846153846)

        time.sleep(0.1)
        num = num + 17
        R2_IMG = R2_IMG + 1
        numtop = numtop + 17
        root.update()

        label110.destroy()
        label111.destroy()

    while R2_IMGN < R2_IMG:

        numstriso = num.__str__()
        numstrtop = numtop.__str__()

        if num < 1000:
            numstriso = "0" + numstriso

        if num < 100:
            numstriso = "0" + numstriso

        if num < 10:
            numstriso = "0" + numstriso

        if numtop < 1000:
            numstrtop = "0" + numstrtop

        if numtop < 100:
            numstrtop = "0" + numstrtop

        if numtop < 10:
            numstrtop = "0" + numstrtop

        SCARA_Iso = ImageTk.PhotoImage(
            Image.open('BLUUUP - Copy'
                       + '/ScaraRobot' + numstriso + '.png'))

        label110 = Label(canvas, image=SCARA_Iso, bg="#777777")

        label110.place(relx=0.6153846154, rely=0, relheight=0.5, relwidth=0.3846153846)

        SCARA_Top = ImageTk.PhotoImage(
            Image.open('BLUP - Copy - Copy'
                       + '/ScaraRobot' + numstrtop + '.png'))

        label111 = Label(canvas, image=SCARA_Top, bg="#777777")

        label111.place(relx=0.6153846154, rely=0.5, relheight=0.5, relwidth=0.3846153846)

        time.sleep(0.1)
        num = num - 17
        R2_IMGN = R2_IMGN + 1
        numtop = numtop - 17
        root.update()

        label110.destroy()
        label111.destroy()

    while P_IMGN > P_IMG:

        numstriso = num.__str__()
        numstrtop = numtop.__str__()

        if num < 1000:
            numstriso = "0" + numstriso

        if num < 100:
            numstriso = "0" + numstriso

        if num < 10:
            numstriso = "0" + numstriso

        if numtop < 1000:
            numstrtop = "0" + numstrtop

        if numtop < 100:
            numstrtop = "0" + numstrtop

        if numtop < 10:
            numstrtop = "0" + numstrtop

        SCARA_Iso = ImageTk.PhotoImage(
            Image.open('BLUUUP - Copy'
                       + '/ScaraRobot' + numstriso + '.png'))

        label110 = Label(canvas, image=SCARA_Iso, bg="#777777")

        label110.place(relx=0.6153846154, rely=0, relheight=0.5, relwidth=0.3846153846)

        SCARA_Top = ImageTk.PhotoImage(
            Image.open('BLUP - Copy - Copy'
                       + '/ScaraRobot' + numstrtop + '.png'))

        label111 = Label(canvas, image=SCARA_Top, bg="#777777")

        label111.place(relx=0.6153846154, rely=0.5, relheight=0.5, relwidth=0.3846153846)

        time.sleep(0.1)
        num = num + 357
        P_IMG = P_IMG + 1
        root.update()

        label110.destroy()
        label111.destroy()

    while P_IMGN < P_IMG:


        numstriso = num.__str__()
        numstrtop = numtop.__str__()

        if num < 1000:
            numstriso = "0" + numstriso

        if num < 100:
            numstriso = "0" + numstriso

        if num < 10:
            numstriso = "0" + numstriso

        if numtop < 1000:
            numstrtop = "0" + numstrtop

        if numtop < 100:
            numstrtop = "0" + numstrtop

        if numtop < 10:
            numstrtop = "0" + numstrtop

        SCARA_Iso = ImageTk.PhotoImage(
            Image.open('BLUUUP - Copy'
                       + '/ScaraRobot' + numstriso + '.png'))

        label110 = Label(canvas, image=SCARA_Iso, bg="#777777")

        label110.place(relx=0.6153846154, rely=0, relheight=0.5, relwidth=0.3846153846)

        SCARA_Top = ImageTk.PhotoImage(
            Image.open('BLUP - Copy - Copy'
                       + '/ScaraRobot' + numstrtop + '.png'))

        label111 = Label(canvas, image=SCARA_Top, bg="#777777")

        label111.place(relx=0.6153846154, rely=0.5, relheight=0.5, relwidth=0.3846153846)

        time.sleep(0.1)
        num = num - 357
        P_IMGN = P_IMGN + 1
        root.update()

        label110.destroy()
        label111.destroy()

    num = int(round(R1N / 15) + 8 + round(R2N / 14.5 + 10) * 17 + round(PN / 30) * 357)
    top = num % 357

    numstriso = num.__str__()
    numstrtop = top.__str__()

    if num < 10:
        numstriso = "0" + numstriso

    if num < 100:
        numstriso = "0" + numstriso

    if num < 1000:
        numstriso = "0" + numstriso

    if top < 10:
        numstrtop = "0" + numstrtop

    if top < 100:
        numstrtop = "0" + numstrtop

    if top < 1000:
        numstrtop = "0" + numstrtop

    SCARA_Isoo = ImageTk.PhotoImage(
        Image.open('BLUUUP - Copy'
                   + '/ScaraRobot' + numstriso + '.png'))
    SCARA_Topo = ImageTk.PhotoImage(
        Image.open('BLUP - Copy - Copy'
                   + '/ScaraRobot' + numstrtop + '.png'))

    label112 = Label(canvas, image=SCARA_Isoo, bg="#777777")

    label112.place(relx=0.6153846154, rely=0, relheight=0.5, relwidth=0.3846153846)

    label113 = Label(canvas, image=SCARA_Topo, bg="#777777")

    label113.place(relx=0.6153846154, rely=0.5, relheight=0.5, relwidth=0.3846153846)

    n = np.array([T[0, 0], T[0, 1], T[0, 2]])
    s = np.array([T[1, 0], T[1, 1], T[1, 2]])
    a = np.array([T[2, 0], T[2, 1], T[2, 2]])
    d = np.array([T[0, 3], T[1, 3], T[2, 3]])
    ORX = np.array2string(n)
    ORY = np.array2string(s)
    ORZ = np.array2string(a)
    x = str(d[0])
    y = str(d[1])
    z = str(d[2])
    label9 = Label(frame9, text="X-coordinate = {} ".format(x))
    label10 = Label(frame10, text="Y-coordinate ={} ".format(y))
    label11 = Label(frame11, text="Z-coordinate = {}".format(z))

    label9.place(relwidth=1, relheight=1)
    label10.place(relwidth=1, relheight=1)
    label11.place(relwidth=1, relheight=1)

    label13 = Label(frame13, text="Orientation of the x-axis of the end-effector relative to the base ={}".format(ORX))
    label14 = Label(frame14, text="Orientation of the y-axis of the end-effector relative to the base ={}".format(ORY))
    label15 = Label(frame15, text="Orientation of the z-axis of the end-effector relative to the base ={}".format(ORZ))

    label13.place(relwidth=1, relheight=1)
    label14.place(relwidth=1, relheight=1)
    label15.place(relwidth=1, relheight=1)

    R1 = R1N
    R2 =R2N
    P = PN

    #entry1.delete(0,END)
    #entry2.delete(0,END)
    #entry3.delete(0,END)
    #entry4.delete(0,END)

## =======================> row 3 <=============================
frame7 = tk.Frame(root)
frame7.place(relwidth = 0.5384615385, relheight = 0.07 , relx= 0.038461538 , rely= 0.36)

button7  = Button(frame7,text = "Calculate Position and Orientation",bg = "#fff703",fg  = "black",command = calc)
button7.place(relwidth = 1 , relheight = 1)

## =======================> row 4 <=============================
frame8 = tk.Frame(root)
frame8.place(relwidth = 0.5384615385, relheight = 0.07 , relx= 0.038461538 , rely= 0.46)

label8 = Label(frame8, text=''' Postion of End-effector "in mm" ''', bg = "#3e96de")
label8.place(relwidth = 1,relheight = 1)

## =======================> row 6 <=============================
frame12 = tk.Frame(root)
frame12.place(relwidth = 0.5384615385, relheight = 0.07 , relx= 0.038461538, rely= 0.63)

label12 = Label(frame12, text=" Orientation of End-effector ", bg  = "#3e96de")
label12.place(relwidth = 1,relheight = 1)

## set menu for the team members
menu = Menu(root)
root.config(menu = menu)
submenu1 = Menu(menu)
subsub1 = Menu(submenu1)
subsub2 = Menu(submenu1)
subsub3 = Menu(submenu1)
subsub4 = Menu(submenu1)
subsub5 = Menu(submenu1)

menu.add_cascade(label = "Team members"        ,menu = submenu1)
submenu1.add_cascade(label = "Hossam Mohamed"  ,menu=  subsub1 )
submenu1.add_cascade(label = "Raghad Khaled"   ,menu=  subsub2 )
submenu1.add_cascade(label = "Taher Mohamed"   ,menu=  subsub3 )
submenu1.add_cascade(label = "Mostafa Wael"    ,menu=  subsub4 )
submenu1.add_cascade(label = "Nada El-Sayed"   ,menu=  subsub2 )

subsub1.add_cascade(label = "Section: 1   BN: 26" )
subsub2.add_cascade(label = "Section: 1   BN: 31" )
subsub3.add_cascade(label = "Section: 1   BN: 38" )
subsub4.add_cascade(label = "Section: 2   BN: 27" )
subsub5.add_cascade(label = "Section: 2   BN: 31" )

## insert the background image
image=ImageTk.PhotoImage(Image.open("Webp.net-resizeimage.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

## insert exit button
button4 = Button(root,text= "Exit The Program", command  = canvas.quit , bg= "black", fg = "white", height = 3)
button4.pack(fill = X)

root.mainloop()