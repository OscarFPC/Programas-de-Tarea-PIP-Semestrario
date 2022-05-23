import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N02_Cambio_UnidadesDeLongitud.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_numA.setEnabled(False)
        self.btn_tipo.setEnabled(False)
        self.horizontalSlider.setMinimum(self.minimo())
        self.horizontalSlider.setMaximum(self.maximo())
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.valueChanged.connect(self.cambiaValorHS)
        self.horizontalSlider.valueChanged.connect(self.convertir)
        self.btn_r.setEnabled(False)
        self.btn_r.clicked.connect(self.convertir)
        self.btn_r.clicked.connect(self.cambiaValorHS)
        self.unidades = ('KILOMETROS','METROS','CENTIMETROS','MILIMETROS','MILLAS','YARDAS','PIES','PULGADAS')
        #Area de Signals y configuraciones incicales
        self.comboBox1.addItems(self.unidades)
        self.comboBox1.setCurrentIndex(0)
        self.comboBox2.addItems(self.unidades)
        self.comboBox2.setCurrentIndex(1)
    #Area de los Slots
    def minimo(self):
        minimo = 0
        return minimo
    def maximo(self):
        maximo = 100
        return maximo
    def convertir(self):
        de = self.comboBox1.currentText()
        a = self.comboBox2.currentText()
        print(de, a)
        if (de == 'KILOMETROS'):
            if (a == 'METROS'):
                numA = int(self.btn_numA.text())
                result = numA * 1000
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'CENTIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 100000
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 1e+6
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILLAS'):
                numA = int(self.btn_numA.text())
                result = numA / 1.609
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'YARDAS'):
                numA = int(self.btn_numA.text())
                result = numA * 1094
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PIES'):
                numA = int(self.btn_numA.text())
                result = numA * 3281
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PULGADAS'):
                numA = int(self.btn_numA.text())
                result = numA * 39370
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
        #1
        if (de == 'METROS'):
            if (a == 'KILOMETROS'):
                numA = int(self.btn_numA.text())
                result = numA / 1000
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'CENTIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 100
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 1000
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILLAS'):
                numA = int(self.btn_numA.text())
                result = numA / 1609
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'YARDAS'):
                numA = int(self.btn_numA.text())
                result = numA * 1.094
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PIES'):
                numA = int(self.btn_numA.text())
                result = numA * 3.281
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PULGADAS'):
                numA = int(self.btn_numA.text())
                result = numA * 39.37
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
        #2
        if (de == 'CENTIMETROS'):
            if (a == 'KILOMETROS'):
                numA = int(self.btn_numA.text())
                result = numA / 100000
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'METROS'):
                numA = int(self.btn_numA.text())
                result = numA / 100
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 10
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILLAS'):
                numA = int(self.btn_numA.text())
                result = numA / 160934
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'YARDAS'):
                numA = int(self.btn_numA.text())
                result = numA / 91.44
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PIES'):
                numA = int(self.btn_numA.text())
                result = numA / 30.48
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PULGADAS'):
                numA = int(self.btn_numA.text())
                result = numA / 2.54
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
        #3
        if (de == 'MILIMETROS'):
            if (a == 'KILOMETROS'):
                numA = int(self.btn_numA.text())
                result = numA / 1e+6
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'METROS'):
                numA = int(self.btn_numA.text())
                result = numA / 1000
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'CENTIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA / 10
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILLAS'):
                numA = int(self.btn_numA.text())
                result = numA / 1.609e+6
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'YARDAS'):
                numA = int(self.btn_numA.text())
                result = numA /914
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PIES'):
                numA = int(self.btn_numA.text())
                result = numA / 305
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PULGADAS'):
                numA = int(self.btn_numA.text())
                result = numA / 25.4
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
        #4
        if (de == 'MILLAS'):
            if (a == 'KILOMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 1.609
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'METROS'):
                numA = int(self.btn_numA.text())
                result = numA * 1609
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'CENTIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 160934
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA / 1.609e+6
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'YARDAS'):
                numA = int(self.btn_numA.text())
                result = numA * 1760
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PIES'):
                numA = int(self.btn_numA.text())
                result = numA * 5280
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PULGADAS'):
                numA = int(self.btn_numA.text())
                result = numA * 63360
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
        #5
        if (de == 'YARDAS'):
            if (a == 'KILOMETROS'):
                numA = int(self.btn_numA.text())
                result = numA / 1094
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'METROS'):
                numA = int(self.btn_numA.text())
                result = numA / 1.094
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'CENTIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 91.44
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 914
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILLAS'):
                numA = int(self.btn_numA.text())
                result = numA / 1760
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PIES'):
                numA = int(self.btn_numA.text())
                result = numA * 3
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PULGADAS'):
                numA = int(self.btn_numA.text())
                result = numA * 36
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
        #6
        if (de == 'PIES'):
            if (a == 'KILOMETROS'):
                numA = int(self.btn_numA.text())
                result = numA / 3281
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'METROS'):
                numA = int(self.btn_numA.text())
                result = numA / 3.281
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'CENTIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 30.48
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 305
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILLAS'):
                numA = int(self.btn_numA.text())
                result = numA / 5280
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'YARDAS'):
                numA = int(self.btn_numA.text())
                result = numA / 3
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PULGADAS'):
                numA = int(self.btn_numA.text())
                result = numA * 12
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
        #7
        if (de == 'PULGADAS'):
            if (a == 'KILOMETROS'):
                numA = int(self.btn_numA.text())
                result = numA / 39370
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'METROS'):
                numA = int(self.btn_numA.text())
                result = numA * 39.37
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'CENTIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 2.54
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILIMETROS'):
                numA = int(self.btn_numA.text())
                result = numA * 25.4
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'MILLAS'):
                numA = int(self.btn_numA.text())
                result = numA / 63360
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'YARDAS'):
                numA = int(self.btn_numA.text())
                result = numA / 36
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)
            elif (a == 'PIES'):
                numA = int(self.btn_numA.text())
                result = numA / 12
                self.btn_numB.setText(str(result))
                self.btn_tipo.setText(a)

    def cambiaValorHS(self):
        valorA = self.horizontalSlider.value()
        minimo = self.minimo()
        maximo = self.maximo()
        print(minimo,maximo)
        self.btn_minimo.setText(str(minimo))
        self.btn_maximo.setText(str(maximo))
        self.btn_numA.setText(str(valorA))
        index1 = int(self.comboBox1.currentIndex())
        index2 = int(self.comboBox2.currentIndex())
        if index2 == index1:
            if(index1 < int(self.comboBox1.count())):
                aux = index1+1
                self.comboBox1.setCurrentIndex(aux)
            if(index1 > 0):
                aux = index1 - 1
                self.comboBox1.setCurrentIndex(aux)
        self.btn_r.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())