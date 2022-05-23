import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = 'N09_AreaDePoligonoRegular.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_calcular.clicked.connect(self.calcular)
        validarN = QtGui.QIntValidator()
        self.txt_lados.setValidator(validarN)
        self.txt_valorlado.setValidator(validarN)
        self.txt_apotema.setValidator(validarN)
        self.txt_area.setEnabled(False)

    #Area de los Slots
    def calcular(self):
        message = QtWidgets.QMessageBox()
        if (len(self.txt_lados.text()) != 0) and (len(self.txt_valorlado.text()) != 0) and (len(self.txt_apotema.text()) != 0):
            apotema = int(self.txt_apotema.text())
            perimetro = int(self.txt_lados.text()) * int(self.txt_valorlado.text())
            self.txt_area.setText(str(perimetro * apotema / 2))
        else:
            message.setText('Algunos parametros estan vacios\n'
                            '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
                            '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿')
            message.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())