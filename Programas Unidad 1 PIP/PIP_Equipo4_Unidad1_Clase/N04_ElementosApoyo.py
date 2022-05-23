import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N04_ElementosApoyo.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_enviar.clicked.connect(self.enviar)
        # Crear una copia de cada uno de los programas encargados la semana pasada y añadir en ellos
        # tres imagenes :  1.- Logo UAT  2.- Logo FIANS  3.- Logo Representativo del Equipo
        # y añadir tooltip, statustip y place holder

    #Area de los Slots
    def enviar(self):
        try:
            nombre = self.txt_nombre.text()
            self.mensaje(nombre)
        except Exception as e:
            print(f'Erro {e}')
        #message = QtWidgets.QMessageBox()
        #message.setText(f"Hola {nombre}")
        #message.exec()
    def mensaje(self, nombre):
        msj = QtWidgets.QMessageBox()
        msj.setText(f'Hola {nombre} :D')
        msj.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())