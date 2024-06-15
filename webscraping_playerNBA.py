import pandas as pd
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

jogador = input('Qual jogador de basquete você deseja analisar? ')

options = Options()
options.add_argument('--window-size=1920,1080')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=options)

url = 'https://www.flashscore.com.br/'

driver.get(url)
try:
    search = driver.find_element(By.XPATH, "//*[@id='search-window']/span").click()
    sleep(2)
    search_text = driver.find_element(By.XPATH, "//*[@id='search-window']/div/div/div[2]/input")
    search_text.send_keys(jogador)
    search_text.send_keys(Keys.RETURN)
    sleep(5)
    sugestoes_jogador = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='search-window']/div/div/div[3]")))
    perfil_jogador = driver.find_element(By.XPATH, "//*[@id='search-window']/div/div/div[3]/div/a[1]").click()
    sleep(2)
    # link_jogador = perfil_jogador.get('href')
    # print(link_jogador)
    # driver.get(link_jogador)
    content_page = driver.page_source
    parser_page = BeautifulSoup(content_page, 'html.parser')
    # print(parser_page.text)
    jogos = parser_page.find_all('div', class_=re.compile("lmTable__row lmTable__row--basketball"))
    sleep(5)

    pts_valores = []
    reb_valores = []
    ass_valores = []

    for jogo in jogos:
        pts = jogo.find('div',class_=re.compile('lmTable__icon lmTable__icon--basketball-169'))
        reb = jogo.find('div',class_=re.compile('lmTable__icon lmTable__icon--basketball-713'))
        ass = jogo.find('div', class_=re.compile('lmTable__icon lmTable__icon--basketball-541'))

        if pts and reb:
            pts_text = int(pts.text)
            reb_text = int(reb.text)
            ass_text = int(ass.text)
            pts_valores.append(int(pts_text))
            reb_valores.append(int(reb_text))
            ass_valores.append(int(ass_text))
            print(f'Pontos {jogador}: {pts_text}')
            print(f'Rebotes {jogador}: {reb_text}')
            print(f'Assistencias {jogador}: {ass_text} \n')

        else:
            ('Não possui PTS e REB')

        # print(f'Pontos {jogador}: {pts} \n Rebotes {jogador}: {reb_text}')

    pts_total = sum(pts_valores)
    reb_total = sum(reb_valores)
    ass_total = sum(ass_valores)
    min_pts = min(pts_valores)
    min_reb = min(reb_valores)
    min_ass = min(ass_valores)
    max_pts = max(pts_valores)
    max_reb = max(reb_valores)
    max_ass = max(reb_valores)
    media_pts = pts_total / len(pts_valores)
    media_reb = reb_total / len(reb_valores)
    media_ass = ass_total / len(ass_valores)

    print(f'Média de pontos por partida: {round(media_pts, 2)}')
    print(f'Média de rebotes por partida: {round(media_reb, 2)}')
    print(f'Media de assistencias por partida: {round(media_ass, 2)}')
    print(f'Minimo de pontos em uma partida: {min_pts}')
    print(f'Minimo de rebotes em uma partida: {min_reb}')
    print(f'Minimo de assistencias em uma partida: {min_ass}')
    print(f'Maximo de pontos em uma partida: {max_pts}')
    print(f'Maximo de rebotes em uma partida: {max_reb}')
    print(f'Maximo de assistencias em uma partida: {max_ass}')
    print("Ok")
except:
    print('Nenhum jogador foi encontrado')