from xml.dom import minidom
from menu import cargarArchivo

def procesarArchivo():
    ruta = cargarArchivo()
    print(ruta)