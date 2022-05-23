import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = 'N07_CentenasDecenasUnidades.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_obtener.clicked.connect(self.obtener)
        ValidarNum = QtGui.QIntValidator(0,100)
        self.txt_numero.setValidator(ValidarNum)
        self.txt_centenas.setEnabled(False)
        self.txt_decenas.setEnabled(False)
        self.txt_unidades.setEnabled(False)

    #Area de los Slots
    def obtener(self):
        if (len(self.txt_numero.text()) != 0):
            numero = int(self.txt_numero.text())
            u = numero % 10
            numero = (numero - u) / 10
            d = numero % 10
            numero = (numero - d) / 10
            c = numero % 10
            self.txt_centenas.setText(str(round(c)))
            self.txt_decenas.setText(str(round(d)))
            self.txt_unidades.setText(str(round(u)))
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