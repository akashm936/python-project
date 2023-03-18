
from lib2to3.pgen2 import driver
import sys
import random
import time
from datetime import datetime
from datetime import date
from email import message
from email.mime import audio
from unittest import result
import speech_recognition as sr
import pyttsx3
import wikipedia
from bs4 import BeautifulSoup
from datetime import timedelta
import webbrowser
import os
import calendar
import smtplib
import pyautogui
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pywhatkit.core.exceptions import InternetException
from keyboard import press




#from googletrans import Translator

#-----------------------------------------------------------
#this section is used to select engine audio english aur hindi
#-----------------------------------------------------------

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#for voice in voices:
#  print(voices,id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#-----------------------------------------------------------
#this section is wish the time on startup
#-----------------------------------------------------------

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Akash sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Akash sir")

    else:
        speak("Good Evening Akash sir")

    speak("I am your personal Assistance kivi, I Can Help You sir")

#-----------------------------------------------------------
#this  section for taking audio command from user
#-----------------------------------------------------------
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
#this  section for send email the to client 
#-----------------------------------------------------------
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('akashbhau101@gmail.com', 'zhqroevofjnkhqmq')
    server.sendmail('', to, content)
    server.close()


def findDay(date):
    born = datetime.weekday()
    return (calendar.day_name[born])


#-----------------------------------------------------------
#this  is the main section of virtual assistance 
#-----------------------------------------------------------

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for exicuting task
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            print('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)


        elif 'youtube' in query:
            #speak("what are play on youtube")
            #query = query.replace("youtube.com", "")
            webbrowser.open("youtube.com")

#-----------------------------------------------------------
#this  section is selenium section for fill automatic form
#-----------------------------------------------------------

        elif 'check result' in query:
            try:
                web = webdriver.Chrome()
                web.get('https://student.dbatuapps.in/itxlogin')
                time.sleep(5)
                
                username = "T2121381242502"
                cname = web.find_element('xpath','/html/body/div[1]/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/input')
                cname.send_keys(username)

                password = '8956055703'
                phone = web.find_element('xpath','/html/body/div[1]/main/div/div/div/div/div[2]/div/div[1]/div/div[2]/input')
                phone.send_keys(password) 

                submit = web.find_element('xpath','/html/body/div[1]/main/div/div/div/div/div[2]/div/div[1]/input')
                submit.click()

                #web.close.window(False)
            except Exception as e:
                print(e)
                print("sorry task not found")
                speak("sorry task not found")

#-----------------------------------------------------------------------------------
#        https://forms.gle/A7hCaNyyTD3VWoKa9
        elif 'fill the form' in query:
            try:
                from fillform import web
                web = webdriver.Chrome()
            except Exception as e:
                print(e)
                speak("sorry form not fill")

#----------------------------------------------
#                     maintaince part end
#-------------------------------------------------------------------------------------------


        elif 'search' in query:
            try:
                web = webdriver.Chrome()
                web.get('https://www.youtube.com/')
                time.sleep(5)
                
                search = query
                cname = web.find_element('xpath','//*[@id="search"]')
                cname.send_keys(search)

                enter = web.find_element('xpath','//*[@id="search-icon-legacy"]/yt-icon')
                enter.click()
                #web.close.window(False)
            except Exception as e:
                print(e)
                print("sorry task not found")
                speak("sorry task not found")

        elif 'your name' in query:
            speak("my name is kivi, and work for akash")
            print("my name is kivi, and work for akash")
            speak("is there anything else you want to know")
            print("is there anything else you want to know")
#-----------------------------------------------------------
#this section is for send whatsapp message form whatsapp.py file
#-----------------------------------------------------------


        elif 'whatsapp' in query:
            from whatsapp import sendMessage
            sendMessage()


        elif 'open my project' in query:
            from project import openproject
            openproject()

        elif 'database' in query:
            try:
                speak("please run the xampp server")
                print("please run the xampp server")
                codepath = "C:/xampp/xampp-control.exe"
                os.startfile(codepath)
                speak("the database are opening")
                print("the database are opening")
                webbrowser.open("http://localhost/phpmyadmin/index.php?route=/database/structure&db=contact")
            
            except Exception as e:
                print(e)
                speak("sorry this command is in maintance please try later")
                print("sorry this command is in maintance please try later")
#-----------------------------------------------------------
#this section is used to search information on google
#-----------------------------------------------------------
            
        elif 'open google' in query:
            web = webdriver.Chrome()
            web.get('google.com')
            speak("what you like to search on google")
            web.maximize_window()
            time.sleep(10)
            if 'search' in query:
                try:
                    query = query.replace("search", "")
                    search = web.find_element('xpath','//*[@id="input"]')
                    search.send_keys(query)
                    press('enter')
                except Exception as e:
                    print(e)
                    speak("sorry this command is in maintance please try later")
        
        elif 'search' in query:
            web = webdriver.Chrome()
            web.get('youtube.com')
            speak("what you like to search on youtube")
            web.maximize_window()
            time.sleep(5)
            if 'search' in query:
                try:
                    search = web.find_element('xpath','//*[@id="search"]')
                    search.send_keys(query)
                    press('enter')
                    #web.startfile(3)
                except Exception as e:
                    print(e)
                    speak("sorry this command is in maintance please try later")
#-----------------------------------------------------------
#this section is used for open the url an play song
#-----------------------------------------------------------

        elif 'play song' in query:
            webbrowser.open("https://music.youtube.com/watch?v=X685cFmDzl0&list=RDAMVMX685cFmDzl0")

        elif 'open job website' in query:
            webbrowser.open("https://www.jobsgaar.com/")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chrome' in query:
            codepath = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            os.startfile(codepath)

        elif 'open university website' in query:
            webbrowser.open("https://student.dbatuapps.in/itxlogin")

        elif 'motivation' in query:
            webbrowser.open("https://www.youtube.com/watch?v=uTDMVdzIhqQs")

        elif 'energy' in query:
            webbrowser.open("https://www.youtube.com/watch?v=CBqdVosM4gU")

        elif 'my favourite song' in query:
            webbrowser.open("https://www.youtube.com/watch?v=fCdS-UShx4c")

        elif 'play music' in query:
            music_dir = 'E:/akashbhau.music'
            songs = os.listdir(music_dir)
            print(songs)
            d = random.randint(0,140)
            os.startfile(os.path.join(music_dir, songs[d]))

        elif 'play movie' in query:
            vidio_dir = 'E:/New folder'
            movie = os.listdir(vidio_dir)
            print(movie)
            d = random.randint(0,14)
            os.startfile(os.path.join(vidio_dir,movie[d]))

        elif 'play dj song' in query:
            webbrowser.open(
                "https://music.youtube.com/watch?v=CZt-rVn2BJs&list=RDCLAK5uy_lFuh0seSkGQjEEqrmTk7hs2OCMvx86nSo")

        elif 'play marathi dj song' in query:
            webbrowser.open(
                "https://music.youtube.com/watch?v=ZO_ZreML0ZY&list=RDAMVMs8iIlVT04OQ")

        elif 'play bollywood song' in query:
            webbrowser.open("https://music.youtube.com/watch?v=dfNdRsNSFx4")

        elif 'play motu patlu' in query:
            webbrowser.open("https://www.youtube.com/watch?v=W2P1jPZAZtU")
        
        elif 'play something' in query:
            webbrowser.open("https://www.youtube.com/watch?v=tZ99OoB_RNs&list=WL&index=80")
        
        elif 'saturday vibe' in query:
            webbrowser.open("https://www.youtube.com/watch?v=-6LHV9zl0Ig&list=RDGMEM6ijAnFTG9nX1G-kbWBUCJAVM-6LHV9zl0Ig&start_radio=1")

#-----------------------------------------------------------
#this section is used start application automatic
#-----------------------------------------------------------
        elif 'open python' in query:
            codepath = "C:/Program Files/JetBrains/PyCharm Community Edition 2021.2.3/bin/pycharm64.exe"
            os.startfile(codepath)

        elif 'open vs code' in query:
            codepath = "E:/ad inrealife/VSCode-win32-x64-1.64.2/code.exe"
            os.startfile(codepath)

        elif 'open chrome' in query:
            codepath = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            os.startfile(codepath)

        elif 'open opera' in query:
            codepath = "C:/Users/Akash/AppData/Local/Programs/Opera/launcher.exe"
            os.startfile(codepath)

#-----------------------------------------------------------
#this is section email jisko send karna hain unke naam
#-----------------------------------------------------------

        elif 'send email' in query:
            speak("who do you want to message")
            a  = int(input(''' 
            send to all 0 - 0
            Akash 1 - 1
            rutik 2 - 2
            gopal 3 - 3
            dhananjay 4 - 4 
            ak 5 - 5
            pappa 6 - 6'''))

    
            if a == 1:
                try:
                    speak("what should i say")
                    content = takeCommand()
                    to = "akashbhau101@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been send")
                    print("Email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry email was not send")

            elif a == 3:
                try:
                    speak("what should i say")
                    content = takeCommand()
                    to = "sablegopal03@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been send")
                    print("Email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry email was not send")

            elif a == 2:
                try:
                    speak("what should i say")
                    content = takeCommand()
                    to = "ruttikgaikwad@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been send")
                    print("Email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry email was not send")

            elif a == 4:
                try:
                    speak("what should i say")
                    content = takeCommand()
                    to = "dhananjaykale90055009@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been send")
                    print("Email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry email was not send")

            elif a == 5:
                try:
                    speak("what should i say")
                    content = takeCommand()
                    to = "amorwal5@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been send")
                    print("Email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry email was not send")

            elif a == 6:
                try:
                    speak("what should i say")
                    content = takeCommand()
                    to = ""
                    sendEmail(to, content)
                    speak("Email has been send")
                    print("Email has been send")
                except Exception as e:
                    print(e)
                    speak("sorry email was not send")

#-----------------------------------------------------------
#this section is to do list in python they remide you dealy task
#-----------------------------------------------------------

        elif 'work for' in query:
            try:
                speak("you have to do these 3 things.....")

                speak("you have to go for morning walk at 6 am")

                speak("Then you have to go to college from 9 am to 6 pm")
            except Exception as e:
                print(e)
                speak("You don't have any work today.")
                print("You don't have any work today.")

#-----------------------------------------------------------
#this is schedule section your import task is here.
#-----------------------------------------------------------

        elif 'lecture' in query:
            try:
                speak("Today your LH is from 10:15 am to 11:15 am")

                speak(
                    "then there is your of software engineering lecture 11:15 AM to 12:15 PM")

                speak("Then, you have a lab of DBMS.")

            except Exception as e:
                print(e)
                speak("you don't have any lectures today")
                print("you don't have any lectures today")

#-----------------------------------------------------------
#this date section which date is on today
#-----------------------------------------------------------

        elif 'today' in query:
            try:
                today = date.today()
                speak(today.strftime(" Today is %A" ))
                print(today.strftime(" Today is %A"))
                #speak(findDay(date))
                #print(today)
                #print(findDay(date))
            except Exception as e:
                print(e)
                print("not found date")
                speak("not found")
        
        elif 'tomorrow' in query:
            try:
                tomorrow = timedelta(1)
                speak(tomorrow.strftime(" tomorrow is %A"))
                print(tomorrow.strftime(" tomorrow %A"))
                #speak(findDay(date))
                #print(today)
                #print(findDay(date))
            except Exception as e:
                print(e)
                print("not found date")
                speak("not found")

#-----------------------------------------------------------
#this exit section for close virtual assistance
#-----------------------------------------------------------

        elif 'stop' in query :
            speak("Ok! by Akash ")
            sys.exit()

        elif 'hello' in query:
            speak("Hello how are you, do you need some help from me?")
            print("Hello how are you, do you need some help from me?")
            speak("list of command that you like run")
            print('''
            1 say hello
            2 send email
            3 send whatsapp message
            4 play music
            5 check result
            6 fill automatic form
            7 open application
            8 open google
            9 what day today
            ''')

#-----------------------------------------------------------
#this is the end of program 
# owner : Akash Ashok Morwal
# email : amorwal5@gmail.com
# mobile : +91 8956055703
# follow me on social media
#-----------------------------------------------------------
