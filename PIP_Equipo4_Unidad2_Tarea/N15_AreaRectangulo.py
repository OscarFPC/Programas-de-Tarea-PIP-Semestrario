#7.- Área de un Rectángulo
import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N15_AreaRectangulo.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        validarN = QtGui.QIntValidator()
        self.txt_altura.setValidator(validarN)
        self.txt_base.setValidator(validarN)
        self.txt_area.setEnabled(False)
        self.btn_area.clicked.connect(self.calcular)

    #Area de los Slots
    def calcular(self):
        base = int(self.txt_base.text())
        altura = int(self.txt_altura.text())
        area = base * altura
        self.txt_area.setText(str(area) + ' cm2')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())