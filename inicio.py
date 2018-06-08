from parseOsm import *
from grafos import *
from kruskal import kruskal
from grafico import mapeoarbol
from depuracion import depurar


archivo = "mapa.osm"

depurar(archivo)
print("fin de depuracion")

archivo2 = "modificado.xml"
grafo = Grafo()
grafo = grafoOSM(archivo2)
print("fin de procesamiento de datos OSM")
# PRUEBA
k = kruskal(grafo)
print("fin de kruskal")
mapeoarbol(grafo, k)
print("fin de grafico de mapa")

#otros comentarios
print("FIN")
# comentarios para probar un segundo commit