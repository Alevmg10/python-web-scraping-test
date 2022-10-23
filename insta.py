from os import environ
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
USERNAME = "su nombre usuario"
PASSWORD = "su contraseña"

delimiter = environ.get("CSV_DELIMITER")
id_variable=environ.get("INSTA_ID_CLASE")
comentario_variable=environ.get("INSTA_COMENTARIO_CLASE")

def instagram_loggin():
    #funcion para el inicio de sesion (si es necesario)
    try:
        username = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.NAME, "username"))
        )
        password = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.NAME, "password"))
        )

        # ingrese  usuario y contraseña
        username.clear()
        username.send_keys(USERNAME)
        password.clear()
        password.send_keys(PASSWORD)

        button = WebDriverWait(browser, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        button.click()

    except:
        pass

def instagram_scraper(url):
    
    print("Iniciando scraper de Instagram")
    browser.get(url)
    instagram_loggin()

    comment_lst = []
    user_lst = []

    #obtener los elementos de la pagina que vamos a usar para el scraper
    try:
        time.sleep(5)
        comment_elements=browser.find_elements(By.CLASS_NAME, comentario_variable)
        user_elements=browser.find_elements(By.CLASS_NAME, id_variable)

    except Exception as e:
        print(f"ERROR - No se puede obtener comentarios  {e}")

    for users in user_elements:
        user_lst.append(users.text)

    for comments in comment_elements:
        comment_lst.append(comments.text)

    # guardar en archivo csv
    dict = {"User ID": user_lst, "Comment": comment_lst}
    df = pd.DataFrame(dict)
    df.to_csv("instagram.csv", sep=delimiter, index=False)
    print("Scraper finalizado")


instagram_scraper("https://www.instagram.com/p/Cj8rwflMpo8/")