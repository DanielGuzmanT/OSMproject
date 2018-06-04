import math 

def distancia(lat1,lon1,lat2,lon2):
	dlat=lat1*math.pi/180-lat2*math.pi/180  # diferencia de latitudes 
	dlon=lon1*math.pi/180-lon2*math.pi/180  #diferencia de longitudes
	R=6372.795477598 # Km del radio de la tierra

	aux=math.sin(dlat/2)**2 + math.cos(lat1*math.pi/180)*math.cos(lat2*math.pi/180)*(math.sin(dlon/2))**2
	dist=2*R*math.asin(math.sqrt(aux))
	return dist   #retornamos distania en kilometros 


dist= distancia(-12.0671609,-77.07424960000002,-12.065781600000001,-77.07557849999998)
print(dist)


