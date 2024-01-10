#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

print('wait...')

service = webdriver.ChromeService(executable_path= r'/home/.../chromedriver') # path to chromedriver executable
driver = webdriver.Chrome(service = service)

email = ''
password = ''

login_url = f'https://play.316ctf.com/login'
driver.get(login_url)
driver.find_element(By.NAME,'name').send_keys(email)
driver.find_element(By.NAME,'password').send_keys(password)
driver.find_element(By.NAME, "_submit").click()

def open_file(file_path):
	with open(file_path,'r') as fp:
		possible_passwords = fp.readlines()
	return possible_passwords

file_path = r'/home/.../dictionary-list.txt' # path to dictionary list
possible_passwords = open_file(file_path)

def start_page():
	challenge_url = 'https://play.316ctf.com/challenges#Huntsville%20#1-121'
	driver.get(challenge_url)
	delay = 3 #seconds
	try:
		myElem = WebDriverWait(driver,delay).until(EC.presence_of_element_located((By.ID, 'challenge-input')))
	except TimeoutException:
		print('page took too long')

start_page()

for password in possible_passwords:
	possible_answer = password
	driver.find_element(By.ID, 'challenge-input').send_keys(possible_answer)
	driver.find_element(By.ID, 'challenge-submit').click()
	time.sleep(0.9)
	result = driver.find_element(By.ID, 'result-message').text
	if result == 'correct':
		print(f'GOT IT: {password}')
		break
	elif result == "You're submitting flags too fast. Slow down.":
		print(f'too fast: {password}')
		driver.refresh()
		start_page()
		time.sleep(5)
	else:
		print(f'WRONG: {password}')
	answer_field = driver.find_element(By.ID, 'challenge-input')
	answer_field.clear()
	time.sleep(1)
