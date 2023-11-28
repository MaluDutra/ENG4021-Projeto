from .models import Events, Category, Price, Time
import requests
import re
from bs4 import BeautifulSoup

def scrape_events():
    url = "https://dasartes.com.br/agenda/pegadas-do-pequeno-principe-riosul-shopping/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    nameSoup = soup.find("h1").text.strip()  #NAME
    string_price = soup.find(string=re.compile("Valores dos ingressos")).text
    lista_price = string_price.split(' ')
    priceSoup = lista_price[7]  #PRICE
    auxiliar = soup.find_all("strong")
    data_abertura = auxiliar[1].text  #DATE
    horario_inicio = auxiliar[3].text  #TIME
    horario_fim = auxiliar[4].text  #TIME
    categorySoup = soup.find(
      "div", class_="post-tags full-width-wrapper").text.strip()  #CATEGORY
    lista_location = soup.find_all("li", class_="post-info-full")
    string_location = lista_location[0].text.strip().split(' ')
    locationSoup = string_location[9]  #LOCATION

    if Events.objects.filter(name=nameSoup).exists():
        return
    else:
        Events.objects.create(
          link=url,
          name=nameSoup,
          location=locationSoup)
        return
