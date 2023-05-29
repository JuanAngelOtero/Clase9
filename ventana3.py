from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication, QToolBar, QAction
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from cliente import Cliente
import sys

class Ventana3(QMainWindow):

    # hacer el metodo de contrucción de la ventana
    def __init__(self, anterior):
        super(Ventana3, self).__init__(anterior)

        # creamos un atributo que guarde la ventana anterior
        self.ventanaAnterior = anterior

        # poner el titulo:
        self.setWindowTitle("Usuarios Registrados")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/bag.jpg'))

        # Establecemos las propiedade de ancho y alto:
        self.ancho = 1500
        self.alto = 700

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

        # abrimos el archivo en modo de lectura:
        self.file  = open('datos/clientes.txt', 'rb')

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

        # Establecemos la distribución de los elementos en layout vertical:
        self.vertical = QVBoxLayout()

        #---- CONSTRIR EL MENÚ TOOLBAR ---
        self.toolbar = QToolBar('Main toolbar')
        self.toolbar.setIconSize(QSize(40, 40))
        self.addToolBar(self.toolbar)

        #-- delete --
        self.delete = QAction(QIcon('imagenes/delete.png'), '&Delete', self)
        self.delete.triggered.connect(self.accion_delete)
        self.toolbar.addAction(self.delete)

        # -- add --
        self.add = QAction(QIcon('imagenes/add.png'), '&Add', self)
        self.add.triggered.connect(self.accion_add)
        self.toolbar.addAction(self.add)

        # -- delete --
        self.insert = QAction(QIcon('imagenes/edit.png'), '&Insert', self)
        self.insert.triggered.connect(self.accion_insert)
        self.toolbar.addAction(self.insert)

        #----FIN MENÚ TOOLBAR -----


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

        # hacemos que el scroll se adapte a diferentes tamaños:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una tabla:
        self.tabla = QTableWidget()

        # Definimos el número de columnas que tendrá la tabla:
        self.tabla.setColumnCount(11)

        # Definimos el ancho de cada columna:
        self.tabla.setColumnWidth(0, 160)
        self.tabla.setColumnWidth(1, 160)
        self.tabla.setColumnWidth(2, 160)
        self.tabla.setColumnWidth(3, 160)
        self.tabla.setColumnWidth(4, 160)
        self.tabla.setColumnWidth(5, 160)
        self.tabla.setColumnWidth(6, 160)
        self.tabla.setColumnWidth(7, 160)
        self.tabla.setColumnWidth(8, 160)
        self.tabla.setColumnWidth(9, 160)
        self.tabla.setColumnWidth(10, 160)

        # Definimos el texto de la cabecera de la tabla:
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Password',
                                              'Documento',
                                              'Correo',
                                              'pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3',])

        # Establecemos el número de filas:
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla:
        for u in self.usuarios:
            self.tabla.setItem(self.contador,0, QTableWidgetItem(u.nombreCompleto))
            # hacemos que el nombre no se oueda editar
            self.tabla.item(self.contador, 0).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            # hacemos que el documento no se oueda editar
            self.tabla.item(self.contador, 3).setFlags(Qt.ItemIsEnabled)
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        # Metemos la tabla en el scroll:
        self.scrollArea.setWidget(self.tabla)

        # Metodos en el layout vertical el scroll:
        self.vertical.addWidget(self.scrollArea)

        # Ponemos un espacio depúes:
        self.vertical.addStretch()

        # ------------ BOTON VOLVER --------------

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

        # Metemos el layout vertical el botonVolver:
        self.vertical.addWidget(self.botonVolver)

        # -------- OJO IMPORTANTE PONER AL FINAL ----------

        # indicamos que el layout pricipal fondo es horizontal:
        self.fondo.setLayout(self.vertical)

    def metodo_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def accion_delete(self):
        pass
    def accion_add(self):
        pass
    def accion_insert(self):
        pass





if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana3 = Ventana3()

    ventana3.show()

    sys.exit(app.exec_())




