from bs4 import BeautifulSoup
import requests

""" Scrapes the cities that oil refineries are located in Texas and places them in a text-file """

res_tx = requests.get(
    'https://www.arnolditkin.com/blog/plant-accidents/comprehensive-list-of-refineries-in-texas/')
soup_tx = BeautifulSoup(res_tx.text, 'html.parser')

cities = []

for city in soup_tx.find_all('u'):
    city_str = str(city)
    end_index = city_str.rfind('</')
    formatted_str = city_str[3:end_index]
    cities.append(formatted_str)
print(cities)

with open('texas_cities_ref.txt', 'w') as f:
    for tx_city in cities:
        f.write(f'{tx_city}\n')
    f.write(f'{len(cities)}')

""" Scrapes the cities that oil refineries are located in Lousiana and places them in a text-file """

cities_la = []

res_la = requests.get(
    'https://www.arnolditkin.com/blog/plant-accidents/comprehensive-list-of-louisiana-refineries/')
soup_la = BeautifulSoup(res_la.text, 'html.parser')

for city in soup_la.find_all('u'):
    city_str = str(city)
    end_index = city_str.rfind('</')
    formatted_str = city_str[3:end_index]
    cities_la.append(formatted_str)
print(cities_la)

with open('la_cities_ref.txt', 'w') as f:
    for la_city in cities_la:
        f.write(f'{la_city}\n')
    f.write(f'{len(cities_la)}')

""" Scrapes the cities that oil refineries are located in California and places them in a text-file """
# https://ww2.arb.ca.gov/resources/documents/california-refineries
