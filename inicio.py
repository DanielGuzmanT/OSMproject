from parseOsm import *
from grafos import *
from kruskal import kruskal
from grafico import mapeoarbol
from depuracion import depurar


archivo = "mapa.osm"

depurar(archivo)
archivo2 = "modificado.xml"

grafo = Grafo()

grafo = grafoOSM(archivo2)

# PRUEBA
k = kruskal(grafo)
mapeoarbol(grafo, k)

#otros comentarios
print("FIN")
# comentarios para probar un segundo commit