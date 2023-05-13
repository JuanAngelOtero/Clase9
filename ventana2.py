import math

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QVBoxLayout, QScrollArea, \
    QWidget, QGridLayout, QButtonGroup, QPushButton
from PyQt5 import QtGui
import sys

from cliente import Cliente
from ventana3 import Ventana3


class Ventana2(QMainWindow):
    # hacer el metodo de contrucción de la ventana
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        # creamos un atributo que guarde la ventana anterior
        self.ventanaanterior = anterior

        # poner el titulo:
        self.setWindowTitle("Usuarios Registrados")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/maldives.jpg'))

        # Establecemos las propiedade de ancho y alto:
        self.ancho = 1000
        self.alto = 800

        # establecemos el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # fijamos el ancho y alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos elfondo principal:
        self.fondo = QLabel(self)


        # Definimos la imagen de fondo:
        self.imagenFondo = QPixmap('imagenes/fondo-ven2.jpg')

        # Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)


        # Hacemos que se adapte al tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)


        # Establecemos la distribución de los elementos en layout vertical:
        self.vertical = QVBoxLayout()

        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Times New Roman", 20))

        # le ponemos color de texto y margenes:
        self.letrero1.setStyleSheet("color: #000080")

        # Agregamos el letrero en la  primera fila:
        self.vertical.addWidget(self.letrero1)

        # ponemos un espacio despues:
        self.vertical.addStretch()

        # creamos un scroll:
        self.scrollArea = QScrollArea()

        # le ponemos el fondo al scroll
        self.scrollArea.setStyleSheet("background-color: transparent;")


        # hacemos que el scroll se adapte a diferentes tamaños:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una ventana contenedora para cada celda:
        self.contenedora = QWidget()

        # vamos a crear un layout de grid para poner una cuadricula de elementos:
        self.cuadricula = QGridLayout(self.contenedora)

        # metemos en la ventna contenedora el scroll:
        self.scrollArea.setWidget(self.contenedora)

        # metemos en el layout vertical el scroll:
        self.vertical.addWidget(self.scrollArea)

        # Abrimos el archivo en modo lectura
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacia para guardar todos los usuarios:
        self.usuarios = []

        # recorremos el archivo linea por linea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # Obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            # se para si ya no hay mas registros en el archivo
            if linea == '':
                break
            # Creamos un objeto de tipo cliente llamdo u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10]
            )
            # Metemos el objeto en la lista de ususarios:
            self.usuarios.append(u)

        # Cerramos el archivo:
        self.file.close()

        # En este punto ya tenmos la lista usuarios con todos los ususarios:

        # obtenemos el numero de ususarios registrados:
        # consultamos el tamaño de la lista usuarios:
        self.numeroUsuarios = len(self.usuarios)

        # contador de elementos para controlar los usuarios en la lista usuarios.
        self.contador = 0

        # definimos la cantidad de elementos a mostrar por columna:
        self.elementosPorColumna = 3

        # calculamos el numero de filas.
        # Redondeamos al entero superior +1, dividimos por elementosPorColumna:
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        # controlamos todos los botones por una variable:
        self.botones = QButtonGroup()

        # definimos que controlardor de los botones
        # debe agrupar a todos los botones internos:
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                # validamos que estan ingresado la cantidad e usuarios correctos.
                if self.contador < self.numeroUsuarios:

                    # En cada selda de la cuadricula va una ventana:
                    self.ventanaAuxiliar = QWidget()

                    # sde determina su ancho y su alto:
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # cramos el layout vertical para cada elemento de la cuadricula:
                    self.verticalCuadricula = QVBoxLayout()

                    # Creamos un botón por cada usuario mostrando sui cedula:
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    # establecemos el ancho del boton:
                    self.botonAccion.setFixedWidth(150)

                    # Le ponemos los estilos:
                    self.botonAccion.setStyleSheet("background-color: #008B45;"
                                                      "color: #FFFFFF;"
                                                      "padding: 10px;"
                                                      )

                    # metemos el boton el en el layout vertical para que se vea:
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo, con su cedula como id:
                    self.botones.addButton(self.botonAccion,int(self.usuarios[self.contador].documento))

                    # agregamos un espacio en blanco:
                    self.verticalCuadricula.addStretch()

                    # A la ventana le asignamos el layout vertical:
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # A la cuadricula le agregamos la ventana em la fila y columna actual:
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    # Aumentamos el contador:
                    self.contador += 1

        # ------ BOTON VOLVER -----

        # Hacemos el boton para pasar a la siguiente ventana:
        self.botonFormaTabular = QPushButton("Forma Tabular")

        # Establecemos el ancho del botón:
        self.botonFormaTabular.setFixedWidth(150)

        # Le ponemos los estilos:
        self.botonFormaTabular.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )

        # Hacemos que el boton botonForomaTabular tenga su metodo:
        self.botonFormaTabular.clicked.connect(self.metodo_botonFormaTabular)

        # Metemos el layout vertical el botonTabular:
        self.vertical.addWidget(self.botonFormaTabular)


        # ------ BOTON VOLVER -----

        # Hacemos el boton para pasar a la siguiente ventana:
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del botón:
        self.botonVolver.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonVolver.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 10px;"
                                          )
        # Hacemos que el boton botonContinuar tenga su metodo:
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        #Metemos el layout vertical el botonVolver:
        self.vertical.addWidget(self.botonVolver)









        # -------- OJO IMPORTANTE PONER AL FINAL ----------

        # indicamos que el layout pricipal fondo es horizontal:
        self.fondo.setLayout(self.vertical)

    # metodo para controlar las acciones de los botones:
    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaanterior.show()

    def metodo_botonFormaTabular(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()







if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())




