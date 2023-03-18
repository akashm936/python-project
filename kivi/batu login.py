from selenium import webdriver
import time


web = webdriver.Chrome()
web.get('https://student.dbatuapps.in/itxlogin')
web.maximize_window()
time.sleep(10)


username = "T212138d56878451242502"
cname = web.find_element('xpath','/html/body/div[1]/main/div/div/div/div/div[2]/div/div[1]/div/div[1]/input')
cname.send_keys(username)


password = '892343565660555645703'
phone = web.find_element('xpath','/html/body/div[1]/main/div/div/div/div/div[2]/div/div[1]/div/div[2]/input')
phone.send_keys(password)

submit = web.find_element('xpath','/html/body/div[1]/main/div/div/div/div/div[2]/div/div[1]/input')
submit.click()


