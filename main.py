from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
# browser = webdriver.Edge("C:/Users/dhariDownloads/PRO-C127-Student-Boilerplate-Code-main/PRO-C127-Student-Boilerplate-Code-main/edgedriver_win64/msedgedriver.exe")
# browser.get(START_URL)

# soup = BeautifulSoup(browser.page_source, "html.parser")
page=requests.get(START_URL)
soup=BeautifulSoup(page.text,'html.parser')
dwarf_table=soup.find_all('table',attrs={'class','wikitable sortable'})

dwarf=[]

table_rows=dwarf_table[1].find_all('tr')

for x in table_rows:
    td=x.find_all('td')
    row=[i.text.rstrip() for i in td]
    dwarf.append(row)
    
star_name=[]
mass=[]
radius=[]
distance=[]

for i in range(1,len(dwarf)):
    star_name.append(dwarf[i][0])
    mass.append(dwarf[i][7])
    radius.append(dwarf[i][8])
    distance.append(dwarf[i][5])
    
headers=['star_name','distance','mass','radius']

dwarf_df_1=pd.DataFrame(list(zip(star_name,mass,radius,distance)),columns=['star_name','mass','radius','distance'])

dwarf_df_1.to_csv('dwarf.csv',index=True,index_label='id')   