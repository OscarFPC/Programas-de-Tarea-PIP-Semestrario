import sys
import math as m

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = 'N01_EcuacionesLineales_SegundoGrado.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_obtenerx.clicked.connect(self.calcular)
        self.txt_b1.setEnabled(False)
        self.txt_b2.setEnabled(False)
        self.txt_a1.setEnabled(False)
        self.txt_c1.setEnabled(False)
        self.txt_a2.setEnabled(False)
        self.spinBox_a.setMinimum(-10)
        self.spinBox_a.setMaximum(10)
        self.spinBox_a.setSingleStep(1)
        self.spinBox_a.setValue(0)
        self.spinBox_a.valueChanged.connect(self.cambiaValorA)
        self.spinBox_b.setMinimum(-10)
        self.spinBox_b.setMaximum(10)
        self.spinBox_b.setSingleStep(1)
        self.spinBox_b.setValue(0)
        self.spinBox_b.valueChanged.connect(self.cambiaValorB)
        self.spinBox_c.setMinimum(-10)
        self.spinBox_c.setMaximum(10)
        self.spinBox_c.setSingleStep(1)
        self.spinBox_c.setValue(0)
        self.spinBox_c.valueChanged.connect(self.cambiaValorC)


    #Area de los Slots
    def calcular(self):
        a = self.spinBox_a.value()
        b = self.spinBox_b.value()
        c = self.spinBox_c.value()
        try:
            cadena1 = "(-b + m.sqrt( (b**2 - 4*a*c))) / (2*a)"
            cadena1 = eval(cadena1)
            self.btn_x1.setText('X1\n' + str(round(cadena1, 2)))
            cadena2 = "(-b - m.sqrt( (b**2 - 4*a*c))) / (2*a)"
            cadena2 = eval(cadena2)
            self.btn_x2.setText('X2\n' + str(round(cadena2, 2)))
        except Exception as e:
            mnsj = QtWidgets.QMessageBox()
            mnsj.setText(f'{e}\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░\n░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░\n░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░\n' \
                     '░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░\n░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░\n░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░\n░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░\n' \
                     '░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░\n░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░\n░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░\n░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░\n' \
                     '░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░\n░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░\n░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░\n░░░░█░░░░░░░░░░░░░░░░░░░░░█░░\n' \
                     '░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░\n░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
            mnsj.exec()
            print(f'Erro {e}')

    def cambiaValorA(self):
        valor = self.spinBox_a.value()
        self.txt_a1.setText('(('+str(valor)+')')
        self.txt_a2.setText('('+str(valor)+')')

    def cambiaValorB(self):
        valor = self.spinBox_b.value()
        self.txt_b1.setText('('+str(valor)+')')
        self.txt_b2.setText('('+str(valor)+')')

    def cambiaValorC(self):
        valor = self.spinBox_c.value()
        self.txt_c1.setText('('+str(valor)+'))')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())