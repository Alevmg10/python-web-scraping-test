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
import os
from os import environ

browser = webdriver.Chrome()
delimiter = environ.get("CSV_DELIMITER")
clase_variable=environ.get("FACEBOOK_COMENTARIO_CLASE")


def facebook_scraper(url):
    print("Iniciando scraper de Facebook")
    browser.get(url)
    comment_lst = []
    user_lst = []

    #obtener los elementos de la pagina que vamos a usar para el scraper
    try:
        time.sleep(5)
        comment_elements = browser.find_elements(By.CLASS_NAME, clase_variable)
        
    except Exception as e:  
        print(f"ERROR - No se puede obtener comentarios  {e}")
    
    for comments in comment_elements:
        coment_n_name = comments.text
        list_all = coment_n_name.split("\n")
        comment_lst.append(list_all[1])
        user_lst.append(list_all[0])

    # guardar en archivo csv
    dict = {'User ID': user_lst, 'Comment': comment_lst}
    df = pd.DataFrame(dict)
    df.to_csv("facebook.csv", sep=delimiter, index=False)
    print('Scraper finalizado')

facebook_scraper("https://m.facebook.com/ign/posts/pfbid02RZTpZ7rVpqAuK6CWaDxgcEQimBYfoEiXFNA1yDFm7S79WZJLsEzbdb2cptp92vx5l")