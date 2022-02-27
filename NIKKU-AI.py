#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
# geektechstuff bluetooth

import speech_recognition as sr
from time import ctime
import time
import bluetooth
from bluetooth.main import list_devices, remove_device, pair_device
import os
from gtts import gTTS
import pyttsx3
from wstring import Wstring
from pyttsx3 import speak
from pyttsx3 import engine
import subprocess as sp
import psutil
from win10toast import ToastNotifier
import threading
import pyautogui
import webbrowser as wb
import random


toaster = ToastNotifier()




paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'music1': "C:\\Users\\hp\\OneDrive\\Desktop\\Music\\yt1s.com - Doctor Strange Believer.mp3",
    'music2' : "C:\\Users\\hp\\OneDrive\\Desktop\\Music\\yt1s.com - La Casa De Papel Bella Ciao Lyrics Money Heist.mp3",
    'music3' : "C:\\Users\\hp\\OneDrive\\Desktop\\Music\\yt1s.com - Marakkar Theme Music By Rahul Raj  Mohanlal  Priyadarshan  Saina Music.mp3",
    'music4' : "C:\\Users\\hp\\OneDrive\\Desktop\\Music\\yt1s.com - Pokemon Ash Greninja AMV Overkill.mp3",
    'music5' : "C:\\Users\\hp\\OneDrive\\Desktop\\Music\\yt1s.com - Captain Jack Sparrow theme music.mp3",
    'parrot_os' : "C:\\Users\\hp\\OneDrive\\Desktop\\parrot security.lnk",
    'kali_linux' : "C:\\Users\\hp\\OneDrive\\Desktop\\dragoni linux.lnk",
    'web' : "E:\\Website\\index.html",
    'gro' : "C:\Program Files\WindowsApps\Groove.exe",
    'incredible_hulk' : "C:\\Users\\hp\\OneDrive\\Desktop\\ALL MOVIE FROM 2021\\Incradeble hulk.mkv",
    'capten' : "C:\\Users\\hp\\OneDrive\\Desktop\\ALL MOVIE FROM 2021\\Capten America 2.mkv",
    'cap1' : "C:\\Users\\hp\\OneDrive\\Desktop\\ALL MOVIE FROM 2021\\Capten America the first avanger.mkv"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def Groove():
    sp.run('start microsoft.window.groove:', shell=True)

def website():
    os.startfile(paths['web'])

def hulk():
    os.startfile(paths['incredible_hulk'])

def cap():
    os.startfile(paths['capten'])

def cap11():
    os.startfile(paths['cap1'])

def musicc1():
    os.startfile(paths['music1'])

def music2():
    os.startfile(paths['music2'])

def marakkar():
    os.startfile(paths['music3'])

def verkill():
    os.startfile(paths['music4'])

def jack():
    os.startfile(paths['music5'])

def parrot():
    os.startfile(paths['parrot_os'])


def kali():
    os.startfile(paths['kali_linux'])

def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])


#ACTIVATION USERNAME
speak("enter username to start")
a = input("user name>>")
if "Admin"  in a:
    speak("welcome sir")
    Wstring("Welcome to Nicto", length=6, height=6, symbol='#', color='white')
    time.sleep(1)
    cmd = 'color c'
    cmd2 = 'dir/s'
    os.system(cmd)
    os.system(cmd2)

else:
    speak("do you want to create a temporary user account")
    b =input("invalid username >> do you want to create a temporary user account")

    if "yes" in b:
        b = input("new user id >>")
        with open('log.txt', 'w') as f:
            f.write(b)
        speak("welcome " + b)
        Wstring("Welcome" +b , length=5, height=5, symbol='#', color='white')
        print("welcome "+b)
    else:
        exit()

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("NCP UNDER CONTROL..")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        speak("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speak("Could not request results from Google Speech Recognition service")

    return data

# THE RESPONCE PART OF NICTO
def jarvis(data):

    if "how are you" in data:
        speak("I am fine sir")

    if "hello" in data:
        speak("hallo sir")
    if "hallo" in data:
        speak("hallo sir")

    if "Nikku" in data:
        speak("yes sir")

    if "open camera" in data:
        speak("ok sir")
        open_camera()

    if "give me a break" in data:
        speak("as you wish")

    if "can you open Discord" in data:
        speak("why not sir")
        open_discord()

    if "start hacking proccess" in data:
        open_cmd()
        cmd= 'ls'
        cmd2 = 'echo "start hacking sir" '

    if "open parrot" in data:
        speak("understanted the secret code ")
        parrot()

    if "hay man" in data:
        speak("hallo")

    if "movie time" in data:
        speak("ok which movie do you want")
        if "Hulk" in data:
            hulk()
        elif "capten america two" in data:
            cap()
        elif "capten america first avenger" in data:
            cap11()

    if "tell me a joke" in data:
        speak("what is best thing about switzerland ? ")
        speak("the flag is a big plus")
        if "not funny" in data:
            speak("What does a ghost say on January 1st")
            speak("happy boo year")
        if "good" in data:
            speak("thankyou sir ")

    if "boot kali" in data:
        speak("kali linux under booting sir")
        kali()

    if "ckeck emails" in data:
        speak("checking your mails ......... hmm you are all set sir")
        wb.register('chrome', None)
        wb.open('https://mail.google.com/mail/u/0/#inbox')
        True

    if "play music" in data:
        speak("ok sir")
        musicc1()

    elif "it's too hard" in data:
        speak("how about this")
        marakkar()

    elif "insiring song" in data:
        speak("ok how about it")
        verkill()

    elif "spanish song" in data:
        speak("ok i have a plan")
        music2()

    elif "a nice BGM" in data:
        speak("how about it")
        jack()

    elif "random song" in data:
        path = "C:\\Users\\hp\\OneDrive\\Desktop\\Music"
        files = os.listdir(path)
        d = random.choice(files)
        os.startfile(d)

    if "self scan" in data:
        speak("checking errors in me please wait")

    if "open youtube" in data:
        speak("ok dont watch youtube so much . you need to complete programming project")
        wb.register('chrome', None)
        wb.open('https://www.youtube.com')
        True

    if "volume down" in data:
        pyautogui.press("volumedown")

    if "volume up" in data:
        pyautogui.press("volumeup")

    if "mute" in data:
        pyautogui.press("volumemute")

    if "give me full control" in data:
        speak("ok sir mannual commant activated ")
        cmd='ls'

    if "you are a fool" in data:
        speak("i am listening . i think it is not funny at all")

    if "are you ready" in data:
        speak("always sir ")

    if "open our website" in data:
        speak("ok sir")
        website()

    if "tell about you" in data:
        speak("THis is nicto at short you can call me nikku and iam made by python so i have limitation")

    if "my friends are here" in data:
        speak("they are your friends not mine ")



    if "security" in data:
        speak("ok sir systems near you are ...")
        list()

    if "check security" in data:
        speak("sorry sir the defence nikku is broken you just made me i dont get security incharge it is your responsibility")

    if "whats time" in data:
        speak(ctime())

    if "exit" in data:
        speak("ok i need rest")
        exit()

    if "where am i" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on sir, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    if "emergency" in data:
        speak("ok sir emergency meatures are been taken your system will SHUTDOWN...")
        speak("your varification needed")
        ab = input("USERNAME :")
        bc = input ("PASSWORD :")
        if "Akshai2006" in ab:
            if "110011" in bc:
                speak("varification sucsess")
                exit()


# initialization
time.sleep(2)
speak(ctime()+" now sir  what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)

#username is Admin