#8. Convertir de un numero decimal a binario
import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N16_DecimalABinario.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        validarN = QtGui.QIntValidator()
        self.txt_numero.setValidator(validarN)
        self.txt_binario.setEnabled(False)
        self.btn_convertir.clicked.connect(self.conversion)

    #Area de los Slots
    def conversion(self):
        decimal = int(self.txt_numero.text())
        binario = format(decimal, "b")
        self.txt_binario.setText(str(binario))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())