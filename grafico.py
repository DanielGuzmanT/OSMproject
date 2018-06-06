import matplotlib.pyplot as plt
from grafos import *

def mapeoarbol(graph, mts):
	plt.xlabel("Longitud")
	plt.ylabel("Latitud")
	plt.axis([graph.xmin, graph.xmax, graph.ymin, graph.ymax])
	#grafo
	imprimirGrafo(graph)
	#kruskal
	imprimirCalles(mts, graph, 'm')
	plt.show()

def imprimirNombres(coorx, coory, name):
	for i in range(len(name)):
		plt.text(coorx[i], coory[i], name[i], fontsize = 7)

def imprimirCalles(conjunto, graph, color = 'y'):
	for tupla in conjunto:
		peso, id1, id2 = tupla
		nd1, nd2 = graph.dic_vertices[id1], graph.dic_vertices[id2]
		x1, y1, x2, y2 = nd1.x, nd1.y, nd2.x, nd2.y
		plt.plot([x1, x2], [y1, y2], color)

def imprimirGrafo(graph):
	# creación de listas de coordenadas
	coorx = []
	coory = []
	name = []
	for v in graph.dic_vertices.values():
		coorx.append(v.x)
		coory.append(v.y)
		name.append(v.id)
	# nodos
	# plt.plot(coorx, coory, 'ro')
	# nombres de las calles
	imprimirNombres(coorx, coory, name)
	# calles (vértices)
	imprimirCalles(graph.conj_aristas, graph)