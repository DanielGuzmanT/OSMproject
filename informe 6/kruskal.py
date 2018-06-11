# Implementación del algoritmo Kruskal
from grafos import *
# Variables globales
base = dict()
ord = dict()


# Función para generar conuntos
def make_set(v):
    base[v] = v
    ord[v] = 0


# Implementación de la función de búsqueda
# de manera recursiva
def find(v):
    if base[v] != v:
        base[v] = find(base[v])
    return base[v]


# Implementación de la unión de conjuntos
def union(u, v):
    v1 = find(u)
    v2 = find(v)
    if ord[v1] > ord[v2]:
        base[v2] = v1
    else:
        base[v1] = v2
        if ord[v1] == ord[v2]:
            ord[v2] += 1

# Función principal del algoritmo Kruskal
def kruskal(graph):
    # A = {conjunto vacío}
    mst = set()

    # Para todo vértice v en G.V
    #for v in graph.vertices.keys():
    for v in graph.listaVertices():
        make_set(v)

    # Ordena la lista G.E en forma no decendente por su peso w
    # En este caso usamos el ordenador dentro de python
    edges = list(graph.conj_aristas)
    edges.sort()

    # Para toda arista(u,v) en G.E
    for e in edges:
        weight, u, v = e
        # Si encontrar-conjunto(u) != encontrar-conjunto(v)
        if find(u) != find(v):
            # A = A union (u,v)
            union(u, v)
            # Union(u,v)
            mst.add(e)
    return mst
