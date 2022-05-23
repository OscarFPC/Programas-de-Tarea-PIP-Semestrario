import sys, random

from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "N25_ProyectoPicasYFijas.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals y Configuraciones Iniciales

        #INFORMACION SOBRE LOS PRIMEROS PASOS PARA COMENZAR A JUGAR
        QMessageBox.information(self, '\tImportante', '🎰 Picas y Fijas 🎰\n\n'
                                                      '🔴 Ingresa nombre del jugador\n\n'
                                                      '🔴 Ingresa la cantidad de intentos en el cual crees adivinar el número\n\n'
                                                      '🔴 Selecciona tu avatar\n\n'
                                                      '🔴 Finalmente dale al botón Comenzar, es importante seguir estos pasos o no podrás comenzar a jugar')
        self.Btn_Comenzar.clicked.connect(self.Comenzar)
        self.Btn_Go.clicked.connect(self.GO)

        self.dial.setEnabled(False)
        self.Btn_Go.setEnabled(False)
        self.Btn_Comenzar.setEnabled(False)
        #####################################################################
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)
        self.segundos = 0
        self.minutos = 0
        #####################################################################
        self.dial.setMinimum(1234)
        self.dial.setMaximum(9876)
        self.dial.setSingleStep(1)
        self.dial.setValue(0)

        self.dial.valueChanged.connect(self.Numero)
        #####################################################################
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(9)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)

        self.horizontalSlider.valueChanged.connect(self.cambiaImagen)
        #####################################################################
        #LISTA DE IMAGENES PARA SELECCIONAR
        self.lista_imagenes = [":/imagenes/IMGs/PersonajesBrawhalla/Azoth.jpg",
                               ":/imagenes/IMGs/PersonajesBrawhalla/Bodvar.png",
                               ":/imagenes/IMGs/PersonajesBrawhalla/Diana.png",
                               ":/imagenes/IMGs/PersonajesBrawhalla/Dusk.png",
                               ":/imagenes/IMGs/PersonajesBrawhalla/Hattori.png",
                               ":/imagenes/IMGs/PersonajesBrawhalla/Magyar.png",
                               ":/imagenes/IMGs/PersonajesBrawhalla/Mordex.png",
                               ":/imagenes/IMGs/PersonajesBrawhalla/Nix.jpg",
                               ":/imagenes/IMGs/PersonajesBrawhalla/WuShang.png",
                               ":/imagenes/IMGs/PersonajesBrawhalla/Xull.png"
                               ]
        self.Et_Personaje.setPixmap(QtGui.QPixmap(self.lista_imagenes[0]))
        #####################################################################
    # Área de los Slots
    def Comenzar(self):
        #AQUI SE GUARDA EL NOMBRE Y LOS INTENTOS QUE INGRESO EL USUARIO, TIENE SELF PARA PODERSE UTILIZAR EN OTRAS FUNCIONES
        self.Nombre_Usuario = self.Txt_Nombre.text()
        self.Intento = self.Txt_Intentos.text()

        #CONDICION PARA QUE EL JUGADOR NO PUEDA COMENZAR SIN ANTES LLENAR LOS CAMPOS (NOMBRE E INTENTOS)
        if(self.Nombre_Usuario=="" or self.Intento==""):
            QMessageBox.information(self, '\tImportante','ES OBLIGATORIO LLENAR LOS CAMPOS')
        else:
            #INSTRUCCIONES DE COMO FUNCIONA EL JUEGO
            QMessageBox.information(self, '\tImportante','🎰 Estas apunto de comenzar a jugar Picas y Fijas 🎰\n\n'
                                                         '🔴 Debes ingresar un numero de 4 dígitos\n\n'
                                                         '🔴 EL juego te dira cuantos fueron fijas y cuantos picas\n\n'
                                                         '🔴 Fijas: Número correcto en la posición correcta\n\n'
                                                         '🔴 Picas: Número correcto en la posición incorrecta\n\n'
                                                         '🔴 El juego termina cuando se te acaben los intentos o cuando adivines el número\n\n'
                                                         '🔴 Con el dial colocas el numero que crees que es el correcto, no pongas 0 ni números repetidos"\n\n',QMessageBox.Ok)
            self.segundoPlano.start(1000)
            self.Txt_Nombre.setEnabled(False)
            self.Txt_Intentos.setEnabled(False)
            self.Btn_Comenzar.setEnabled(False)
            self.Btn_Comenzar.setEnabled(False)
            self.dial.setEnabled(True)
            self.Btn_Go.setEnabled(True)

            #AQUI SE GENERA UN NUMERO RANDOM 4 VECES(SIMULANDO UN NUMERO DE 4 DIGITOS) Y SE AGREGA A LA LISTA
            # CON LA CONDICION DE NO REPETIRSE, SELF.L TIENE LA LISTA DE LOS NUMEROS PARA ADIVINAR
            self.L = [random.randint(1, 9)]
            i = 1
            while i < 4:
                x = random.randint(1, 9)
                for j in range(0, len(self.L)):
                    if self.L[j] == x:
                        break
                else:
                    self.L.append(x)
                    i += 1

    def cambiaImagen(self):
        self.Btn_Comenzar.setEnabled(True)
        self.valor = self.horizontalSlider.value()
        self.Et_Personaje.setPixmap(QtGui.QPixmap(self.lista_imagenes[self.valor]))

    def Numero(self):
        global dial
        dial = self.dial.value()

        #SEPARA EN UNIDADES EL NUMERO INGRESADO CON EL DIAL
        u_m = int(dial / 1000)
        dial_1 = int(dial % 1000)
        c = int(dial_1 / 100)
        dial_2 = int(dial % 100)
        d = int(dial_2 / 10)
        u = int(dial_2 % 10)

        self.Et_1.setText(str(u_m))
        self.Et_2.setText(str(c))
        self.Et_3.setText(str(d))
        self.Et_4.setText(str(u))

        #AQUI SE GUARDA EL NUMERO DEL DIAL SEPARADOS EN UNA LISTA
        self.Num = [u_m, c, d, u]

    def temporizador(self):
        self.segundos += 1

        if (self.segundos == 60):
            self.minutos += 1
            self.segundos = 0

        self.lb_min.setText(str(self.minutos))
        self.lb_seg.setText(str(self.segundos))

    def GO(self):
        #ESTA PARTE SOLO ES DE DESMOSTRACION PARA VER QUE LAS DOS LISTAS ESTAN CREADAS CORRECTAMENTA(SE PUEDE BORRAR ESTO)
        #Lista generada con el dial (Linea 126)
        print(self.Num)
        #Numero Random --> Self.L (Linea 100)
        print(self.L)
        ###################################################################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle('Juego: Picas y Fijas')
    window.show()
    sys.exit(app.exec_())

