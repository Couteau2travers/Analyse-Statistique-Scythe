from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import shutil


time_debut_general = time.time()

y=1

Data_base = f"Data_base2.csv"
DB_abandonée = f'Partie_Abandonné2.csv'

data_base_python = [
    "Lien partie", "Numéro Partie", "Nbr de joueurs",

    # Position de départ
    "J1 Position départ", "J2 Position départ", "J3 Position départ", "J4 Position départ", "J5 Position départ",

    # Factions
    "J1 Faction", "J2 Faction", "J3 Faction", "J4 Faction", "J5 Faction",

    # Mat (joueur mat)
    "J1 Mat", "J2 Mat", "J3 Mat", "J4 Mat", "J5 Mat",

    # Score final
    "J1 Score final", "J2 Score final", "J3 Score final", "J4 Score final", "J5 Score final",

    # Points provenant des étoiles
    "J1 Pts étoiles", "J2 Pts étoiles", "J3 Pts étoiles", "J4 Pts étoiles", "J5 Pts étoiles",

    # Points provenant des territoires
    "J1 Pts territoires", "J2 Pts territoires", "J3 Pts territoires", "J4 Pts territoires", "J5 Pts territoires",

    # Points provenant des ressources
    "J1 Pts ressources", "J2 Pts ressources", "J3 Pts ressources", "J4 Pts ressources", "J5 Pts ressources",

    # Points provenant de la tuile bonus
    "J1 Pts tuile bonus", "J2 Pts tuile bonus", "J3 Pts tuile bonus", "J4 Pts tuile bonus", "J5 Pts tuile bonus",

    # Points provenant des pièces
    "J1 Pts pièces", "J2 Pts pièces", "J3 Pts pièces", "J4 Pts pièces", "J5 Pts pièces",

    # Niveau population
    "J1 Niveau pop", "J2 Niveau pop", "J3 Niveau pop", "J4 Niveau pop", "J5 Niveau pop",

    # Territoires contrôlés
    "J1 Territoires contrôlés", "J2 Territoires contrôlés", "J3 Territoires contrôlés",
    "J4 Territoires contrôlés", "J5 Territoires contrôlés",

    # Ressources restantes
    "J1 Ressources restantes", "J2 Ressources restantes", "J3 Ressources restantes",
    "J4 Ressources restantes", "J5 Ressources restantes",

    # Étoiles gagnées (total)
    "J1 Étoiles gagnées", "J2 Étoiles gagnées", "J3 Étoiles gagnées", "J4 Étoiles gagnées", "J5 Étoiles gagnées",

    # Détail des étoiles
    "J1 Étoile amélioration", "J2 Étoile amélioration", "J3 Étoile amélioration", "J4 Étoile amélioration", "J5 Étoile amélioration",
    "J1 Étoile mechas", "J2 Étoile mechas", "J3 Étoile mechas", "J4 Étoile mechas", "J5 Étoile mechas",
    "J1 Étoile bâtiment", "J2 Étoile bâtiment", "J3 Étoile bâtiment", "J4 Étoile bâtiment", "J5 Étoile bâtiment",
    "J1 Étoile recrue", "J2 Étoile recrue", "J3 Étoile recrue", "J4 Étoile recrue", "J5 Étoile recrue",
    "J1 Étoile ouvrier", "J2 Étoile ouvrier", "J3 Étoile ouvrier", "J4 Étoile ouvrier", "J5 Étoile ouvrier",
    "J1 Étoile objectif", "J2 Étoile objectif", "J3 Étoile objectif", "J4 Étoile objectif", "J5 Étoile objectif",
    "J1 Étoile combat", "J2 Étoile combat", "J3 Étoile combat", "J4 Étoile combat", "J5 Étoile combat",
    "J1 Étoile popu max", "J2 Étoile popu max", "J3 Étoile popu max", "J4 Étoile popu max", "J5 Étoile popu max",
    "J1 Étoile puissance max", "J2 Étoile puissance max", "J3 Étoile puissance max", "J4 Étoile puissance max", "J5 Étoile puissance max",

    # Actions de section
    "J1 Mouvement section", "J2 Mouvement section", "J3 Mouvement section", "J4 Mouvement section", "J5 Mouvement section",
    "J1 Production section", "J2 Production section", "J3 Production section", "J4 Production section", "J5 Production section",
    "J1 Commerce section", "J2 Commerce section", "J3 Commerce section", "J4 Commerce section", "J5 Commerce section",
    "J1 Soutien section", "J2 Soutien section", "J3 Soutien section", "J4 Soutien section", "J5 Soutien section",
    "J1 Usine section", "J2 Usine section", "J3 Usine section", "J4 Usine section", "J5 Usine section",

    # Combats
    "J1 Combats gagnés", "J2 Combats gagnés", "J3 Combats gagnés", "J4 Combats gagnés", "J5 Combats gagnés",
    "J1 Combats perdus", "J2 Combats perdus", "J3 Combats perdus", "J4 Combats perdus", "J5 Combats perdus"
]

with open(Data_base, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data_base_python)

with open(DB_abandonée, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow("Lien partie abandonné")

email = "xxxxxxxx"
code = "xxxxxxx"


lien_fichier_source = "xxxxxxxxxxxxxx"

tout_les_lien = []

lien_partie_abandonné = []

with open(lien_fichier_source, "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=';')
    for ligne in reader:
        if ligne:
            tout_les_lien.append(ligne[0])

tout_les_lien = tout_les_lien[1:]

nbr_de_partie = len(tout_les_lien)

#début boucle

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

cpt = 1
buffer = []

for l in tout_les_lien:
    time_debut = time.time()

    lien = l

    driver.get(lien)

    time.sleep(1)

    try:
        refuse_button = driver.find_element(By.ID, "didomi-notice-disagree-button")
        refuse_button.click()
        time.sleep(1)
    except:
        pass


    #partie abandonné ou non, si oui passer l'itération
    try:
        if driver.find_element(By.ID, "game_abandonned").is_displayed():
            lien_partie_abandonné.append(lien)
            continue
    except NoSuchElementException:
        pass

    try:
        if driver.find_element(By.ID, "game_cancelled").is_displayed():
            lien_partie_abandonné.append(lien)
            continue
    except NoSuchElementException:
        pass

    #essayer de se connecter
    try:
        se_connecter = driver.find_element(By.LINK_TEXT, "Se connecter")
        se_connecter.click()

        time.sleep(1)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email'], input[id='username']"))
        )

        potential_inputs = driver.find_elements(By.CSS_SELECTOR, "input[name='email'], input[id='username']")
    
        email_input = None

        for i, input_field in enumerate(potential_inputs):
            try:
                is_visible = input_field.is_displayed()
                            
                if is_visible:
                    email_input = input_field
                    driver.execute_script("arguments[0].style.border='5px solid red'", email_input)
                    break
            except:
                continue

        email_input.click()
        email_input.clear()
        email_input.send_keys(email) 

        time.sleep(1)

        suivant1 = driver.find_element(By.LINK_TEXT,"Suivant")
        suivant1.click()

        time.sleep(1)

        input_code = driver.find_element(By.CSS_SELECTOR, "input[type='password'][placeholder='Mot de passe']")
        input_code.send_keys(code)

        time.sleep(1)

        candidats = driver.find_elements(By.CSS_SELECTOR, "a.bga-button.bga-button--blue")           
        candidats[7].click()
   
        time.sleep(1)

        xpath = "//a[contains(@class, 'bga-button--green-on-blue')]"
        candidats_jouons = driver.find_element(By.XPATH, xpath)

        candidats_jouons.click()
    
        time.sleep(3)

    except:
        pass


    #récupérer les données du site
    try :
        tableau_html = driver.find_element(By.ID, "player_stats")
    
        ligne_hmtl = tableau_html.find_elements(By.TAG_NAME, "tr")

        donnees_brut = []

        for ligne in ligne_hmtl :
            cellules = ligne.find_elements(By.CSS_SELECTOR, "td, th")

            ligne_texte = [c.text.strip() for c in cellules]

            if ligne_texte:
                donnees_brut.append(ligne_texte)

    except :
        pass


    #réordonner les données pour mon tableau

    nbr_joueur = len(donnees_brut[0])-1

    nouvelle_ligne = [None] * len(donnees_brut) * 5

    nouvelle_ligne[0]=lien
    nouvelle_ligne[1]=lien[-9:]
    nouvelle_ligne[2]=nbr_joueur

    ordre_donnée = ("Position de départ au premier tour", "Faction", "Joueur Mat", "Résultat de la partie", "Points provenant des étoiles", "Points provenant des territoires", "Points provenant des ressources", "Score de la tuile bonus de structure", "Points provenant des pièces", "Niveau de popularité", "Territoires contrôlés", "Ressources restantes", "Étoiles gagnées", "Etoile d'amélioration", "Étoile mécanique","Étoile des structures", "Recrutement d'une étoile", "Etoile d'ouvrier", "Étoile d'objectif", "Combat les étoile(s)", "Étoile de popularité maximun", "Etoile de puissance maximum", "Section de déplacement/gain prélevée", "Le rayon des fruits et légumes est cueilli", "Choix de la section commerciale", "Section de traversin prélevée", "Section d'usine choisie", "Combats gagnés", "Combats perdus" )

    donnees_dict = {
        ligne[0]: ligne[1:]
        for ligne in donnees_brut
        if ligne and len(ligne) > 1
        }

    z = 0
    for el in ordre_donnée :
        valeurs = donnees_dict.get(el)

        if el == "Résultat de la partie":
            for x in range (nbr_joueur) :
                ll = valeurs[x]
                valeurs[x] = ll.split("(")[1].replace(")", "")
    
        
        if el in donnees_dict:
            for x in range(nbr_joueur):
                nouvelle_ligne[z+3]= valeurs[x]
                z+=1
        else:
            print(el, "pas dans la liste")
            z+=1

        for x in range(5-nbr_joueur):
            nouvelle_ligne[z+3]=""
            z+=1

    nouvelle_ligne_sans_none = [x for x in nouvelle_ligne if x is not None]

    buffer.append(nouvelle_ligne_sans_none)

    if cpt == 50:
        with open(Data_base, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(buffer)
            buffer = []
        cpt = 0 

    time_fin = time.time()

    print(round(time_fin-time_debut, 2),"s pour la partie", lien[-9:])
    print(y, "sur ", nbr_de_partie)
    print(round(y/len(tout_les_lien)*100, 2),"%")


    cpt+=1
    y+=1

driver.quit()

if buffer:
    with open(Data_base, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(buffer)

with open(DB_abandonée, 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(lien_partie_abandonné)
    

destination = "c:/Users/arthu/OneDrive/Bureau/Programmation/Python/Scrapping/BGA- Scythe/Extraction"
shutil.move(Data_base, destination)
shutil.move(DB_abandonée, destination)

print("nbr de partie abandonné", len(lien_partie_abandonné))

time_fin_general = time.time()

print(round(time_fin_general-time_debut_general, 2),"s ou", round((time_fin_general-time_debut_general)/60, 2),"m ou", round((time_fin_general-time_debut_general)/60/60, 2), "h")

print("Fin")
