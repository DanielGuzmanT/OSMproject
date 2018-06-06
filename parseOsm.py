import xml.etree.ElementTree as et
import math
from grafos import *
'''
Dato un archivo .osm o .xml que almacena nodos y caminos,
se retorna un grafo que almacene todos estos datos usando
las clases Grafo y Vertice
'''

def grafoOSM(archivo):
    graph = Grafo()
    tree = et.parse(archivo)
    root = tree.getroot()
    graph.agregarCoorXY(root)
    # se agregan los nodos al grafo a retornar
    agregarNodos(graph, root)
    # se agregan las aristas al grafo a retornar
    agregarAristas(graph, root)
    return graph

def agregarNodos(graph, root):
    for node in root.findall("node"):
        nodo = Vertice(node.get("id"))
        nodo.x = float(node.get("lon"))
        nodo.y = float(node.get("lat"))
        graph.agregarVertice(nodo)

def agregarAristas(graph, root):
    for way in root.findall("way"):
        "obtenemos datos: autopista(boolean)-si es autopista, nombre(string)-el nombre de la calle"
        autopista, nombre = obtenerDatosWay(way)
        "en caso no sea una autopista, continua iterando con otros caminos o ways"
        if not autopista: continue
        "se inicia la conexión entre dos nodos de la misma calle"
        id1 = None   # id del nodo actual
        idant = None # id del nodo anterior
        for nd in way.findall("nd"):
            id1 = nd.get("ref")
            # se agrega el nombre de la calle a todos los nodos que pertenecen a esta
            graph.dic_vertices[id1].nombre += nombre + '\n'
            # se le señala como nodo perteneciente a una autopista
            graph.dic_vertices[id1].autopista = True
            if idant != None:
                # crear tupla (DISTANCIA, ID nodo 1, ID nodo Anterior) = una arista
                # agregar la tupla creada en el conjunto de aristas del grafo
                graph.conj_aristas.add(crearTupla(graph, id1, idant))
            idant = id1

# observacion: nodo anterior es tratado como nodo2, esto no afecta al algoritmo de kruskal,
# pues esta es en base a un grafo no dirigido, modificar esto cuando se trabajo con los dirigidos
def crearTupla(graph, id1, idant):
    nodo1 = graph.dic_vertices[id1]
    nodo2 = graph.dic_vertices[idant]
    tupla = (distancia(nodo1.y, nodo1.x, nodo2.y, nodo2.x), nodo1.id, nodo2.id)
    return tupla

def distancia(lat1,lon1,lat2,lon2):
    dlat=lat1*math.pi/180-lat2*math.pi/180  # diferencia de latitudes 
    dlon=lon1*math.pi/180-lon2*math.pi/180  # diferencia de longitudes
    R=6372.795477598 # Km del radio de la tierra
    aux=math.sin(dlat/2)**2 + math.cos(lat1*math.pi/180)*math.cos(lat2*math.pi/180)*(math.sin(dlon/2))**2
    dist=2*R*math.asin(math.sqrt(aux))
    return dist   #retornamos distania en kilometros 

def obtenerDatosWay(way):
    autopista = False
    nombre = ""
    for tag in way.findall("tag"):
        # highway no puede ser "*", el cual significa ser una calle cerrada
        if tag.get("k") == "highway" and tag.get("v") != '*': autopista = True
        elif tag.get("k") == "name": nombre = tag.get("v")
    return autopista, nombre
