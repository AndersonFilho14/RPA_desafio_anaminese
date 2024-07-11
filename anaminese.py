from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
#Para o selenium usar o teclado
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Esperar
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)

browser.get('https://www.jotform.com/form/241925512525656')

# Nome e sobrenome 
browser.find_element(By.ID,'first_3').send_keys('Anderson')
browser.find_element(By.ID,'last_3').send_keys('Filho')
#nascimento
browser.find_element(By.XPATH,'//*[@id="lite_mode_4"]').send_keys('7212003')
#email
browser.find_element(By.ID,'input_5').send_keys('anderson@anderson.br')
browser.save_screenshot('prova01.png')
#idade
browser.find_element(By.ID,'input_7').send_keys('20')
#Altura
browser.find_element(By.ID,'input_8').send_keys('1.80')
#Profissão
browser.find_element(By.ID,'input_9').send_keys('Dev')

browser.save_screenshot('prova02.png')    