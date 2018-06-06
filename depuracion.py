import xml.etree.ElementTree as et
from grafos import Vertice

tree = et.parse('pucp.osm')
root = tree.getroot()


# eliminación de etiquetas relation
for relation in root.findall("relation"):
	root.remove(relation)

# almacenamiento de todos los nodos en diccionario
conj_nodos = {}
for nodo in root.findall("node"):
	conj_nodos[nodo.get("id")] = 0

# eliminación de caminos que no sean 'highway'
# además, se aumenta el número de conexiones de cada nodo leído
for way in root.findall("way"):
    "obtenemos datos: autopista(boolean) - si es autopista, nombre(string) - el nombre de la calle"
    autopista, nombre = obtenerDatosWay(way)
    "en caso no sea una autopista, se elimina y continua iterando"
    if not autopista:
    	root.remove(way)
    	continue
    "se inicia la conexión entre dos nodos de la misma calle"
    id1 = None   # id del nodo actual
    idant = None # id del nodo anterior
    for nd in way.findall("nd"):
        id1 = nd.get("ref")
        graph.dic_vertices[id1].autopista = True
        if idant != None:
            # crear tupla (DISTANCIA, ID nodo 1, ID nodo Anterior) = una arista
            # agregar la tupla creada en el conjunto de aristas del grafo
            graph.conj_aristas.add(crearTupla(graph, id1, idant))
        idant = id1
tree.write('pucppurgado.xml')


def obtenerDatosWay(way):
    autopista = False
    nombre = ""
    for tag in way.findall("tag"):
        # highway no puede ser "*", el cual significa ser una calle cerrada
        if tag.get("k") == "highway" and tag.get("v") != '*': autopista = True
        elif tag.get("k") == "name": nombre = tag.get("v")
    return autopista, nombre
