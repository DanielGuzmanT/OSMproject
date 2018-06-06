import xml.etree.ElementTree as et
from grafos import Vertice




def obtenerDatosWay(way):
    autopista = False
    nombre = ""
    for tag in way.findall("tag"):
        # highway no puede ser "*", el cual significa ser una calle cerrada
        if tag.get("k") == "highway" and tag.get("v") != '*': autopista = True
        elif tag.get("k") == "name": nombre = tag.get("v")
        else: way.remove(tag)
    return autopista, nombre

##################################################################################################
def depurar(archivo):
	tree = et.parse(archivo)
	root = tree.getroot()

	# eliminación de etiquetas relation
	for relation in root.findall("relation"):
		root.remove(relation)

	# almacenamiento de todos los nodos en diccionario
	dict_nodos = {}
	for nodo in root.findall("node"):
		dict_nodos[nodo.get("id")] = 0

	# eliminación de caminos que no sean 'highway'
	# además, se aumenta el número de conexiones de cada nodo leído
	for way in root.findall("way"):
	    "obtenemos datos: autopista(boolean) - si es autopista, nombre(string) - el nombre de la calle"
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
	    "guardamos el número de aristas de los nodos en diccionario"
	    nd = way.find("nd")
	    dict_nodos[nd.get("ref")] = -1 # el primero solo debe tener 1 conexion en este camino
	    for nd in way.findall("nd"):
	        dict_nodos[nd.get("ref")] += 2 # los nodos intermedios deben tener 2 conexiones en este camino
	    dict_nodos[nd.get("ref")] = -1 # el ultimo solo debe tener 1 conexion en este camino

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
	tree.write('modificado.xml')
