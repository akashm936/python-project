from posixpath import split
from turtle import update
import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep, strftime
import os
from datetime import timedelta
from datetime import datetime
from keyboard import press


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#for voice in voices:
#  print(voices,id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    # it takes microphone input an output in string
    #t = Translator()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-In')
        #translated = t.translate(query, dest='en')
        #text = translated()
        speak(f"you said: {query}\n")
        print(f"you said: {query}\n")
    except Exception as e:
        print(e)
        speak("say that again please.....")
        print("Say that again please....")
        return "None"
    return query

#-----------------------------------------------------------
#this section for get date and time for send message
#-----------------------------------------------------------

#strTime = int(datetime.now().strftime("%H"))
#update = int((datetime.now)+timedelta(minutes=2).strftime("%M"))
hour = int(datetime.now().hour)
minute = int(datetime.now().minute)

#-----------------------------------------------------------
#this section to list to those people to send message.
#-----------------------------------------------------------
def sendMessage():
    speak("who do you want to message")
    a = int(input(''' 
    send to all 0 - 0
    person 1 - 1
    person 2 - 2
    person 3 - 3
    person 4 - 4 
    person 5 - 5 
    person 7 - 7
    person 6 - 6'''))

    if a == 1:
        try:
            speak("whats the message")
            message = str(input("Enter the message"))
            pywhatkit.sendwhatmsg("+918956055703",message,hour,minute+2)
            press('enter')
            speak("message send successfully")
        except Exception as e:
            print(e)
            print("sorry message not send")
            speak("sorry message not send")

    elif a == 2:
        try:
            speak("whats the message")
            message = str(input("Enter the message"))
            pywhatkit.sendwhatmsg("+919359765355",message,hour,minute+2)
            press('enter')
        except Exception as e:
            print(e)
            print("sorry message not send")
            speak("sorry message not send")

    elif a == 3:
        try:
            speak("whats the message")
            message = str(input("Enter the message"))
            pywhatkit.sendwhatmsg("+919158043201",message,hour,minute+2)
            press('enter')
        except Exception as e:
            print(e)
            print("sorry message not send")
            speak("sorry message not send")

    elif a == 4:
        try:
            speak("whats the message")
            message = str(input("Enter the message"))
            pywhatkit.sendwhatmsg("91+634643663",message,hour,minute+2)
            press('enter')
        except Exception as e:
            print(e)
            print("sorry message not send")
            speak("sorry message not send")

    elif a == 5:
        try:
            speak("whats the message")
            message = str(input("Enter the message"))
            pywhatkit.sendwhatmsg("+9194668914634634940",message,hour,minute+2)
            press('enter')
        except Exception as e:
            print(e)
            print("sorry message not send")
            speak("sorry message not send")

    elif a == 6:
        try:
            speak("whats the message")
            message = str(input("Enter the message"))
            pywhatkit.sendwhatmsg("+9194366736346676804",message,hour,minute+2)
            press('enter')
        except Exception as e:
            print(e)
            print("sorry message not send")
            speak("sorry message not send")
    
    elif a == 7:
        try:
            speak("whats the message")
            message = str(input("Enter the message"))
            pywhatkit.sendwhatmsg("+9154345344363",message,hour,minute+2)
            press('enter')
        except Exception as e:
            print(e)
            print("sorry message not send")
            speak("sorry message not send")

    elif a == 0:
        try:
            speak("whats the message")
            message = str(input("Enter the message"))
            pywhatkit.sendwhatmsg("+918956055703",message,hour,minute+2)
            pywhatkit.sendwhatmsg("+919359765355",message,hour,minute+3)
            pywhatkit.sendwhatmsg("+919763070748",message,hour,minute+4)
            pywhatkit.sendwhatmsg("+919673676804",message,hour,minute+5)
            pywhatkit.sendwhatmsg("+918408063553",message,hour,minute+6)
            press('enter')
            speak("message send successfully")
        except Exception as e:
            print(e)
            print("sorry message not send")
            speak("sorry message not send")

#-----------------------------------------------------------
#this this end of program
#-----------------------------------------------------------