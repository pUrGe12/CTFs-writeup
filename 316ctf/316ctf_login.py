#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup

print('wait...logging you in')

service = webdriver.ChromeService(executable_path= r'/home/purge0218/Desktop/chromedriver/chromedriver')
driver = webdriver.Chrome(service = service)

email = 'helloitsme0218@gmail.com'
password = 'Football@5'

login_url = f'https://play.316ctf.com/login'
driver.get(login_url)
driver.find_element(By.NAME,'name').send_keys(email)
driver.find_element(By.NAME,'password').send_keys(password)

driver.find_element(By.NAME, "_submit").click()

print('starting brute-forcing the flags')

i = 9
url = f'https://play.316ctf.com/challenges#Huntsville%20#{i}-12{i}'
driver.get(url)
