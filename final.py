from tkinter import *
from tkinter.messagebox import showinfo
from gpiozero import MotionSensor, LED, Button
import time
import _thread
import pygame
from signal import pause

a = 0
alarmMode = 1


def looptest():
    global a
    print('aan trigger')
    gled = LED(17)
    sense = MotionSensor(4)
    counter = 0
    time.sleep(10)
    while a:
        gled.on()
        x = sense.is_active
        time.sleep(0.3)
        if x:
            counter += 1
        if counter > 3:
            print('Zeker een inbreker')
            time.sleep(10)
            alarm()
        if not x:
            counter = 0

def alarm():
    global a
    global alarmMode
    rled = LED(16)
    pygame.mixer.init()
    pygame.init()
    sounda= pygame.mixer.Sound("/home/pi/Geluid.wav")
    if a:
        sounda.play()
    if alarmMode == 1:
        while a:
            rled.on()
            time.sleep(1)
            rled.off()
            time.sleep(1)
    elif alarmMode == 2:
        while a:
            rled.on()
            time.sleep(0.5)
            rled.off()
            time.sleep(0.5)

def loginFrame():
    def login():
        username = usernameEntry.get()
        password = passwordEntry.get()
        print(username)
        print(password)
        if username == "" and password == '':
            removeLoginFrame()
            mainFrame()

    def removeLoginFrame():
        usernameLabel.grid_remove()
        usernameEntry.grid_remove()
        passwordLabel.grid_remove()
        passwordEntry.grid_remove()
        loginButton.grid_remove()

    usernameLabel = Label(master=root, text='Username: ', height=1)
    usernameLabel.grid(row=0, column=0, pady=4)
    usernameEntry = Entry(master=root)
    usernameEntry.grid(row=0, column=1, pady=4)
    passwordLabel = Label(master=root, text='Password: ', height=1)
    passwordLabel.grid(row=1, column=0, pady=4)
    passwordEntry = Entry(master=root, show='*')
    passwordEntry.grid(row=1, column=1, pady=4)
    loginButton = Button(master=root, text='Login', command=login)
    loginButton.grid(row=2, column=1, pady='4')

def mainFrame():

    def alarmToggle():
        global a
        if statusLabel2["text"] == 'Uit':
            statusLabel2["text"] = 'Aan'
            bericht = 'Na het sluiten van dit venster start de uitlooptimer. Na 10 seconden is het alarm actief.'
            showinfo(title='popup', message=bericht)
            a = 1
            _thread.start_new_thread(looptest,())
        else:
            statusLabel2["text"] = 'Uit'
            a = 0

    def modeToggle():
        global alarmMode
        if modusLabel2["text"] == 'Langzaam knipperen':
            alarmMode = 2
            modusLabel2["text"] = 'Snel Knipperen'
        else:
            alarmMode = 1
            modusLabel2["text"] = 'Langzaam knipperen'


    statusLabel = Label(master=root, text='Alarm status: ', height=1)
    statusLabel.grid(row=0, column=0, pady=4)
    statusLabel2 = Label(master=root, text='Uit', height=1)
    statusLabel2.grid(row=0, column=2, pady=4)
    statusButton = Button(master=root, text='Aan / Uitzetten', command=alarmToggle)
    statusButton.grid(row=1, column=0, pady='4')
    modusLabel = Label(master=root, text='Alarm modus: ', height=1)
    modusLabel.grid(row=2, column=0, pady=4)
    modusLabel2 = Label(master=root, text='Langzaam knipperen', height=1)
    modusLabel2.grid(row=2, column=2, pady=4)
    loginButton = Button(master=root, text='Kies modus', command=modeToggle)
    loginButton.grid(row=3, column=0, pady='4')

def startInterface():
    loginFrame()
    root.mainloop()

root = Tk()

startInterface()

