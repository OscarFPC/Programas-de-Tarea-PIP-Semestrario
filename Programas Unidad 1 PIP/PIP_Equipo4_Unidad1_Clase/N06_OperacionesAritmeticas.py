import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = 'N06_OperacionesAritmeticas.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_sumar.clicked.connect(self.operacion)
        self.btn_restar.clicked.connect(self.operacion)
        self.btn_multiplicar.clicked.connect(self.operacion)
        self.btn_dividir.clicked.connect(self.operacion)
        self.txt_resultado.setEnabled(False)
        validadorNumeros = QtGui.QIntValidator()
        self.txt_num1.setValidator(validadorNumeros)
        self.txt_num2.setValidator(validadorNumeros)

    #Area de los Slots
    def operacion(self):
        print('Operacion Aplicada : ', end='')
        sender = self.sender()
        Operador = sender.text()
        print(Operador)
        num1 = int(self.txt_num1.text())
        num2 = int(self.txt_num2.text())
        if Operador == 'SUMAR':
            resultado = num1+num2
        elif Operador == 'RESTAR':
            resultado = num1-num2
        elif Operador == 'MULTIPLICAR':
            resultado = num1*num2
        else:
            resultado = num1/num2
        self.txt_resultado.setText(str(resultado))

        '''
        Ejercicios:
        1.- Discriminante de una matriz de 2*1
        2.- De un numero de 3 digitos obtener sus centenas, decenas y unidades
        3.- Obtener la potencia de un numero x elevado a un exponente y
        4.- Area de un poligono regular dadas sus medidas (lado y apotema)
        5.- Solucion de la ecucacion lineal de la forma AX + B... se pide: A,X y B
        '''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())