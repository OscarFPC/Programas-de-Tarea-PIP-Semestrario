import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = 'N06_DiscriminanteDeMatrix2x2.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_calcular.clicked.connect(self.operacion)
        self.txt_resultado.setEnabled(False)
        ValidarNum = QtGui.QIntValidator()
        self.txt_a11.setValidator(ValidarNum)
        self.txt_a12.setValidator(ValidarNum)
        self.txt_a21.setValidator(ValidarNum)
        self.txt_a22.setValidator(ValidarNum)

    #Area de los Slots
    def operacion(self):
        if (len(self.txt_a11.text()) != 0) and (len(self.txt_a12.text()) != 0) and (len(self.txt_a21.text()) != 0) and (len(self.txt_a22.text()) != 0):
            a11 = float(self.txt_a11.text())
            a12 = float(self.txt_a12.text())
            a21 = float(self.txt_a21.text())
            a22 = float(self.txt_a22.text())
            print(a11, a12, a21, a22)
            result = (a11 * a22) - (a12 * a21)
            print(result)
            result = round(result, 2)
            self.txt_resultado.setText(str(result))
        else:
            mesage = QtWidgets.QMessageBox()
            mesage.setText('Algunos espacios estan vacios\n'
                           '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
                           '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿'
                           )
            mesage.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())