import math
import sys
from builtins import str

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N04_TeoremaPitagoras.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_calcular.clicked.connect(self.calcular)
        self.btn_texto.clicked.connect(self.runtroll)

    #Area de los Slots
    def runtroll(self):
        message = QtWidgets.QMessageBox()
        message.setText('░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄\n''░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄\n'
        '░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█\n''░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█\n''░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█\n'
        '█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█\n''█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n'
        '░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█\n''░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█\n'
        '░░░█░░██░░▀█▄▄▄█▄▄█▄████░█\n''░░░░█░░░▀▀▄░█░░░█░███████░█\n'
        '░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█\n''░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█\n'
        '░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█\n''░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█')
        message.exec()
    def calcular(self):
        a2 = self.txt_a.text()
        b2 = self.txt_b.text()
        c2 = self.txt_c.text()
        message = QtWidgets.QMessageBox()
        def esNumero(cadena):
            try:
                float(cadena)
                return True
            except ValueError:
                return False
        if (len(a2)!=0) and (len(b2)!=0) and (len(c2)!=0):
            valores = [a2,b2,c2]
            validacion = True
            print(valores)
            if valores.count('x') == 1:
                valores.remove('x')
                print(valores,'elminado')
            else:
                message.setText('Se ingreso mas de una X para el valor buscado')
                message.exec()
            for valor in valores:
                if esNumero(valor)==False:
                    validacion = False
            if validacion == True:
                if str(a2).lower() == 'x':
                    b = float(b2)
                    c = float(c2)
                    a2 = float((b**2)+(c**2))
                    message.setText(f'La hipotenusa del triangulo es:\n'
                                    f'{math.sqrt(a2):.2f}\n'
                                    f'░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░\n'f'░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░\n'
                                    f'░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░\n░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░\n'
                                    f'░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░\n░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██\n░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n'
                                    f'░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██\n░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██\n██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██\n'
                                    f'█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░\n░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░\n'
                                    f'░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░\n░░████████████░░░█████████████████░░░░░░'
                                    )
                    message.exec()
                elif str(b2).lower() == 'x':
                    a = float(a2)
                    c = float(c2)
                    b2 = float((a**2)-(c**2))
                    message.setText(f'El valor del cateto\n'
                                    f'del triangulo es:\n'
                                    f'{math.sqrt(b2):.2f}\n'
                                    f'░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░\n'f'░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░\n'
                                    f'░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░\n░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░\n'
                                    f'░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░\n░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██\n░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n'
                                    f'░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██\n░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██\n██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██\n'
                                    f'█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░\n░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░\n'
                                    f'░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░\n░░████████████░░░█████████████████░░░░░░'
                                    )
                    message.exec()
                elif str(c2).lower() == 'x':
                    a = float(a2)
                    b = float(b2)
                    c2 = float((a**2)-(b**2))
                    message.setText(f'El valor del cateto\n'
                                    f'del triangulo es:\n'
                                    f'{math.sqrt(c2):.2f}\n'
                                    f'░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░\n'f'░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░\n'
                                    f'░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░\n░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░\n'
                                    f'░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░\n░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██\n░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n'
                                    f'░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██\n░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██\n██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██\n'
                                    f'█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░\n░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░\n'
                                    f'░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░\n░░████████████░░░█████████████████░░░░░░')
                    message.exec()
                else:
                    message.setText('Ingrese una "" X "" al valor\n'
                                    'que desea encontrar\n'
                                    '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
                                    '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿'

                                    )
                    message.exec()
            else:
                message.setText('Algunos Valores no son validos\n'
                                '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
                                '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿'

                                )
                message.exec()
        else:
            message.setText('Algunos parametros estan vacios\n'
            '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
            '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿'
                            )
            message.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())