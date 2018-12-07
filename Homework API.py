#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:40:57 2018

@author: MariusD
"""
#%%
#White Belt

import requests

def lyrics(artist, song): 
    
    url = "https://api.lyrics.ovh/v1/" + artist + "/" + song
        
    response  = requests.get(url)
    
    print(response.json()["lyrics"])

#%%
#Blue Belt
    
import requests

def location_of_iss():
    
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    position = response.json()["iss_position"]
    
   
    print("The current position of the ISS is {}:{}".format(
            position["latitude"],
            position["longitude"]))

#%%
#Black Belt
    
import requests

    
def population_of_countries():
    url = "http://api.population.io:80/1.0/countries"
    response = requests.get(url)
    
    countries = []
    
    for country in set(response.json()["countries"]):   
        if country.isupper():
            continue
        else:
            if  len(countries) < 10:
                countries.append(country)      
    for country in countries:
        url = "http://api.population.io:80/1.0/population/" + country  + "/today-and-tomorrow/"
        response = requests.get(url)
        population = response.json()["total_population"]
        
        print(country)
        for day in population:
            print(day["date"] + ": " + str(day["population"]))