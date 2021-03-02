from nodo import Nodo
from lista import Lista

class Matriz(Lista):
    #m > filas
    #m > cols
    def __init__(self, m, n, nombre):
        self.m = m
        self.n = n
        self.nombre = nombre
        super().__init__()

    def obtener_elem(self, x, y):
        if((y >= self.m) or (x >= self.n)):
            raise RuntimeError('Límites no definidos en la matriz')
        fila = self.get(y)
        celda = fila.get(x)
        return celda.valor

    def get_name(self):
        return self.nombre
        
    def get_n(self):
        return self.n

    def get_m(self):
        return self.m

    def __str__(self):
        resultado = '{} de tamaño {}x{}, con valor: {}'.format(self.nombre, self.m, self.n, super().__str__())
        return resultado