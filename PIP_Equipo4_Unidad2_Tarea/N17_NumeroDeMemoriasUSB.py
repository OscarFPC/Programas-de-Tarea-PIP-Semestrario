#9. Calcular el número de memorias USB de Y capacidad, necesarias para hacer una copia de seguridad, de X Gigabytes de información almacenada en un disco duro
import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N17_NumeroDeMemoriasUSB.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        validarN = QtGui.QIntValidator()
        self.txt_copia.setValidator(validarN)
        self.txt_usbs.setEnabled(False)
        self.txt_porciento.setVisible(False)
        self.label_8.setVisible(False)
        self.btn_calcular.clicked.connect(self.calcular)
        self.txt_totalusb.setEnabled(False)

    #Area de los Slots
    def calcular(self):
        copia = int(self.txt_copia.text())
        usb = int(self.txt_capacidad.text())
        cantusb = copia / usb
        self.txt_usbs.setText(str(int(cantusb)))
        resto = copia % usb
        if(resto!=0):
            porcentaje = 100/usb * resto
            self.txt_porciento.setVisible(True)
            self.txt_porciento.setEnabled(False)
            self.label_8.setVisible(True)
            self.txt_porciento.setText(f'{porcentaje:.2f} %')
            self.txt_totalusb.setText(str(int(cantusb)+1))
        else:
            self.txt_porciento.setVisible(False)
            self.label_8.setVisible(False)
            self.txt_totalusb.setText(str(int(cantusb)))
        #print(f'USBs = {int(cantusb)} y el {(100 / 32 * resto):.2f} % de una USB mas')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())