import math
import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N05_DistanciaEntreDosPuntos.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_calcular.clicked.connect(self.calcularD)

    #Area de los Slots
    def calcularD(self):
        x1 = self.txt_x1.text()
        y1 = self.txt_y1.text()
        x2 = self.txt_x2.text()
        y2 = self.txt_y2.text()
        print(x1,y1,x2,y2)
        message = QtWidgets.QMessageBox()
        def esNumero(cadena):
            try:
                float(cadena)
                return True
            except ValueError:
                return False
        if (len(x1) != 0) and (len(y1) != 0) and (len(x2) != 0) and (len(y2) != 0):
            puntos = [x1,y1,x2,y2]
            print(puntos)
            validacion = True
            for punto in puntos:
                if esNumero(punto) == False:
                    validacion = False
                    print('no valido')
            if validacion == True:
                x1 = float(x1)
                y1 = float(y1)
                x2 = float(x2)
                y2 = float(y2)
                d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
                message.setText(f'La distancia entre\n'
                                f'el punto A ( {x1} , {y1} )\n'
                                f'y\n'
                                f'el punto B ( {x2} , {y2} )\n'
                                f'es : " {d:.2f} "\n'
                                f'░░░░░░░░░░░░░░░░░░░░░░█████████░░░░░░░░░\n'f'░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███░░░░░░░\n'
                                f'░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███░░░░\n░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░\n'
                                f'░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███░\n░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██\n░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██\n'
                                f'░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██\n░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██\n██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██\n'
                                f'█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░\n░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░\n'
                                f'░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█░░░░░\n░░████████████░░░█████████████████░░░░░░')
                message.exec()
            else:
                message.setText('Algunos valores no son validos\n'
                                '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
                                '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿'
                                )
                message.exec()
        else:
            message.setText('Algunos espacios estan vacios\n'
            '╭━┳━╭━╭━╮╮\n''┃┈┈┈┣▅╋▅┫┃\n''┃┈┃┈╰━╰━━━━━━╮\n''╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣\n'
            '╲┃┈┈┈┈┈┈┈┈┈▉▉▉\n''╲┃┈┈┈┈┈┈┈┈┈◥▉◤\n''╲┃┈┈┈┈╭━┳━━━━╯\n''╲┣━━━━━━┫﻿'
                            )
            message.exec()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())



