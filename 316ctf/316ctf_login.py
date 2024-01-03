#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup

print('wait...logging you in')

service = webdriver.ChromeService(executable_path= r'/home/.../chromedriver') # path to chrome driver
driver = webdriver.Chrome(service = service)

email = '' # enter your email
password = '' # enter your password

login_url = f'https://play.316ctf.com/login'
driver.get(login_url)
driver.find_element(By.NAME,'name').send_keys(email)
driver.find_element(By.NAME,'password').send_keys(password)

driver.find_element(By.NAME, "_submit").click()
