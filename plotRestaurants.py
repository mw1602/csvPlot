## takes in a CSV file with a name field and creates a leaflet map with icons

import folium as fm
import pandas as pd
from googleplaces import GooglePlaces, types, lang


# get the API key

with open('csvPlot/api_key.txt') as f:
    API_KEY = f.read()


# import the CSV file 

restaurants = pd.read_csv('chicagorestaurants.csv')

# initialize map

map_osm = fm.Map(location=[41.874996, -87.627286]) #this is the UC

# go through each restaurant, get their location and name, add a marker

for restaurant in restaurants.Name:
    query_result = google_places.nearby_search(
        location='Chicago, USA', name = restaurant,
        radius=20000, types=[types.TYPE_FOOD])
    
    for place in query_result.places:
        map_osm.simple_marker([place.geo_location['lat'],place.geo_location['lng']], popup = place.name, marker_color = 'green')

        


map_osm.create_map(path='chicago_restaurants.html')
    