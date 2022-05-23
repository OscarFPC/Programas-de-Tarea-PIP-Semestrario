import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N08_IMC_CambioColor.ui' #Nombre del archivo aqui

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
                if imc < 18.5:
                    #color azul
                    comando = "background-color: rgb(63, 178, 245);"
                    self.btn_color.setStyleSheet(comando)
                    self.btn_color.setText('IMC - Desnutrición')
                if imc >= 18.5 and imc <= 24.9:
                    #color verde
                    comando = "background-color: rgb(73, 172, 34);"
                    self.btn_color.setStyleSheet(comando)
                    self.btn_color.setText('IMC - Normal')
                if imc >= 25 and imc <= 29.9:
                    #color naranja
                    comando = "background-color: rgb(252, 179, 9);"
                    self.btn_color.setStyleSheet(comando)
                    self.btn_color.setText('IMC - SobrePeso')
                if imc >= 30 and imc <= 34.9:
                    #color rojo
                    comando = "background-color: rgb(254, 61, 50);"
                    self.btn_color.setStyleSheet(comando)
                    self.btn_color.setText('IMC - Obesidad')
                if imc >35:
                    #color rojo oscuro
                    comando = "background-color: rgb(222, 0, 0);"
                    self.btn_color.setStyleSheet(comando)
                    self.btn_color.setText('IMC - Obesidad Extrema')
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