from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QLineEdit, QApplication, \
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
import sys

from cliente import Cliente


class Ventana4(QMainWindow):
    # hacer el metodo de contrucción de la ventana
    def __init__(self,anterior,cedula):
        super(Ventana4, self).__init__(None)

        # creamos un atributo que guarde la ventana anterior
        self.ventanaAnterior = anterior

        self.cedulaUsuario = cedula

        # poner el titulo:
        self.setWindowTitle("editar usuario")

        # Poner el icono:
        self.setWindowIcon(QtGui.QIcon('imagenes/maldives.jpg'))

        # Establecemos las propiedade de ancho y alto:
        self.ancho = 1000
        self.alto = 800

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

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

        self.fondo.setStyleSheet("background-color: #FFDEAD;")

        # Establecemos la ventna fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribución de los elementos en layouthorizontal:
        self.horizontal = QHBoxLayout()

        # le ponemos las margenes:
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ------ LAYOUT IZQUIERDO -------
        # Creamos el layout del lado izquierdo:
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero:
        self.letrero1 = QLabel()

        # Le escribimos el texto:
        self.letrero1.setText("Editar Cliente")

        # Le asignamos el tipo de letra:
        self.letrero1.setFont(QFont("Times New Roman", 20))

        # le ponemos color de texto y margenes:
        self.letrero1.setStyleSheet("color: #FFFFFF"
                                    "background-color: #FF8C00;")

        # Agregamos el letrero en la  primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        #-------LETRERO 2 ---------
        # Hacemos el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(450)

        # Le escribimos el texto
        self.letrero2.setText("Por favor ingrese la información del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y margenes:
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
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        #Hacemos el campo para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos esto en el formulario:
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

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # Hacemos el campo para ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el documento:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

         # ------ BOTON EDITAR -----

        # Hacemos el boton para registrar los datos:
        self.botonEditar = QPushButton("Editar")

        # Establecemos el ancho del botón:
        self.botonEditar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonEditar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 10px;"
                                          )
        # Hacemos que el boton botonEditar tenga su metodo:
        self.botonEditar.clicked.connect(self.accion_botonEditar)

        # ------ BOTON LIMPIAR -----

        # Hacemos el boton para registrar los datos:
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del botón:
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )
        # Hacemos que el boton botonLimpiar tenga su metodo:
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        #Agregamos los dos botones al layaut ladoIzquierdo
        self.ladoIzquierdo.addRow(self.botonEditar, self.botonLimpiar)

        # ------ BOTON ELIMINAR -----

        # Hacemos el boton para registrar los datos:
        self.botonEliminar = QPushButton("Eliminar")

        # Establecemos el ancho del botón:
        self.botonEliminar.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonEliminar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )
        # Hacemos que el boton botonEliminar tenga su metodo:
        self.botonEliminar.clicked.connect(self.accion_botonEliminar)

        # Agregamos los dos botones al layaut ladoIzquierdo
        self.ladoIzquierdo.addRow(self.botonEliminar)

        # ------ BOTON Volver-----

        # Hacemos el boton para registrar los datos:
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del botón:
        self.botonVolver.setFixedWidth(90)

        # Le ponemos los estilos:
        self.botonVolver.setStyleSheet("background-color: #008B45;"
                                         "color: #FFFFFF;"
                                         "padding: 10px;"
                                         "margin-top: 10px;"
                                         )
        # Hacemos que el boton botonEliminar tenga su metodo:
        self.botonVolver.clicked.connect(self.accion_botonVolver)

        # Agregamos los dos botones al layaut ladoIzquierdo
        self.ladoIzquierdo.addRow(self.botonVolver)

        # Agregamos al layout izquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # --------- LAYOUT DERECHO ------------

        # Creamos un layout del lado derecho:
        self.ladoDerecho = QFormLayout()

        # Se asigna la margen solo a la izquierda de 100px:
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero:
        self.letrero3 = QLabel()

        # Le escribimos el texto:
        self.letrero3.setText("Editar Recuperar contraseña")

        # Le asignamos el tipo de letra:
        self.letrero3.setFont(QFont("Times New Roman", 15))

        # le ponemos color de texto y margenes:
        self.letrero3.setStyleSheet("color: #000080;"
                                    "background-color: # #FF8C00;")

        # Agregamos el letrero en la  primera fila:
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero:
        self.letrero4 = QLabel()

        # Establecemos el ancho del label:
        self.letrero4.setFixedWidth(400)

        # Le escribimos el texto
        self.letrero4.setText("Por favor ingrese la información para recuperar "
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra:
        self.letrero4.setFont(QFont("Andale Mono", 9))

        # Le ponemos color de texto y margenes:
        self.letrero4.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agrgamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.letrero4)

        # ----1

        # Hacemos el letrero de la pregunta 1:
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta1)

        # Hacemos el campo para ingresar la pregunta1:
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero de la respuesta 1:
        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta 1:
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta1)

        # ----2

        # Hacemos el letrero de la pregunta 2:
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta2:
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta2)

        # Hacemos el letrero de la respuesta 2:
        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta 2:
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta2)

        # ----3

        # Hacemos el letrero de la pregunta 3:
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta2:
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero de la respuesta 3:
        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta 3:
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta3)

        # ----

        # Agregamos el layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)

        # -------- OJO IMPORTANTE PONER AL FINAL ----------

        # indicamos que el layout pricipal fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

       # ------ Creamos la VENTANA DE DIALOGO: ----------
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Definimos el tamaño de la ventana:
        self.ventanaDialogo.resize(300, 150)

        # Creamos el botón para aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formuilario de registro")

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos es layout vertical:
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("")

        # Leponemos estilos al label mensaje:
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        # Agregamos el labbel mensaje:
        self.vertical.addWidget(self.mensaje)

        # Agregamos las obciones de los botones:
        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana:
        self.ventanaDialogo.setLayout(self.vertical)

        # Llamamos el metodo para que se carguen los datos del usuario  en el formulario:
        self.cargar_datos()

    def accion_botonEditar(self):
        # Variable para controlar que los datos se han ingresados corretos:
        self.datosCorreectos = True

        # establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de Edición ")

        # Validamos que los password sean iguales
        if (
                self.password.text() != self.password2.text()

        ):
            self.datosCorreectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Los password no son iguales")

            # Hacemos que la ventan de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Validamos que se ingresen todos los campos:
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorreectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Debe seleccionar un usuario con documento valido")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        # si los datos son correctos:
        if self.datosCorreectos:

            # abrimos los datos en forma de lectura:
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacia para guardar todos los usuarios:
            usuarios = []

            # Iteramos sobre el archivo linea por linea:
            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # Obtenemos del string una lista con 11 datos separados por ;
                lista = linea.split(";")
                print(lista)
                # se para si ya no hay mas registros en el archivo
                if linea == '':
                    break
                # Creamos un objeto de tipo cliente llamdo u
                # Y le pasamos los elementos de la lista:
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
                usuarios.append(u)

            # Cerramos el archivo:
            self.file.close()

            # En este punto ya tenemos la lista usuario con todos los usuarios:

            # variable para controlar si existe el documento:
            existeDocumento = False

            # Buscamos en la lista de usuario por usuario si existe la cedula:
            # es la cedula celeccionada de la ventana anterior:
            for u in usuarios:
                # compramos el documento ingresado:
                # si corresponde con el documento, es el usuario correcto:
                if int(u.documento) == self.cedulaUsuario:
                    # guardamos los datos delformulario en las propiedades del usuario:

                    u.usuario = self.usuario.text()
                    u.password = self.password.text()
                    u.correo = self.correo.text()
                    u.pregunta1 = self.pregunta1.text()
                    u.respuesta1 = self.respuesta1.text()
                    u.pregunta2 = self.pregunta2.text()
                    u.respuesta2 = self.respuesta2.text()
                    u.pregunta3 = self.pregunta3.text()
                    u.respuesta3 = self.respuesta3.text()
                    # Indicamos que encontramos el documento:
                    existeDocumento = True
                    # paramos el for
                    break

            # si no existe usuario con este documento:
            if (
                    not existeDocumento
            ):
                # Escribimos el texto explicativo
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + str(self.cedulaUsuario))

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()

            # Abrimos el archivo en modo agregar escribiendo datos en vinario.
            self.file = open('datos/clientes.txt', 'wb')

            # Recorremos la lista de usuarios .
            # Para guardar usuario por usuario en el archivo.
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))

            # Cerramos el archivo:
            self.file.close()

            # si  existe un usuario con este documento:
            # y si se editó correctamente:
            if (
                     existeDocumento
            ):
                # Escribimos el texto explicativo
                self.mensaje.setText("Usuarios actualizados correctamente!")


                # Hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.accion_botonVolver()

            self.file = open('datos/clientes.txt', 'rb')
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()



    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def accion_botonEliminar(self):
        # Variable para controlar que los datos se han ingresados corretos:
        self.datosCorreectos = True

        # controlamos si vamos a eliminar:
        self.eliminar = False

        # Validamos que se ingresen todos los campos:
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorreectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Debe seleccionar un usuario con documento valido:")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

        # si los datos estan correctos:
        if self.datosCorreectos:


            # ------ Creamos la VENTANA DE DIALOGO: ----------
            self.ventanaDialogoEliminar = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

            # Definimos el tamaño de la ventana:
            self.ventanaDialogoEliminar.resize(300, 150)

            # Configuramos la ventana para que sea modal:
            self.ventanaDialogoEliminar.setWindowModality(Qt.ApplicationModal)

            # Creamos es layout vertical:
            self.verticalEliminar = QVBoxLayout()

            # Creamos un label para los mensajes:
            self.mensajeEliminar = QLabel("¿Estas seguro que deseas eliminar este registro de usuario?")

            # Leponemos estilos al label mensaje:
            self.mensajeEliminar.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

            # agregamos el lavel de mensajes:
            self.verticalEliminar.addWidget(self.mensajeEliminar)

            #Agregamos las opciones de aceptar y cancelar en la ventana de dialogo
            self.opcionesEliminar = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            self.opcionesBox = QDialogButtonBox(self.opcionesEliminar)

            self.opcionesBox.accepted.connect(self.ok_opcion)
            self.opcionesBox.rejected.connect(self.cancel_opcion)

            # agregamos las obciones de los botones:
            self.verticalEliminar.addWidget(self.opcionesBox)

            # establecemos el layout para la ventana.
            self.ventanaDialogoEliminar.setLayout(self.verticalEliminar)

            # hacemos que la ventana de dialogo se vea:
            self.ventanaDialogoEliminar.exec_()

        if self.eliminar:
            # Abrimos el archivo en modo lectura:
            self.file = open('datos/clientes.txt', 'rb')

            # Lista vacia para guardar todos los usuarios:
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # Obtenemos del string una lista con 11 datos separados por ;
                lista = linea.split(";")
                print(lista)
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
                usuarios.append(u)

            # Cerramos el archivo:
            self.file.close()

            # En este punto ya tenmos la lista usuarios con todos los ususarios:

            # variable para controlar si existe el documento:
            existeDocumento = False

            # Buscamos en la lista de usuario si existe la cedula:
            for u in usuarios:
                # comparamos el documento ingresado:
                # si corresponde con el docuimento, es el usuario correcto:
                if int(u.documento) == self.cedulaUsuario:
                    # eliminamos el usuario de lalista de usuarios:
                    usuarios.remove(u)
                    existeDocumento = True
                    # paramos el for:
                    break

            # Abrimos el archivo en modo agregar escribiendo datos en vinario.
            self.file = open('datos/clientes.txt', 'wb')

            # Recorremos la lista de usuarios .
            # Para guardar usuario por usuario en el archivo.
            for u in usuarios:
                self.file.write(bytes(u.nombreCompleto + ";"
                                      + u.usuario + ";"
                                      + u.password + ";"
                                      + u.documento + ";"
                                      + u.correo + ";"
                                      + u.pregunta1 + ";"
                                      + u.respuesta1 + ";"
                                      + u.pregunta2 + ";"
                                      + u.respuesta2 + ";"
                                      + u.pregunta3 + ";"
                                      + u.respuesta3, encoding='UTF-8'))


            self.file.close()


            # si se encontro un usuraio con este documento y se ha eliminado:
            if (
                    existeDocumento
            ):
                # Escribimos el texto explicativo
                self.mensaje.setText("Usuarios eliminado exitosamente!")

                # Hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

                self.accion_botonLimpiar()

                self.accion_botonVolver()


    def ok_opcion(self):
        self.ventanaDialogoEliminar.close()
        self.eliminar = True

    def cancel_opcion(self):
        self.ventanaDialogoEliminar.close()

    def accion_botonVolver(self):
        self.hide()
        self.ventanaAnterior.show()

    def cargar_datos(self):
        # Abrimos el archivo en modo lectura
        self.file = open('datos/clientes.txt', 'rb')

        # Lista vacia para guardar todos los usuarios:
        usuarios = []

        # Interamos sobre el archivo linea por linea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # Obtenemos del string una lista con 11 datos separados por ;
            lista = linea.split(";")
            print(lista)
            # se para el wile si ya no hay mas registros en el archivo
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
            usuarios.append(u)

            # Cerramos el archivo:
        self.file.close()

        # En este punto ya tenmos la lista usuarios con todos los ususarios:

        # variable para controlar si existe el documento:
        existeDocumento = False

        # Buscamos en la lista de usuario por usuario si existe la cedula:
        # es la cedula celeccionada de la ventana anterior:
        for u in usuarios:
            # comparamos el documento ingresado:
            # si corresponde con el documento, es el usuario correcto :
            if int(u.documento) == self.cedulaUsuario:
                # mostramos lo datos en el formulario:
                self.nombreCompleto.setText(u.nombreCompleto)
                # hacemos que el nombre nose pueda editar:
                self.nombreCompleto.setReadOnly(True)
                self.usuario.setText(u.usuario)
                self.password.setText(u.password)
                self.password2.setText(u.password)
                self.documento.setText(u.documento)
                # Hacer que el documento no se pueda editar:
                self.documento.setReadOnly(True)
                self.correo.setText(u.correo)
                self.pregunta1.setText(u.pregunta1)
                self.respuesta1.setText(u.respuesta1)
                self.pregunta2.setText(u.pregunta2)
                self.respuesta2.setText(u.respuesta2)
                self.pregunta3.setText(u.pregunta3)
                self.respuesta3.setText(u.respuesta3)
                # Indicamos que encontramos el documento:
                existeDocumento = True
                # paramos el for:
                break

        # si no existe usuario con este documento:
        if (
                not existeDocumento
        ):
            # Escribimos el texto explicativo
            self.mensaje.setText("No existe un usuario con este documento:\n"
                                 + str(self.cedulaUsuario))

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            self.accion_botonVolver()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana4 = Ventana4()

    ventana4.show()

    sys.exit(app.exec_())








