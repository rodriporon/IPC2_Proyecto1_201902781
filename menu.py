from tqdm.auto import tqdm
from time import sleep
from xml.dom import minidom
from nodo import Nodo
from lista import Lista
from matriz import Matriz

from xml.etree.ElementTree import TreeBuilder, parse


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

    tree = parse(ruta)

    nombre_matrices = Lista()
    m_matrices = Lista()
    n_matrices = Lista()

    for node in tree.iter('matriz'):
        nombre = node.attrib.get('nombre')
        m = node.attrib.get('m')
        n = node.attrib.get('n')
        nombre_matrices.add(Nodo(nombre))
        m_matrices.add(Nodo(m))
        n_matrices.add(Nodo(n))

    print(nombre_matrices[0])
            

    
    
    """for i in tqdm(range(len(root))):
        print(" ", end='\r')"""
            
    """for elem in root:
        for subelem in elem:
            print(subelem.text)"""

                
    print('\n Realizando suma de tuplas...')
            


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

