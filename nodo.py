class Nodo:
    def __init__(self, valor=None, anterior=None, siguiente=None):
        self.valor = valor
        self.anterior = anterior
        self.siguiente = siguiente 

    def __str__(self):
        resultado = ""
        if (self.valor):
            resultado += str(self.valor)
        else:
            resultado = "El nodo está vacío"
        if(self.anterior):
            resultado += "\nNodo anterior con valor: {}".format(self.anterior.valor)
        if(self.siguiente):
            resultado += "\nNodo siguiente con valor: {}".format(self.siguiente.valor)
        return resultado