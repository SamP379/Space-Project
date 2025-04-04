
from math import cos, asin, sqrt, pi

def haversine(position1 : tuple, position2 : tuple):
    # https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
    lat1 = position1[0]
    lon1 = position1[1]
    lat2 = position2[0]
    lon2 = position2[1]    
    r = 6371 
    p = pi / 180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return round(2 * r * asin(sqrt(a)))

    
        
