import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class grafo(QWidget):
    """
    Clase realizada para una segunda interfaz donde se muestran el grafo generado apartir del JSON
    """
    def __init__(self,json_grafo):
        super().__init__()
 
        # Crear una escena y un view para el grafo
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setWindowTitle('Grafo generado')
        self.view.setMinimumSize(QSize(700,700))    

        #Se convierte el JSON en un diccionario en python
        grafo = json.loads(json_grafo)
        lista_aristas = []

        #Se convierten las keys del diccionario en enteros para usarlos con las aristas
        nodos={}
        for clave,valor in grafo['vl'].items():
            new_key = int(clave)
            nodos[new_key]=valor


        # Se crean los nodos tomando las posiciones que tiene el JSON de las coordenadas x e y de los nodos
        for nodo, pos in grafo['vl'].items():
            x = pos['x']
            y = pos['y']
            radio = 20
            brush = QBrush(Qt.green)
            ellipse = QGraphicsEllipseItem(x - radio, y - radio, radio * 2, radio * 2)
            ellipse.setBrush(brush)
            self.scene.addItem(ellipse)
            # Se agregan aquí los numeros de los nodos que hay en el JSON (claves)
            text = QGraphicsTextItem(str(nodo))
            font = QFont()
            font.setPointSize(10)
            text.setFont(font)
            text.setPos(x - 5, y - 7)
            self.scene.addItem(text)
        
        #Se crea una lista de listas de las conexiones entre nodos
        for x,nodo in grafo['el'].items():
            lista_aristas.append([nodo['u'],nodo['v']])

        # Se crean las aristas tomando las coordenadas de origen entre los nodos
        pen = QPen(QColor("black"),2)
        for origen, destino in lista_aristas:
            x1 = nodos[origen]['x']
            y1 = nodos[origen]['y']
            x2 = nodos[destino]['x']
            y2 = nodos[destino]['y']
            line = QGraphicsLineItem(x1, y1, x2, y2)
            line.setPen(pen)
            # Función para colocar las líneas por debajo de los nodos
            line.setZValue(-1)
            self.scene.addItem(line)

        # Mostrar el view
        self.view.show()

