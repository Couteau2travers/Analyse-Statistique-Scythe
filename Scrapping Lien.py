#import requests
#from bs4 import BeautifulSoup

#reponse = requests.get('https://boardgamearena.com/gamepanel?game=scythe')
#print(reponse)

#soup = BeautifulSoup(reponse.content, "html.parser")
#soup.prettify

#print('test')

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import os
import shutil
import random as rd

time_debut = time.time()

#print("SCRIPT EXECUTÉ :", os.path.abspath(__file__))

# Lance Chrome automatiquement avec le bon driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Ouvre la page BGA
driver.get("https://boardgamearena.com/gamepanel?game=scythe")

time.sleep(3)  # Laisse le temps à la page de charger les scripts

try:
    refuse_button = driver.find_element(By.CSS_SELECTOR, ".cc-btn.cc-deny")
    refuse_button.click()
    print("Cookies refusés.")
    time.sleep(1)
except:
    print("Pas de bannière cookies détectée.")


elements = driver.find_elements(By.CSS_SELECTOR, "div.bga-link")
y = 0

print(elements)


played_games = None
for el in elements:
    raw_text = el.text
    clean_text = "".join(filter(str.isdigit, raw_text))
    if clean_text and int(clean_text) > 1000:
        played_games = int(clean_text)
        clique = el
        break
    y+=1

print("Nombre de parties jouées :", played_games)
#print(clique)

r_text = elements[y].text
c_text = "".join(filter(str.isdigit, r_text))
print(int(c_text))

try:
    #nbr_party = driver.find_element(By.XPATH, clique)
    #nbr_party.click()
    clique.click()
    print("ouverture partie")
except : 
    print("j ai pas reussi je suis nul")

time.sleep(4)

element_voir_plus = driver.find_element(By.ID, "board_seemore__") 

for i in range(1000):
        element_voir_plus.click()
        time.sleep(1)
    
elements2 = driver.find_elements(By.TAG_NAME, "a")
lien = []

for el in elements2:
    url = el.get_attribute("href")
    if url is not None:
        if "table?table" in url :
            lien.append(el.get_attribute("href"))

#print(elements2)
#print(lien)
#print(len(lien))

donnees = [["Lien partie"], ["Numéro de la table"]]

for el in lien:
    if el :
        tableID = el.split("=")[-1]
        donnees.append([el, tableID])

#print(donnees)

LienScythe = f"lien_scythe_5000.csv"

#dossier_script = 'C:\Users\arthu\OneDrive\Bureau\Programmation\Python\Scrapping\Nouveau dossier'
#chemin_fichier = os.path.join(dossier_script, "lien_scythe.csv")

#print(chemin_fichier)

with open(LienScythe, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(donnees)

destination = "C:/Users/arthu/OneDrive/Bureau/Programmation/Python/Scrapping/BGA - Scythe"
shutil.move(LienScythe, destination)

driver.quit()

time_fin = time.time()

print(time_fin - time_debut)

