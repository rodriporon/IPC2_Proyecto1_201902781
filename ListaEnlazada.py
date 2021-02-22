class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaCircularEnlazada:
    def __init__(self, head):
        self.head = head
        self.head.next = head

    def length(self):
        current = self.head.next
        count = 1
        if self.head is not None:
            while current != self.head:
                count += 1
                current = current.next
            return count
        else:
            return 0

    def search(self, position, prev=False):
        # Busca el elemento en la posición dada. Si position es negativo busca el último elemento
        # El argumento prev sirve para devolver en una lista tanto el nodo buscado como el anterior.
        if position == 0:
            if prev is False:
                return self.head
            else:
                return [self.search(-1), self.head]
        elif position < 0:
            current = self.head
            while current.next !=self.head:
                previous = current
                current = current.next
            return current if prev is False else [previous, current]
        else:
            k = 1
            current = self.head
            while k < position and current.next !=self.head:
                k += 1
                previous = current
                current = current.next
            return current if prev is False else [previous, current]

    def insert(self, node, position):
        # Inserta el nodo después de la posición indicada. Si se indica una posición negativa, o mayor que
        # el tamaño de la lista, se inserta al final
        if position == 0:
            last_element = self.search(-1)
            last_element.next = node
            node.next = self.head
            self.head = node
        elif position < 0:
            last_element = self.search(-1)
            last_element.next = node
            node.next = self.head
        else:
            element = self.search(position)
            node.next = element.next
            element.next = node

    def delete(self, position):
        # Para posiciones con valor negativo, borra el último nodo
        if position > 1:
            previous = self.search(position-1)
        elif position < 0:
            previous = self.search(-1, True)[0]
        else:
            previous = self.search(-1)
            self.head = previous.next.next
        previous.next = previous.next.next  


c_list = ListaCircularEnlazada()
for i in range(15):
    c_list.insert(Node(i), i)



print(c_list.head.data)
current = c_list.head.next
while current is not c_list.head:
    print(current.data)
    current = current.next