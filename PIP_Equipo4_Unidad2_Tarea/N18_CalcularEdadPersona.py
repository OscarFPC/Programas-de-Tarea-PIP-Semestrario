#10. Calcular la edad de una persona que es el doble de grande en edad que su hermano pequeño
# y su hermano pequeño tiene 5 años más que el de en medio,
# teniendo este último X años
import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N18_CalcularEdadPersona.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        validarN = QtGui.QIntValidator()
        self.txt_edadmediano.setValidator(validarN)
        self.txt_edadgrande.setEnabled(False)
        self.txt_fgrande.setEnabled(False)
        self.txt_edadpeque.setEnabled(False)
        self.txt_fpeque.setEnabled(False)
        self.btn_calcular.clicked.connect(self.calcular)

    #Area de los Slots
    def calcular(self):
        x = int(self.txt_edadmediano.text())
        self.txt_fpeque.setText(str(x))
        self.txt_edadpeque.setText(str(5+x))
        self.txt_fgrande.setText(f'(5 + {x})')
        self.txt_edadgrande.setText(str(2*(5+x)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())