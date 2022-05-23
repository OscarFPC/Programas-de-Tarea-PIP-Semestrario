import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N10_EcuacionLinealAX+B.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_calcular.clicked.connect(self.calcular)
        self.txt_x.setEnabled(False)
        validarN = QtGui.QIntValidator()
        self.txt_a.setValidator(validarN)
        self.txt_b.setValidator(validarN)
        self.txt_c.setValidator(validarN)

    #Area de los Slots
    def calcular(self):
        if (len(self.txt_a.text()) != 0) and (len(self.txt_b.text()) != 0) and (len(self.txt_c.text()) != 0):
            cal = (int(self.txt_c.text()) - int(self.txt_b.text())) / int(self.txt_a.text())
            self.txt_x.setText(str(round(cal, 2)))
        else:
            message = QtWidgets.QMessageBox()
            message.setText('Algunos parametros estan vacios\n'
                            '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
                            '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿')
            message.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())