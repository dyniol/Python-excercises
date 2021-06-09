import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):  # produce different colors for markers depending on elevation
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.50, -98.0], zoom_start=5) # set default location

fgv = folium.FeatureGroup(name="Volcanoes") # feature group to add various features to map and keep code clean and organised

for lt, ln, el in zip(lat, lon, elev): # zip() function goes trough many lists at same time
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+"m", fill_color=color_producer(el), color = 'gray', fill_opacity=0.7)) # add marker element to the map (set location, popup and icon for Marker)

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(   
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']< 10000000 
    else 'orange' if 10000000 <= x['properties']['POP2005'] < 30000000 else 'red'})) # adding polygons to mark countries in different colors depending on population

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) # layer control menu
map.save("Map1.html") # save file to Map1.html
