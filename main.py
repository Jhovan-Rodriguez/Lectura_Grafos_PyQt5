"""
Alumno: Jorge Jhovan Rodriguez Moreno 2030295

Proyecto Individual Unidad 1

 Cuando se edita un grafo en el modulo TSP, permite la exportación en formato JSON. 
 El proyecto debe leer dicho grafo (de un cuadro de texto o de un archivo) y 
 desplegar el grafo correspondiente en un programa de PyQt5

"""

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
from grafo import *

class MainWindow(QMainWindow):

    """
    Creación de la interfaz inicial del programa.
    Interfaz donde se coloca el JSON para su generación. Grafo de la página VisualGO.
    """
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(700, 140))    
        self.setWindowTitle("Insertar JSON del grafo") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Ingrese JSON del grafo:')
        self.line = QLineEdit(self)

        self.line.move(200, 20)
        self.line.resize(400, 32)
        self.nameLabel.move(20, 20)
        self.nameLabel.resize(200,20)

        pybutton = QPushButton('Graficar', self)
        pybutton.clicked.connect(self.click)
        pybutton.resize(250,32)
        pybutton.move(270, 60)        

    def click(self):
        self.json=self.line.text()
        # Obtener el contenido del QLineEdit
        content = self.json
        # Intentar cargar el contenido como un objeto JSON
        try:
            json_object = json.loads(content)
        except json.JSONDecodeError:
            print("El contenido no es un objeto JSON válido")
            message_box = QMessageBox()
            message_box.setMinimumSize(QSize(300, 140))    
            message_box.setIcon(QMessageBox.Critical)
            # Establecer el texto del mensaje y el título
            message_box.setText("JSON inválido!")
            message_box.setWindowTitle("Error")

            # Establecer el tipo de botones que aparecerán
            message_box.setStandardButtons(QMessageBox.Ok)

            # Mostrar el QMessageBox y esperar a que el usuario haga clic en el botón Aceptar
            response = message_box.exec()
        else:
            self.w=grafo(self.json)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )

