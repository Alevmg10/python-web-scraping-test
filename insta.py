from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from lxml import html
import time

browser = webdriver.Chrome()

USERNAME = "alevmg_"
PASSWORD = "Trivium.2021"

def instagram_loggin():
    
        try:
            username = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
            password = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.NAME, "password")))

            #ingrese  username and password
            username.clear()
            username.send_keys(USERNAME)
            password.clear()
            password.send_keys(PASSWORD)

            button = WebDriverWait(browser, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
            button.click()

        except:
            pass


def instagram_scraper(url):
    browser.get(url)
    instagram_loggin()
    
    comment_lst = []
    user_lst = []

    try:
        time.sleep(5)
        comment_elements = browser.find_elements(By.CLASS_NAME, '_a9zs')
        user_elements = browser.find_elements(By.CLASS_NAME, '_a9zc')
        
    except Exception as e:  
        print(f"ERROR - No se puede obtener comentarios  {e}")
    
    for users in user_elements:
        user_lst.append(users.text)
    for comments in comment_elements:
        comment_lst.append(comments.text)

    
    dict = {'User ID': user_lst, 'Comment': comment_lst}
    df = pd.DataFrame(dict)
    df.to_csv("instagram.csv", sep=";", index=False)    

instagram_scraper("https://www.instagram.com/p/Cj8rwflMpo8/")