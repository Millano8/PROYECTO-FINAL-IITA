import requests
from bs4 import BeautifulSoup

CLIMA_VILLE_URL = "https://www.tiempo.com/general-villegas.htm"
CLIMA_CABA_URL = "https://www.tiempo.com/buenos-aires.htm"
CLIMA_LA_PLATA_URL = "https://www.tiempo.com/la-plata.htm"


def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")


def get_clima_villegas():
    soup = get_soup(CLIMA_VILLE_URL)
    scrap_clima = soup.find_all("div", class_="item-principal")
    scrap_temp = []
    for climas in scrap_clima:
        span_temp = soup.find(
            "span", class_="dato-temperatura changeUnitT").text
        scrap_temp.append(span_temp)
    respuesta = f"El clima de Villegas en este momento es de {scrap_temp[0]} grados"
    return respuesta


def get_clima_capi():
    soup = get_soup(CLIMA_CABA_URL)
    scrap_clima = soup.find_all("div", class_="item-principal")
    scrap_temp = []
    for climas in scrap_clima:
        span_temp = soup.find(
            "span", class_="dato-temperatura changeUnitT").text
        scrap_temp.append(span_temp)
    respuesta = f"El clima de La Ciudad Autonoma en este momento es de {scrap_temp[0]} grados"
    return respuesta


def get_clima_la_plata():
    soup = get_soup(CLIMA_LA_PLATA_URL)
    scrap_clima = soup.find_all("div", class_="item-principal")
    scrap_temp = []
    for climas in scrap_clima:
        span_temp = soup.find(
            "span", class_="dato-temperatura changeUnitT").text
        scrap_temp.append(span_temp)
    respuesta = f"El clima de La Plata en este momento es de {scrap_temp[0]} grados"
    return respuesta
