import serial
from tkinter import *
import tkinter as tk 

commPort = '/dev/cu.usbmodem14101'
ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)

def turnOnLED():
    ser.write(b'o')
    if blinkState.get() == 1:
        blinkLED()

def turnOffLED(): 
    ser.write(b'x')

def blinkLED():
    if blinkState.get() == 1:
        ser.write(b'b')
        
# creating tkinter window 
root = Tk() 
root.title('Blink GUI')

btn_On = tk.Button(root, text="Turn On", command=turnOnLED)
btn_On.grid(row=0, column=0)

btn_Off = tk.Button(root, text="Turn Off", command=turnOffLED)
btn_Off.grid(row=0, column=1)

blinkState = IntVar()
chkBtn_Blink = tk.Checkbutton(root, text = "Blink",variable = blinkState, command = blinkLED)
chkBtn_Blink.grid(row=0, column = 2)

root.geometry("350x350")
root.mainloop()
