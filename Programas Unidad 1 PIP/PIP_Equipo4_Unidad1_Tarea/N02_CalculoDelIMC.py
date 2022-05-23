import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N02_CalculoDelIMC.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_calcular.clicked.connect(self.calcular)


    #Area de los Slots
    def calcular(self):
        peso = self.txt_peso.text()
        estatura = self.txt_estatura.text()
        mesage = QtWidgets.QMessageBox()
        def esNumero(cadena):
            try:
                float(cadena)
                return True
            except ValueError:
                return False
        if (len(peso)!= 0) and (len(estatura)!=0):
            persona = [peso, estatura]
            validacion = True
            print(persona)
            for datos in persona:
                if esNumero(datos) == False:
                    validacion = False
            if validacion == True:
                peso = float(self.txt_peso.text())
                estatura = float(self.txt_estatura.text())
                imc = peso / estatura ** 2
                mesage.setText(f'Tu IMC es de: {imc:.2f}\n'
                               f'▓▓▓▓\n'
                               f'▒▒▒▓▓\n'
                               f'▒▒▒▒▒▓\n'
                               f'▒▒▒▒▒▒▓\n▒▒▒▒▒▒▓\n▒▒▒▒▒▒▒▓\n▒▒▒▒▒▒▒▓▓▓\n▒▓▓▓▓▓▓░░░▓\n'
                               f'▒▓░░░░▓░░░░▓\n▓░░░░░░▓░▓░▓\n▓░░░░░░▓░░░▓\n▓░░▓░░░▓▓▓▓\n'
                               f'▒▓░░░░▓▒▒▒▒▓\n▒▒▓▓▓▓▒▒▒▒▒▓\n▒▒▒▒▒▒▒▒▓▓▓▓\n▒▒▒▒▒▓▓▓▒▒▒▒▓\n'
                               f'▒▒▒▒▓▒▒▒▒▒▒▒▒▓\n▒▒▒▓▒▒▒▒▒▒▒▒▒▓\n▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓\n▒▓▒▓▒▒▒▒▒▒▒▒▒▓\n'
                               f'▒▓▒▓▓▓▓▓▓▓▓▓▓\n▒▓▒▒▒▒▒▒▒▓\n▒▒▓▒▒▒▒▒▓')
                mesage.exec()
            else:
                mesage.setText('Algunos valores no son validos\n'
                                '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
                                '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿'
                                )
                mesage.exec()
        else:
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