import sys
from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = 'N03_GradosCentigrados_Farenheit.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.dial.setMinimum(-50)
        self.dial.setMaximum(50)
        self.dial.setValue(0)
        self.dial.setSingleStep(1)
        self.dial.valueChanged.connect(self.cambio)
        self.dial.valueChanged.connect(self.cambioimg)
        ruta = 'C:/a/PIP_Equipo4_Unidad1_Tarea/imagenes'
        self.listimg = [f'{ruta}/frio.jpg',
                        f'{ruta}/fresco.jpg',
                        f'{ruta}/normal.jpg',
                        f'{ruta}/caluroso.jpg']

    #Area de los Slots
    def cambio(self):
        valor = self.dial.value()
        f = (valor*(9/5))+32
        self.txt_c.setText(str(valor))
        self.txt_f.setText(str(round(f)))
    def cambioimg(self):
        valor = self.dial.value()
        if (valor <= 10):
            self.img.setPixmap(QtGui.QPixmap(self.listimg[0]))
        if (valor > 10 and valor <= 15):
            self.img.setPixmap(QtGui.QPixmap(self.listimg[1]))
        if (valor > 15 and valor <= 27):
            self.img.setPixmap(QtGui.QPixmap(self.listimg[2]))
        if (valor > 27 and valor <= 50):
            self.img.setPixmap(QtGui.QPixmap(self.listimg[3]))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())