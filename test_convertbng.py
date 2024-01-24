place,lat,lon = ('Exmouth', 50.6200, -3.4137)

from convertbng.util import convert_bng

eastings, northings = convert_bng(lon, lat)
e = eastings[0]
n = northings[0]

print(place, lat, lon)
print(e, n)

from convertbng.util import convert_bng

def lat_lon_to_northings_eastings(lat, lon):
    eastings, northings = convert_bng(lon, lat)
    return northings[0], eastings[0]


assert lat_lon_to_northings_eastings(lat, lon) == (n, e)
