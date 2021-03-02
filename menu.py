from os import lseek
from tqdm.auto import tqdm
from time import sleep
from xml.dom import minidom
from nodo import Nodo
from lista import Lista
from matriz import Matriz

from xml.etree import ElementTree


def verificarNumero():
 
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Seleccione una opción: "))
            correcto=True
        except ValueError:
            print('Error, introduzca un numero entero')
     
    return num

def procesarArchivo():

    print('\n Calculando la matriz binaria..')

    with open(ruta, 'rt') as f:
        tree = ElementTree.parse(f)


    lista_matrices = Lista()
    nombre_matrices = Lista()
    m_matrices = Lista()
    n_matrices = Lista()

    for node in tree.iter('matriz'):
        nombre = node.attrib.get('nombre')
        m = int(node.attrib.get('m'))
        n = int(node.attrib.get('n'))
        nombre_matrices.agregar(Nodo(nombre))
        m_matrices.agregar(Nodo(m))
        n_matrices.agregar(Nodo(n))
        
        lista_matrices.agregar(Matriz(m, n, nombre))

        for i in node:
            print(i.text)
        print('....')

    """for i in range(lista_matrices.length()):
        lista_matrices[i].add(n_matrices)"""
    contador_fin_matriz = 0
   
    lista = Lista()
    for node in tree.iter('matriz'):
        contador_y = 1
        contador_x = 1
        contador_elemento = 0
        termino_fila = False
        y = int(node.attrib.get('m'))
        x = int(node.attrib.get('n'))
        for i in node:
            valor_y = int(i.attrib.get('y'))
            valor_x = int(i.attrib.get('x'))
            valor = int(i.text)

            

            """print('Los valores son {} y {}'.format(contador_y, valor_y))
            if contador_x == x:
                print()
                print('Llegó al limite')
            if contador_y == valor_y and contador_x == valor_x:
                valor = int(i.text)
                lista.agregar(Nodo(valor))
                print('Lista sumando: {}'.format(lista))
            elif contador_y == (y + 1):
                lista_matrices[contador_fin_matriz].agregar(lista)
                lista = Lista()
                lista.agregar(Nodo(valor))
                print('El valor de contador_x: {}'.format(contador_x))
                contador_y = 1
                contador_x += 1


            contador_y += 1
        contador_x = 1    
        print('............................................ contador_x = {}'.format(contador_x))
        contador_fin_matriz += 1"""
        
            lista.agregar(Nodo(valor))
            if valor_y == y:
                print(lista)
                lista_matrices[contador_fin_matriz].agregar(lista)
                lista = Lista()

        contador_fin_matriz += 1

    print(lista_matrices[2].obtener_elem(4,4))

    """ node = tree.find('.//dato')
    print(node.tag) """



    
    
    """for i in tqdm(range(len(root))):
        print(" ", end='\r')"""
            
    """for elem in root:
        for subelem in elem:
            print(subelem.text)"""

    print(lista_matrices)

    print('\n Realizando suma de tuplas...')

    for i in range(lista_matrices.length()):
        for j in range(lista_matrices[i].get_m()):
            for k in range(lista_matrices[i].get_n()):
                if lista_matrices[i].obtener_elem(k, j) != 0:
                    print(1)
                else:
                    print(0)

        


def cargarArchivo():

    global ruta 
    print('Opción Cargar Archivo')
    print('Ingrese la ruta del archivo:')
    ruta = input()
    return ruta

def menuPrincipal():

    salir = False
    opcion = 0
 
    while not salir:
        print()
        print ("1. Cargar archivo")
        print ("2. Procesar archivo")
        print ("3. Escribir archivo salida")
        print ("4. Mostrar datos del estudiante")
        print ("5. Generar gráfica")
        print ("6. Salir")
 
        opcion = verificarNumero()

        if opcion == 1:

            cargarArchivo()

        if opcion == 2:

            procesarArchivo()
                

        elif opcion == 6:
            salir = True

