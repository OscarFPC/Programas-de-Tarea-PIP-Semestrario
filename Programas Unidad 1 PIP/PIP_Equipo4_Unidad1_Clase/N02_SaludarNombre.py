import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N02_SaludarNombre.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_saludar.clicked.connect(self.ejecutarSaludo)

    #Area de los Slots
    def ejecutarSaludo(self):
        nombre = self.txt_nombre.text()#regresa str
        #n = int(self.txt_nombre.text())
        #n**=2
        #self.saludar(f'No. {str(n)} ')
        self.saludar(f'Hola'+ nombre)

    def saludar(self, nombre):
        m = QtWidgets.QMessageBox()
        m.setText(f'Hola {nombre} :D')
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())