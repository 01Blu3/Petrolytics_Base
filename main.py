import folium
from numpy import empty
# from folium import HeatMap
import requests
from keys import *
# import urllib.parse
import random
from folium.plugins import HeatMap

# Our data set is working with
# 29 / 47 refineries for TX ( 2014 )
# 19 / 19 refineries for LA ( 2015 )
# 15 / 18 refineries for CA ( 2020 )
# 2019 -> 135 refineries in USA | Our coverage is 49%
cities = []
refineries_in_state = [['TX', 47], ['LA', 19], ['CA', 18]]
refinery_scores = []

m = folium.Map(location=[31.000000, -100.000000], zoom_start=6)

# data = [[lat, lng, hm intensity]]
# parsed_city = urllib.parse.quote(city.encode('utf8'))


# name of address is given and lat, lng coordinates are returned
def get_coordinates(location):
    res = requests.get(
        f"https://api.mapbox.com/geocoding/v5/mapbox.places/{location}.json?limit=2&access_token={API_KEY_MAPBOX}")
    data = res.json()
    coordinates = data['features'][0]['geometry']['coordinates']
    return coordinates


# Looks at refinery folder and adds all tx cities stored to a list
def get_refinery_cities_tx():
    with open('./refineries/texas_cities_ref.txt') as f:
        lines = f.readlines()
        for line in lines:
            end_index = line.rfind('\\')
            city = line[:end_index]
            cities.append(city)


# Looks at refinery folder and adds all lousiana cities stored to a list
def get_refinery_cities_la():
    with open('./refineries/la_cities_ref.txt') as f:
        lines = f.readlines()
        for line in lines:
            end_index = line.rfind('\\')
            city = line[:end_index]
            cities.append(city)


get_refinery_cities_tx()
get_refinery_cities_la()

is_empty = False
# gets coordinates for each city and stores them in a list
# only done when updates to data points are needed
# coord = get_coordinates(cities)
if (is_empty):
    for city in cities:
        coord = get_coordinates(city)
        refinery_scores.append(coord)
    # writes weighted scores list to a text-file
    with open('data_points.txt', 'w') as f:
        for point in refinery_scores:
            f.write(f'{point}\n')
        is_empty = False

# print(cities)

data_points = []


def get_datapoints():
    with open('./data_points.txt') as f:
        lines = f.readlines()
        for line in lines:
            end_index_1 = line.rfind(',')
            num2 = line[1:end_index_1]
            num1 = line[end_index_1 + 2:-2]
            data_points.append([float(num1), float(num2)])


get_datapoints()
coord_points = data_points
# print(data_points)

rand_weights = []
x = 0
while (x < 40):
    rand_weights.append(random.uniform(0, 1))
    x += 1

x = 0
for item in data_points:
    item.append(rand_weights[x])
    x += 1

# print(data_points)

HeatMap(data_points).add_to(m)

m.save('index.html')
