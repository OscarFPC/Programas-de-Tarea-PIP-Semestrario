#Degradar color cada segundo 000 - FFF
import sys

from PyQt5 import uic, QtWidgets,QtGui, QtCore

qtCreatorFile = 'N19_DegradarColorPorSegundo.ui' #Nombre del archivo aqui

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
        self.btn_elegir.setEnabled(False)
        self.btn_cambiar.setEnabled(False)
        self.btn_elegir.clicked.connect(self.elegir)
        self.btn_cambiar.clicked.connect(self.cambiar)
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setEnabled(False)
        self.verticalSlider.valueChanged.connect(self.degradado)
        self.btn_degradar.clicked.connect(self.iniciardegradadoS)
        self.btn_degradar.setVisible(False)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)
        self.valor = 0
    #Area de los Slots
    def iniciardegradadoS(self):
        self.btn_degradar.setEnabled(False)
        self.valor = self.aux
        self.verticalSlider.setValue(self.valor)
        self.valor -= 1
        self.segundoPlano.start(100)
    def temporizador(self):
        self.verticalSlider.setValue(self.valor)
        self.valor -= 1
        if self.valor == -1:
            self.segundoPlano.stop()
            self.btn_degradar.setVisible(False)
            self.horizontalSlider1.setValue(0)
            self.horizontalSlider2.setValue(0)
            self.horizontalSlider3.setValue(0)
    def cambio(self):
        self.btn_elegir.setEnabled(True)
        r = self.horizontalSlider1.value()
        g = self.horizontalSlider2.value()
        b = self.horizontalSlider3.value()
        self.btn_r.setText(f'R: {r}')
        self.btn_g.setText(f'G: {g}')
        self.btn_b.setText(f'B: {b}')
        color = f"background-color: rgb({r}, {g}, {b});"
        self.dial.setStyleSheet(color)
        self.lbl_color.setStyleSheet(color)
    def elegir(self):
        self.btn_degradar.setVisible(True)
        self.btn_degradar.setEnabled(True)
        self.btn_elegir.setEnabled(False)
        self.horizontalSlider1.setEnabled(False)
        self.horizontalSlider2.setEnabled(False)
        self.horizontalSlider3.setEnabled(False)
        numbers = self.guardado()
        max_value = None
        for num in numbers:
            if (max_value is None or num > max_value):
                max_value = num
        self.verticalSlider.setValue(max_value)
        #self.verticalSlider.setEnabled(True)
        self.btn_cambiar.setEnabled(True)
        self.aux = max_value
    def cambiar(self):
        self.btn_elegir.setEnabled(True)
        self.btn_cambiar.setEnabled(False)
        self.horizontalSlider1.setEnabled(True)
        self.horizontalSlider2.setEnabled(True)
        self.horizontalSlider3.setEnabled(True)
        self.verticalSlider.setValue(0)
        self.verticalSlider.setEnabled(False)
        self.cambio()
    def degradado(self):
        self.btn_elegir.setEnabled(False)
        r = self.horizontalSlider1.value()
        g = self.horizontalSlider2.value()
        b = self.horizontalSlider3.value()
        numbers = [r, g, b]
        max_value = None
        for num in numbers:
            if (max_value is None or num > max_value):
                max_value = num
        aux = 0
        for ele in numbers:
            try:
                numbers[aux] = round(max_value/ele)
            except Exception as e:
                numbers[aux] = 1
            aux += 1
        if(self.verticalSlider.value()>max_value and self.verticalSlider.value()<255):
            if (r != 0):
                r = r + numbers[0]
            if (g != 0):
                g = g + numbers[1]
            if (b != 0):
                b = b + numbers[2]
            print('suma ', r, g, b)
        elif(self.verticalSlider.value()<max_value and self.verticalSlider.value()>0):
            if (r != 0):
                r = r - numbers[0]
            if (g != 0):
                g = g - numbers[1]
            if (b != 0):
                b = b - numbers[2]
            print('resta ', r, g, b)
        self.horizontalSlider1.setValue(r)
        self.horizontalSlider2.setValue(g)
        self.horizontalSlider3.setValue(b)
    def guardado(self):
        r = self.horizontalSlider1.value()
        g = self.horizontalSlider2.value()
        b = self.horizontalSlider3.value()
        guardado = [r,g,b]
        return guardado
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())