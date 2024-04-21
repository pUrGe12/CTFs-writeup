#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup

print('wait...logging you in')

service = webdriver.ChromeService(executable_path= r'/home/purge0218/Desktop/chromedriver/chromedriver')
driver = webdriver.Chrome(service = service)

email = ''
password = ''

login_url = f'https://play.316ctf.com/login'
driver.get(login_url)
driver.find_element(By.NAME,'name').send_keys(email)
driver.find_element(By.NAME,'password').send_keys(password)

driver.find_element(By.NAME, "_submit").click()

print('starting brute-forcing the flags')

fp = open(r'C:\Users\hello\OneDrive\Desktop\dictionary-list.txt', 'r')
pass_list = fp.readlines()

url = f'https://play.316ctf.com/challenges#Huntsville%20#{i}-12{i}'
driver.get(url)
driver.find_element(By.NAME, 'answer').send_keys(pass_list[j])
driver.find_element(By.CLASS, "challenge-submit btn btn-md btn-outline-secondary float-right").click()


