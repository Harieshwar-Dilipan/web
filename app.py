from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Edge("C:/Users/dhariDownloads/PRO-C127-Student-Boilerplate-Code-main/PRO-C127-Student-Boilerplate-Code-main/edgedriver_win64/msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data=[]

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table=soup.find('table',attrs={'class','wikitable'})
    table_body=bright_star_table.find('tbody')
    table_rows=table_body.find_all('tr')
    for rows in table_rows:
        table_cols=rows.find_all('td')
        temp_list=[]
        for col_data in table_cols:
            data=col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)