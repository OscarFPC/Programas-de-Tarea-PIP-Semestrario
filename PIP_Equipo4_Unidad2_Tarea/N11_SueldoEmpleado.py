import sys

from PyQt5 import uic, QtWidgets, QtGui
#Sueldo de un empleado, que trabaja N horas por Y días a la semana.
# Considerando Jornadas Laborales de 40horas con un Sueldo de 10 pesos y Extras de 20 pesos
# 128/3 = 42.66666666666667
qtCreatorFile = 'N11_SueldoEmpleado.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        validarN = QtGui.QIntValidator()
        self.txt_diasT.setValidator(validarN)
        self.txt_horasT.setEnabled(False)
        self.txt_horasT.setValidator(validarN)
        self.txt_hnormales.setEnabled(False)
        self.txt_hextras.setEnabled(False)
        self.txt_totalpago.setEnabled(False)
        self.btn_calcularpago.setEnabled(False)
        self.btn_ingresarhoras.setEnabled(False)
        self.btn_ingresardias.clicked.connect(self.ingresodias)
        self.btn_ingresarhoras.clicked.connect(self.ingresohoras)
        self.btn_calcularpago.clicked.connect(self.calcular)
        self.lista1 = []
        self.lista2 = []
        self.count = 1

    #Area de los Slots
    def ingresodias(self):
        self.txt_diasT.setEnabled(False)
        self.btn_ingresardias.setEnabled(False)
        self.txt_horasT.setEnabled(True)
        self.btn_ingresarhoras.setEnabled(True)
        self.dias = int(self.txt_diasT.text())
        self.label_5.setText(f'Horas trabajadas de la jornada {self.count}')

    def ingresohoras(self):
        print(self.count, self.dias)
        if(self.count<=self.dias):
            horas = int(self.txt_horasT.text())
            if (horas < 40):
                self.lista1.append(horas)
            else:
                horasE = horas - 40
                self.lista2.append(horasE)
                self.lista1.append(40)
            self.txt_horasT.setText('')
            self.label_5.setText(f'Horas trabajadas de la jornada {self.count + 1}')
            self.count += 1
            print('ok')
        if (self.count>self.dias):
            self.label_5.setText(f'Horas trabajadas de la jornada')
            self.txt_horasT.setEnabled(False)
            self.btn_ingresarhoras.setEnabled(False)
            self.btn_calcularpago.setEnabled(True)
            self.horasT = 0
            self.horasE = 0
            for e in self.lista1:
                self.horasT += e
            for e in self.lista2:
                self.horasE += e
            self.txt_hnormales.setText(str(self.horasT))
            self.txt_hextras.setText(str(self.horasE))


    def calcular(self):
        pago = float((self.horasT*10)+(self.horasE*20))
        self.txt_totalpago.setText(f'${pago:.2f}')
        print(self.lista1)
        print(self.lista2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())