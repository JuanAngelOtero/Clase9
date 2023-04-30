import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
from PyQt5 import QtGui


class Ventana1(QMainWindow):

    # hacer el metodo de contrucción de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # Poner el titulo:
        self.setWindowTitle("Formulario de registro")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/bag.jpg'))

        # Establecemos las propiedade de ancho y alto:
        self.ancho = 1000
        self.alto = 700

        # establecemos el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro  = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # fijamos el ancho y alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal:
        self.fondo = QLabel(self)

        # Definimos la imagen de fondo:
        self.imagenFondo = QPixmap('imagenes/maldives.jpg')

        # Definimos la imagen de fondo:
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen:
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte al tamaño de la imagen:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos en layout horizontal:
        self.horizontal = QHBoxLayout()
        # Le ponemos la margenes:
        self.horizontal.setContentsMargins(30,30,30,30)

        # --------- LAYOUT IZQUIERDO ------------

        # Creamos un layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Información del cliente")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Times New Roman",20))

        # le ponemos color de texto y margenes:
        self.letrero1.setStyleSheet("color: #000080")

        # Agregamos el letrero en la  primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(450)

        # Le escribimos el texto
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\nconasterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero2.setFont(QFont("Andale Mono", 10))

        #Le ponemos color de texto y margenes:
        self.letrero2.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agrgamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)

        # Hacemos el campo para ingresar el nombre:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre Completo*",self.nombreCompleto)

        # Hacemos el campo para ingresar el Usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar el password:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario.
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Hacemos un botón para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del botón:
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el boton para limpiar los datos:
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del botón:
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al layout ladoizquierdo:
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)




        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # -------- OJO IMPORTANTE PONER AL FINAL ----------

        # indicamos que el layout pricipal fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

    # Método del botonlimpiar:
    def accion_botonLimpiar(self):
        pass

    # Método del botonRegistrar
    def accion_botonRegistrar(self):
        pass

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())



