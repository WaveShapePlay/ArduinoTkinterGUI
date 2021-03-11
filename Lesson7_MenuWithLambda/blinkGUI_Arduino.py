import serial
from tkinter import *
import tkinter as tk
from tkinter import messagebox
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
        userInputVaild = userDataCheck(numBlinks)
        if userInputVaild == True:
            dataToSend = delay + '-' + numBlinks
            ser.write(dataToSend.encode())

def userDataCheck(userInput):
    try:
        int(userInput)
        return True
    except:
        messagebox.showerror("Error", "Please enter a valid integer", icon = 'error')
        return False

def menuBlinkEnable():
    if blinkState.get() != 1:
        blinkState.set(1)
    blinkLED()

def menuDelaySelect(index):
    if blinkState.get() == 0:
        blinkState.set(1)
    userDelay.set(blinkTime[index])

def menuTurnOn():
    if blinkState.get() == 1:
        blinkState.set(0)
    ser.write(b'o')

def menuTurnOff():
    if blinkState.get() == 1:
        blinkState.set(0)
    ser.write(b'x')

def menuSave():
    print("Selected Save")

def exitGUI():
    root.destroy()
    
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

menuBar = Menu(root)

fileMenu = Menu(menuBar,tearoff = 0)
menuBar.add_cascade(label ='File', menu = fileMenu)  
fileMenu.add_command(label ='Save', command = menuSave)
fileMenu.add_command(label ='Exit', command = exitGUI)

settings = Menu(menuBar, tearoff = 0)
menuBar.add_cascade(label ='Settings', menu = settings) 
settings.add_command(label ='Blink', command = menuBlinkEnable) 
settings.add_command(label ='Turn On', command = menuTurnOn)
settings.add_command(label ='Turn Off', command = menuTurnOff)

delaySubMenu = Menu(settings, tearoff = 0)
settings.add_cascade(label ='Delay', menu = delaySubMenu)
for i in range(0,len(blinkTime)):
    delaySubMenu.add_command(label = blinkTime[i], command = (lambda i=i : menuDelaySelect(i)))

root.config(menu = menuBar)
root.geometry("350x350")
root.mainloop()
