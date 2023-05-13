from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication
from PyQt5 import QtGui
import sys

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


        # Establecemos la distribución de los elementos en layout horizontal:
        self.vertical = QHBoxLayout()


        # -------- OJO IMPORTANTE PONER AL FINAL ----------

        # indicamos que el layout pricipal fondo es horizontal:
        self.fondo.setLayout(self.vertical)



if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())




