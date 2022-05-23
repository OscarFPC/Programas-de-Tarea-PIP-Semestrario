#5. Calcular la distancia recorrida (D) por una persona que tiene una velocidad constante (V) durante un cierto tiempo (T).
import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N13_DistanciaRecorrida.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        validarN = QtGui.QIntValidator()
        self.txt_velocidad.setValidator(validarN)
        self.txt_tiempo.setValidator(validarN)
        self.btn_calcular.clicked.connect(self.calcular)

    #Area de los Slots
    def calcular(self):
        distancia = int(self.txt_velocidad.text())*int(self.txt_tiempo.text())
        print(distancia)
        self.label_6.setText(f'Distancia recorrida: {distancia} m')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())