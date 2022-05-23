import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N05_CAmbioDeColor_Semaforo.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.horizontalSlider.setMaximum(2)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.valueChanged.connect(self.cambio)
        self.dial_a.setStyleSheet("background-color: rgb(255, 255, 0);")


    #Area de los Slots
    def cambio(self):
        valor = self.horizontalSlider.value()
        if(valor==0):
            self.dial_v.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.dial_a.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.dial_r.setStyleSheet("background-color: rgb(0, 0, 0);")
        if (valor == 1):
            self.dial_v.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.dial_a.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.dial_r.setStyleSheet("background-color: rgb(255, 0, 0);")
        if (valor == 2):
            self.dial_v.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.dial_a.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.dial_r.setStyleSheet("background-color: rgb(0, 0, 0);")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())