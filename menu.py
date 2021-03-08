import os
from xml.dom import minidom
from nodo import Nodo
from lista import Lista
from matriz import Matriz
from graphviz import Digraph
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

        
            lista.agregar(Nodo(valor))
            if valor_y == y:
                #print(lista)
                lista_matrices[contador_fin_matriz].agregar(lista)
                lista = Lista()

        contador_fin_matriz += 1

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
def mostrarDatos():

    print('\nRodrigo Antonio Porón De León\n201902781\nIntroducción a la Programación y Computación 2 Sección "C"')
    print('Ingeniería en Ciencias y Sistemas\n4to Semestre\n')

def mostrarMatrices():
    for i in range(lista_matrices.length()):
        print('{}.- {}'.format(i+1, lista_matrices[i].nombre))
    
    matriz_seleccionada = int(input('Seleccione el No. de la matriz a graficar: ')) - 1
    #print(f'La matriz que seleccionó es: {lista_matrices[matriz_seleccionada]}')
    #print(f'm es: {lista_matrices[matriz_seleccionada].m} y n es: {lista_matrices[matriz_seleccionada].n}')

    generarGrafica(lista_matrices[matriz_seleccionada])

def generarGrafica(matriz):
    
    """with open("grafo-salida.dot", mode="w") as f:
        f.write("digraph Matrices{\n")
        f.write(f"Matrices -> {matriz.nombre};\n")
        f.write(f"{matriz.nombre} -> n;\n")
        f.write(f"{matriz.nombre} -> m;\n")
        f.write(f"n [label=\"n={matriz.n}\"];\n")
        f.write(f"m [label=\"m={matriz.m}\"];\n")
        for i in range(matriz.get_m()):
            print(f'la dimension de la fila es: {matriz.get_m()}')
            for j in range(matriz.get_n()):
                if j == 0:
                    f.write(f"{matriz.nombre} -> \"({i}, {j}): {matriz[i][j]}\";\n")
                else:
                    f.write(f'\"({i}, {j-1}): {matriz[i][j-1]}\" -> \"({i}, {j}): {matriz[i][j]}\";\n')
        f.write("}")
    os.system("dot -Tpng grafo-salida.dot -o salida.png")"""

    dot = Digraph()
    dot.node('P','Matrices')
    dot.node('Q',matriz.nombre)
    dot.edge('P','Q')
    dot.node('M','m={}'.format(str(matriz.m)))
    dot.node('N','n={}'.format(str(matriz.n)))
    dot.edge('Q','M')
    dot.edge('Q','N')

    for i in range(matriz.length()):
        for j in range(matriz[i].length()):
            dot.node(f'{i},{j}', f'{matriz.obtener_elem(i,j)}')
            if j == 0:
                #f.write(f"{matriz.nombre} -> \"({i}, {j}): {matriz[i][j]}\";\n")
                dot.edge('Q', f'{i},{j}')
            else:
                #f.write(f'\"({i}, {j-1}): {matriz[i][j-1]}\" -> \"({i}, {j}): {matriz[i][j]}\";\n')
                dot.edge(f'{i},{j-1}',f'{i},{j}')
    dot.render('grafo.gv', view=True)
    print('Grafo creado')



def cargarArchivo():
    global ruta 
    print('Opción Cargar Archivo')
    print('Ingrese la ruta del archivo:')
    ruta = input()
    return ruta

def escribirArchivo():
    ruta_salida = input('Escribir una ruta específica:')
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
    f = open(ruta_salida, "w")
    f.write(xml_parseado)
    f.close()
    print("El archivo xml con las matrices reducidas ha sido escrito")

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

        if opcion == 4:

            mostrarDatos()
                
        if opcion == 5:

            mostrarMatrices()

        elif opcion == 6:
            salir = True

