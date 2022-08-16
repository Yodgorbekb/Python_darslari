# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 14:54:17 2022

@author: Ogabek
"""

                        #PYTHON DARSLARI
                        #34-DARS
                        #JSON

#import json
#import googlemaps
#from apikey import APIKEY
 
##GoogleMaps
#gmaps = googlemaps.Client(key=APIKEY)

#data = gmaps.geocode('Olmazor,Toshkent, Uzbekiston')


#g = json.dump(data[0], indent = 4, sort_keys=True)
#print(g)


import json

x = 10
x_json = json.dumps(x)


y = 5.5
y_json = json.dumps(y)


m = True
m_json = json.dumps(m)


#ism = "anvar"
#ism_json = dumps(ism)
#familiya_json = json_dumps('narzullayev')

sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)



bemor = {
    "ism": "Alijon Valiyev",
    "yosh":30,
    "oila":True,
    "farzandlari": ("Ahmad, Bonu"),
    "allergiya": None,
    "dorilar": [
        {"nomi":"Analgin", "miqdori": 0.5},
        {"nomi":"Pannadol", "miqdori":1.2}
      ]
    }


bemor_json = json.dumps(bemor)
print(bemor_json)


with open('bemor.json','w') as f:
    json.dump(bemor,f)
    
    
with open('sonlar.json','w') as f:
    json.dump(sonlar,f)
    
bemor2 = json.loads(bemor_json)





import requests
import json

wikiurl = 'https://qkwr.com/qwerty'
response = requests.get(wikiurl)
print(json.dumps(response.json(), indent=4))




import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))