#6. Dado un número de dos dígitos, intercambiar sus valores. Ejemplo: 89 pasaría a 98
import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N14_IntercambiarNumerosDosValores.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(99)
        self.spinBox.setSingleStep(1)
        self.spinBox.setValue(0)
        self.spinBox.valueChanged.connect(self.cambiar)
        self.txt_numeronuevo.setEnabled(False)

    #Area de los Slots
    def cambiar(self):
        a = int(self.spinBox.value())
        print(a)
        if (a >= 10) and (a < 100):
            aux1 = int(a / 10)
            print(aux1)
            aux2 = a % 10
            print(aux2)
            if(aux2==0):
                cadena = (f'{aux2}{aux1}')
                self.txt_numeronuevo.setText(cadena)
            else:
                nuevo = (aux2 * 10) + aux1
                print(nuevo)
                self.txt_numeronuevo.setText(str(nuevo))

        else:
            msj = QtWidgets.QMessageBox()
            msj.setText('Numero no valido'
                        '\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░\n░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░\n░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░\n' \
                     '░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░\n░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░\n░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░\n░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░\n' \
                     '░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░\n░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░\n░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░\n░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░\n' \
                     '░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░\n░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░\n░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░\n░░░░█░░░░░░░░░░░░░░░░░░░░░█░░\n' \
                     '░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░\n░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())