import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ast
from bs4 import BeautifulSoup
import requests
import re
import sqlite3

url = "https://lista.mercadolivre.com.br/notebook#D[A:notebook]"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('li', class_='ui-search-layout__item')

def clean_data():
    items_list = []
    for i in items:
        title = i.find('h3', class_='poly-component__title-wrapper').text
        clean_title = re.sub(r'\bNOVO|FRETE GRATIS|FRETE GRÁTIS|GAMER|PROMOCAO|PROMOÇAO|PROMOCÃO|PROMOÇÃO|OFERTA|™|®', '', title, flags=re.IGNORECASE)
        clean_title = clean_title.replace("  ", " ")

        price = i.find('span', class_='andes-money-amount__fraction').text
        clean_price = int(price.replace(".", ""))

        ram = re.search(r'(\d+\s*GB)\s(?=RAM|MEMORIA|MEMÓRIA)', clean_title, flags=re.IGNORECASE)
        storage = re.search(r'(\d+\s*GB|\d+\s*TB)\sSSD', clean_title, flags=re.IGNORECASE)
        color = re.search(r'\b(?:color|cor)?\s\b(PRETO|BRANCO|CINZA|VERMELHO|AZUL|ROSA|PRATA|AMARELO|VERDE|BLACK|WHITE|SILVER|GREY|GRAY)', clean_title, flags=re.IGNORECASE)

        item_dict = {
            "full_title": clean_title,
            "memory": ram.group(1) if ram else "N/A",
            "storage": storage.group(1) if storage else "N/A",
            "color": color.group(1) if color else "N/A",
            "price": clean_price
        }
        items_list.append(item_dict)
    return items_list

df = pd.DataFrame(clean_data())
connection = sqlite3.connect('mercado_livre_data.db')
df.to_sql('listings', connection, if_exists="replace", index="False")

test_sql = pd.read_sql('SELECT * FROM listings WHERE memory != "N/A" LIMIT 5', connection)
print(test_sql)
connection.close()