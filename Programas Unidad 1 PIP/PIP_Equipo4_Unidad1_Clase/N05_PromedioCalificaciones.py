import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = 'N05_PromedioCalificaciones.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_calcular.clicked.connect(self.calcular)

        self.calificaciones = []
        self.txt_promedio.setEnabled(False)

        validadorNumeros = QtGui.QIntValidator(0, 10)
        self.txt_calificacion.setValidator(validadorNumeros)

    #Area de los Slots
    def agregar(self):
        calificacion = self.txt_calificacion.text()
        calificacion = float(calificacion)
        self.calificaciones.append(calificacion)
        self.txt_calificacion.setText('')
        self.txt_promedio.setText('')
        self.msn('Calificacion agragada')

    def calcular(self):
        calificacion = sum(self.calificaciones)/len(self.calificaciones)
        calificacion = round(calificacion,2)
        self.txt_promedio.setText(str(calificacion))

    def msn(self, cal):
        msnj = QtWidgets.QMessageBox()
        msnj.setText(f'{cal}')
        msnj.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())