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


def openproject():
    speak(" list of project that you like to open")
    a = int(input(''' 
    CG Foundation 1 - 1
    Virtual assistance kivi 2 - 2
    django template 3 - 3
    portfolio 4 - 4 
    random quotes generator react 5 - 5
    python face detection 6 - 6
    work for future 7 - 7
    upcoming project update soon '''))

    if a == 1:
        try:
            speak("project will opening")
            print("project will opening")
            codepath = "E:/New project CG/index.html"
            os.startfile(codepath)
        except Exception as e:
            print(e)
            speak("sorry some error occure try again.")
            print("sorry some error occure try again.")
            
    elif a == 2:
        try:
            speak("project will opening")
            print("project will opening")
            codepath = "C:/Users/Akash/Desktop/kivi"
            os.startfile(codepath)
        except Exception as e:
            print(e)
            speak("sorry some error occure try again.")
            print("sorry some error occure try again.")

    elif a == 3:
        try:
            speak("project will opening")
            print("project will opening")
            codepath = "C:/Users/Akash/projects/firstdjango"
            os.startfile(codepath)
        except Exception as e:
            print(e)
            speak("sorry some error occure try again.")
            print("sorry some error occure try again.")
            
    elif a == 4:
        try:
            speak("project will opening")
            print("project will opening")
            codepath = "C:/xampp/htdocs/first project/index.html"
            os.startfile(codepath)
        except Exception as e:
            print(e)
            speak("sorry some error occure try again.")
            print("sorry some error occure try again.")
            
            
    elif a == 5:
        try:
            speak("project will opening")
            print("project will opening")
            codepath = "C:/Users/Akash/firstreactjs/r1"
            os.startfile(codepath)
        except Exception as e:
            print(e)
            speak("sorry some error occure try again.")
            print("sorry some error occure try again.")
            
    elif a == 6:
        try:
            speak("project will opening")
            print("project will opening")
            codepath = "E:/python project/look-face.py"
            os.startfile(codepath)
        except Exception as e:
            print(e)
            speak("sorry some error occure try again.")
            print("sorry some error occure try again.")




    elif a == 7:
        try:
            speak("project will opening")
            print("project will opening")
            codepath = "C:\Users\Akash\projects\workforfuture"
            os.startfile(codepath)
        except Exception as e:
            print(e)
            speak("sorry some error occure try again.")
            print("sorry some error occure try again.")




