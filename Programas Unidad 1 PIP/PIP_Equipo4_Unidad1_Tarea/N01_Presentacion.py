import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = 'N01_Presentacion.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_saludar.clicked.connect(self.presentar)

    #Area de los Slots
    def presentar(self):
        p = QtWidgets.QMessageBox()
        p.setText('  ▔▔▔▔▔╲\n▕╮╭┻┻╮╭┻┻╮╭▕╮╲\n▕╯┃╭╮┃┃╭╮┃╰▕╯╭▏\n▕╭┻┻┻┛┗┻┻┛ ▕ ╰▏\n▕╰━━━┓┈┈┈╭╮▕╭╮▏\n'
                  '▕╭╮╰┳┳┳┳╯╰╯▕╰╯▏\n▕╰╯┈┗┛┗┛┈╭╮▕╮┈▏\n'
                  'Hola a Todos\n'
                  'Me llamo Oscar\n'
                  '\n'
                  'Bienvenidos a la materia de:\n'
                  'Programacion de interfaces y puertos.\n'
                  '\n'
                  'Impartida por el:\n'
                  'Dr. Garcia Ruiz Alejandro Humberto\n'
                  'Los dias Viernes de 7 a 10 A.M')
        p.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())