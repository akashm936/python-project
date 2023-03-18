#current_dateTime = datetime.now()
def time(now,hour,minute):
    now = datetime.now()
    hour = int(datetime.now().hour)
    minute = int(datetime.now().minute)

    if 'send message to Akash' in query:
        try:
            speak("whats the message")
            message = takeCommand()
            now = datetime.now()
            hour = int(datetime.now().hour)
            minute = int(datetime.now().minute)
            pywhatkit.sendwhatmsg("+91 8956055703", message,hour, minute+2)
            speak("massege was send successfully!")
    except Exception as e:
            print(e)
            print("sorry was message not send")
            speak("sorry was message not send")

#========================================================
def whatsapp(number,message):
    numb = '+91' + int(number)
    mess = message
    open_chat = "https://web.whatsapp.com/send?photos=" + numb + "&text" + mess
    webbrowser.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')


#---------------------------------------------------
        elif 'send message' in query:
            query = query.replace("send","")
            query = query.replace("message","")
            query = query.replace("to","")
            name = query

            if 'Akash' in name:
                numb = "8956055703"
                speak(f"what the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)
            
            elif 'hrithik' in name:
                numb = "8956055703"
                speak(f"what the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp(numb,mess)

            elif 'akm' in name:
                gro = "EyZN4b18O5B074HlNwgBW1"
                speak(f"whats the message for {name}")
                mess = takeCommand()
                whatsapp.whatsapp_Grp(gro,mess)
