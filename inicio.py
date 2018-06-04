from parseOsm import *
from grafos import *
from kruskal import kruskal
from grafico import mapeoarbol

archivo = "pucp.osm"
grafo = Grafo()

grafo = grafoOSM(archivo)

# PRUEBA
k = kruskal(grafo)
mapeoarbol(grafo, k)