import matplotlib.pyplot as plt
from grafos import *

def mapeoarbol(graph, mts):
	plt.title("MAPA DE RUTAS Y ÁRBOL DE COSTE MÍNIMO")
	plt.xlabel("Longitud")
	plt.ylabel("Latitud")
	plt.axis([graph.xmin, graph.xmax, graph.ymin, graph.ymax])
	#grafo
	print("impresion de calles")
	imprimirCalles(graph.conj_aristas, graph)
	#kruskal
	print("impresion de arbol de kruskal")
	imprimirCalles(mts, graph, 'm')
	# impresion de direcciones de las casas de los tres integrantes
	alumno1 = "5381377898"
	alumno2 = "1273696581"
	alumno3 = "651807699"
	imprimirCasa(graph, alumno1, "Guzmán")
	imprimirCasa(graph, alumno2, "Reyes")
	imprimirCasa(graph, alumno3, "Cabrera")
	# impresion de la dirección de la universidad PUCP
	imprimirPucp()
	plt.show()

def imprimirCasa(graph, idCasa, alum):
	v = graph.dic_vertices[idCasa];
	plt.plot([v.x],[v.y], 'ro')
	plt.text(v.x,v.y, "casa de " + alum, fontsize = 10)	

def imprimirCalles(conjunto, graph, color = 'y'):
	i = 0
	for tupla in conjunto:
		peso, id1, id2 = tupla
		nd1, nd2 = graph.dic_vertices[id1], graph.dic_vertices[id2]
		x1, y1, x2, y2 = nd1.x, nd1.y, nd2.x, nd2.y
		if i % 550 == 0: print("cargando...")
		i += 1
		plt.plot([x1, x2], [y1, y2], color)

def imprimirPucp():
	plt.plot([-77.0779],[-12.0687],'ro')
	plt.text(-77.0805,-12.069,"PUCP",fontsize = 15)	

'''
def imprimirNombres(coorx, coory, name):
	i = 0
	for i in range(len(name)):
		if i % 100 == 0: print("cargando..."); i += 1
		plt.text(coorx[i], coory[i], name[i], fontsize = 7)
'''