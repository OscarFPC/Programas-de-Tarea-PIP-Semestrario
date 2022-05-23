import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N06_CambioColor_Slider.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.horizontalSlider1.setMaximum(255)
        self.horizontalSlider1.setMinimum(0)
        self.horizontalSlider1.setSingleStep(1)
        self.horizontalSlider1.setValue(0)
        self.horizontalSlider1.valueChanged.connect(self.cambio)
        self.horizontalSlider2.setMaximum(255)
        self.horizontalSlider2.setMinimum(0)
        self.horizontalSlider2.setSingleStep(1)
        self.horizontalSlider2.setValue(0)
        self.horizontalSlider2.valueChanged.connect(self.cambio)
        self.horizontalSlider3.setMaximum(255)
        self.horizontalSlider3.setMinimum(0)
        self.horizontalSlider3.setSingleStep(1)
        self.horizontalSlider3.setValue(0)
        self.horizontalSlider3.valueChanged.connect(self.cambio)
        self.btn_r.setEnabled(False)
        self.btn_g.setEnabled(False)
        self.btn_b.setEnabled(False)
    #Area de los Slots
    def cambio(self):
        r = self.horizontalSlider1.value()
        g = self.horizontalSlider2.value()
        b = self.horizontalSlider3.value()
        self.btn_r.setText(f'R: {r}')
        self.btn_g.setText(f'G: {g}')
        self.btn_b.setText(f'B: {b}')
        color = f"background-color: rgb({r}, {g}, {b});"
        self.dial.setStyleSheet(color)
        self.lbl_color.setStyleSheet(color)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())