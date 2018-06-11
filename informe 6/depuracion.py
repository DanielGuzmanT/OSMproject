
import xml.etree.ElementTree as et
from grafos import Vertice


def depurar(archivo):
	tree = et.parse(archivo)
	root = tree.getroot()

	eliminarRelations(root)
	dict_nodos = {} # se lleva registro de los nodos que existen solo en los caminos
	eliminarWays(dict_nodos, root)
	eliminarNodes(dict_nodos, root)
	tree.write('modificado.xml')


def eliminarRelations(root):
	for relation in root.findall("relation"):
		root.remove(relation)

def eliminarWays(dict_nodos, root):	
	# eliminación de caminos que no sean 'highway'
	for way in root.findall("way"):
	    '''obtenemos datos: autopista(boolean) 
	       - si es autopista, nombre(string)
	       - el nombre de la calle'''
	    autopista, nombre = obtenerDatosWay(way)
	    "en caso no sea una autopista, se elimina y continua iterando"
	    if not autopista:
	    	root.remove(way)
	    	continue
	    else:
	    	way.attrib.pop("changeset")
	    	way.attrib.pop("timestamp")
	    	way.attrib.pop("uid")
	    	way.attrib.pop("user")
	    	way.attrib.pop("version")
	    	way.attrib.pop("visible")
	    	# guardamos los nodos de los caminos
	    	for nd in way.findall("nd"):
	    		dict_nodos[nd.get("id")] = 0
	
	
def eliminarNodes(dict_nodos, root):
	# almacenamiento de todos los nodos en diccionario
	dict_nodos = {}
	for nodo in root.findall("node"):
		dict_nodos[nodo.get("id")] = 0
	# eliminación de nodos que no se encuentran en los caminos
	# los que no se eliminan, se borran atributos que no se utilizan    
	for nodo in root.findall("node"):
		if not nodo.get("id") in dict_nodos:
			root.remove(nodo)
		else:
			nodo.attrib.pop("changeset") 
			nodo.attrib.pop("timestamp")
			nodo.attrib.pop("uid")
			nodo.attrib.pop("user")
			nodo.attrib.pop("version")
			nodo.attrib.pop("visible")


def obtenerDatosWay(way):
    autopista = False
    nombre = ""
    for tag in way.findall("tag"):
        # highway no puede ser "*", el cual significa ser una calle cerrada
        if tag.get("k") == "highway" and tag.get("v") in [
        'unclassified',
        'residential',
        'primary',
        'secondary',
        'tertiary',
        'primary_link',
        'living_street'
        ]: autopista = True
        elif tag.get("k") == "name": nombre = tag.get("v")
        else: way.remove(tag)
    return autopista, nombre

