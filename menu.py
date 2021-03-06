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

    global lista_matrices, lista_matrices_binarias, lista_matrices_reducidas
    lista_matrices_binarias = Lista()
    lista_matrices_reducidas = Lista()
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
        
        lista_matrices_binarias.agregar(Matriz(m,n,nombre))
        lista_matrices.agregar(Matriz(m, n, nombre))

        #for i in node:
            #print(i.text)
        #print('....')

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
                #print(lista)
                lista_matrices[contador_fin_matriz].agregar(lista)
                lista = Lista()

        contador_fin_matriz += 1

    #print(lista_matrices[2].obtener_elem(4,4))

    
    
    """for i in tqdm(range(len(root))):
        print(" ", end='\r')"""
            
    """for elem in root:
        for subelem in elem:
            print(subelem.text)"""

    #print(lista_matrices)

    print('\n Realizando suma de tuplas...')

    #print(f"La lista de matrices que vienen en el xml tiene longitud: {lista_matrices.length()}")
    for i in range(lista_matrices.length()):
        matriz_binaria = lista_matrices_binarias.get(i)
        for j in range(lista_matrices[i].get_m()):
            listab = Lista()
            for k in range(lista_matrices[i].get_n()):
                if lista_matrices[i].obtener_elem(k,j) != 0:
                    listab.agregar(Nodo(1))
                else:
                    listab.agregar(Nodo(0))
            matriz_binaria.agregar(listab)


        matriz_original = lista_matrices.get(i)
        matriz_binaria = lista_matrices_binarias.get(i)
        matriz_reducida = Matriz(matriz_original.m, matriz_original.n, matriz_original.nombre + "_reducida")
        for j in range(lista_matrices[i].get_m()):
            fila_original = matriz_original.get(j)
            encontrada = False
            for k in range(matriz_reducida.length()):
                if(str(matriz_reducida.get(k).obtenerPatron()) == str(fila_original.obtenerPatron())):
                    encontrada = True
                    matriz_reducida.get(k).sumar(fila_original)
                    matriz_reducida.get(k).frecuencia += 1
            if(encontrada):
                continue
            else:
                fila_nueva = fila_original.clonar()
                fila_nueva.indice_frecuencia = j+1
                matriz_reducida.agregar(fila_nueva)
        lista_matrices_reducidas.agregar(matriz_reducida)

def buscarMatriz(buscar):
    for i in range(lista_matrices.length()):
        if lista_matrices[i].nombre == buscar:
            return i
        else:
            return 'No se encontró la matriz'


def cargarArchivo():
    global ruta 
    print('Opción Cargar Archivo')
    print('Ingrese la ruta del archivo:')
    ruta = input()
    return ruta

def escribirArchivo():
    et_raiz = ElementTree.Element("matrices")
    for i in range(lista_matrices_reducidas.length()):
        matriz_reducida = lista_matrices_reducidas.get(i)
        et_matriz = ElementTree.SubElement(et_raiz, "matriz",
            {"nombre": matriz_reducida.nombre, "m": str(matriz_reducida.length()), "n": str(matriz_reducida.n)
        })
        for j in range(matriz_reducida.length()):
            fila_reducida = matriz_reducida.get(j)
            for k in range(fila_reducida.length()):
                et_dato = ElementTree.SubElement(et_matriz, "dato", {"x": str(j+1), "y": str(k+1)})
                et_dato.text = str(fila_reducida.get(k).valor)
        for j in range(matriz_reducida.length()):
            fila_reducida = matriz_reducida.get(j)
            et_frecuencia = ElementTree.SubElement(et_matriz, "frecuencia", {
                "g": str(fila_reducida.indice_frecuencia)
            })
            et_frecuencia.text = str(fila_reducida.frecuencia)
    xml_matrices = ElementTree.tostring(et_raiz, 'utf-8')
    xml_parseado = minidom.parseString(xml_matrices).toprettyxml(indent="\t")
    f = open("salida.xml", "w")
    f.write(xml_parseado)
    f.close()
    print("El xml con las matrices reducidas ha sido escrito")

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

        if opcion == 3:

            escribirArchivo()
                

        elif opcion == 6:
            salir = True

