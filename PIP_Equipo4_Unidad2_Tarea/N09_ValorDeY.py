import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N09_ValorDeY.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_obtenery.clicked.connect(self.calcular)
        self.spinBox_x.setMinimum(-10)
        self.spinBox_x.setMaximum(10)
        self.spinBox_x.setSingleStep(1)
        self.spinBox_x.setValue(0)

    #Area de los Slots
    def calcular(self):
        a = self.spinBox_x.value()
        try:
            cadena1 = "(3*a + 2)"
            cadena1 = eval(cadena1)
            self.btn_y.setText('Y = ' + str(round(cadena1, 2)))
        except Exception as e:
            mnsj = QtWidgets.QMessageBox()
            mnsj.setText(
                f'{e}\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░\n░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░\n░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░\n' \
                '░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░\n░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░\n░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░\n░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░\n' \
                '░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░\n░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░\n░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░\n░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░\n' \
                '░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░\n░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░\n░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░\n░░░░█░░░░░░░░░░░░░░░░░░░░░█░░\n' \
                '░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░\n░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
            mnsj.exec()
            print(f'Erro {e}')
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())