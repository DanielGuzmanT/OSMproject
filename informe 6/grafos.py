class Grafo:
    def __init__(self):
        self.ymin = None
        self.xmin = None
        self.ymax = None
        self.xmax = None
        self.dic_vertices = {}
        self.conj_aristas = set()

    def listaVertices(self):
        return self.dic_vertices.keys()

    def agregarVertice(self, nodo):
        self.dic_vertices[nodo.id] = nodo

    def agregarCoorXY(self, root):
        bounds = root.find("bounds")
        self.ymin = float(bounds.get("minlat"))
        self.xmin = float(bounds.get("minlon"))
        self.ymax = float(bounds.get("maxlat"))
        self.xmax = float(bounds.get("maxlon"))


class Vertice:
    def __init__(self, idv):
        self.id = idv
        self.x = None
        self.y = None
        self.nombre = ""