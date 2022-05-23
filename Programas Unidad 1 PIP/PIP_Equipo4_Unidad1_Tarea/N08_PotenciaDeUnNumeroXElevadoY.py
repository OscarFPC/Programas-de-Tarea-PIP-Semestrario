import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = 'N08_PotenciaDeUnNumeroXElevadoY.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.txt_r.setEnabled(False)
        validarN = QtGui.QIntValidator()
        self.txt_x.setValidator(validarN)
        self.txt_y.setValidator(validarN)
        self.btn_calcular.clicked.connect(self.calcular)

    #Area de los Slots
    def calcular(self):
        if (len(self.txt_x.text()) != 0) and (len(self.txt_y.text()) != 0):
            self.txt_r.setText(str(int(self.txt_x.text()) ** int(self.txt_y.text())))
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