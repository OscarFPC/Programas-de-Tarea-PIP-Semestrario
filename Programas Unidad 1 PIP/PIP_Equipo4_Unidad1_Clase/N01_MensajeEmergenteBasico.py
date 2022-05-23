import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N01_MensajeEmergenteBasico.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_saludar.clicked.connect(self.saludar)

    #Area de los Slots
    def saludar(self):
        m = QtWidgets.QMessageBox()
        m.setText('Hola Mundo :D')
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())