from nodo import Nodo

class Lista(Nodo):
    def __init__(self):
        super().__init__()
        self.cabeza = Nodo()
        self.contador = 0
        self.valor = self.__str__()
        self.frecuencia = 1
        self.indice_frecuencia = None
        
    def agregar(self, nuevo_nodo):
        nodo = self.cabeza
        while(nodo.siguiente):
            nodo = nodo.siguiente
        nodo.siguiente = nuevo_nodo
        self.contador += 1
        self.valor = self.__str__()
        
    def get(self, i):
        if (i >= self.contador):
            return None
        nodo = self.cabeza.siguiente
        n = 0
        while(nodo):
            if (n == i):
                return nodo
            nodo = nodo.siguiente
            n += 1

    def __getitem__(self, i):
        return self.get(i)

    def length(self):
        return self.contador

    def primero(self):
        return self.get(0)

    def ultimo(self):
        return self.get(self.length() - 1)

    def __str__(self):
        resultado = "["
        for i in range(self.length()):
            nodo = self.get(i)
            if (i == self.length()-1):
                resultado += '{}'.format(nodo.valor)
                break
            resultado += '{}, '.format(nodo.valor)
        resultado += "]"
        return resultado
    def clonar(self):
        nueva = Lista()
        for i in range(self.length()):
            valor = self.get(i).valor
            nuevo_nodo = Nodo(valor)
            nueva.agregar(nuevo_nodo)
            nueva.valor = self.__str__()
        return nueva
    def sumar(self, lista):
        for i in range(self.length()):
            self.get(i).valor += lista.get(i).valor
        self.valor = self.__str__()
    def obtenerPatron(self):
        listaPatron = Lista()
        for i in range(self.length()):
            if(self.get(i).valor > 0):
                listaPatron.agregar(Nodo(1))
            else:
                listaPatron.agregar(Nodo(0))
        return listaPatron
