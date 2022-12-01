import googlemaps
from googlemaps import places
from random import randint
import configparser

def search_cafe(latitude:float,longitude:float,type:str):
    config = configparser.ConfigParser()
    config.read('config.ini')
    location = (latitude, longitude)
    gmaps = googlemaps.Client(config['Google_API']['GOOGLE_PLACES_API_KEY'])
    places_radar_result = gmaps.places(type,location,300,True)
    data = places_radar_result['results']
    if len(data)<5:
        ret = randint(0,len(data))
    else:
        ret = randint(0,5)
    return places_radar_result['results'][ret],location
