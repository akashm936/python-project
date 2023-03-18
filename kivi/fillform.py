from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import driver
import time

from Kivi import speak

while (10):
    
    web = webdriver.Chrome()
    web.get('https://forms.gle/RWDDuVtD1LeV1t3S8')
    time.sleep(5)

    email = "example123@gamil.com"
    cname = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
    cname.send_keys(email)


    sname = 'Entere your name...'
    name = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name.send_keys(sname)

    phoneno = '54542456444528387923116'
    phone = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    phone.send_keys(phoneno)

    sel_button = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[2]')
    sel_button.click()

    col_name = "Enter Your college here...."
    cname = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cname.send_keys(col_name)

    submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()


    speak("form successfully filled")
#web.close.window(False)
