import serial
from tkinter import *
import tkinter as tk
import time

commPort = '/dev/cu.usbmodem14401'

ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)

def turnOnLED():
    if blinkState.get() == 1:
        blinkLED()
    else:
        ser.write(b'o')
        
def turnOffLED(): 
    ser.write(b'x')

def blinkLED():
    if blinkState.get() == 1:
        ser.write(b'b')
        time.sleep(1)
        delay = userDelay.get()
        numBlinks = entryBlink.get()
        dataToSend = delay + '-' + numBlinks
        ser.write(dataToSend.encode())
    
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

blinkTime = ['50','100','200','400','600','800','1000','1200']
userDelay = StringVar()
delayMenu = tk.OptionMenu(root,userDelay,*blinkTime)
userDelay.set('800')
delayLabel = tk.Label(root,text="Blink (ms)")
delayLabel.grid(row=1,column=0)
delayMenu.grid(row=1,column=1)

entryBlink = Entry(root,width=3)
entryBlink.insert(0,"5")
entryBlinkLabel = tk.Label(root,text="Num Blinks")
entryBlinkLabel.grid(row=2,column =0)
entryBlink.grid(row=2,column = 1)

root.geometry("350x350")
root.mainloop()
