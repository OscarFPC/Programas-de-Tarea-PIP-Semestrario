#Progress bar que se cargue en un tiempo en segundos dado
import sys

from PyQt5 import uic, QtWidgets,QtGui, QtCore

qtCreatorFile = 'N22_ProgressBarPorSegundo.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.validar = QtGui.QIntValidator()
        self.txt_segundos.setValidator(self.validar)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)
        self.valor = 0
        self.pb_1.setValue(self.valor)
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.division = 0
    #Area de los Slots
    def iniciar(self):
        self.lbl_i1.setVisible(False)
        self.lbl_tt.setVisible(False)
        self.txt_segundos.setVisible(False)
        self.btn_iniciar.setVisible(False)
        segundos = int(self.txt_segundos.text())
        self.division = 100/segundos
        print(self.division)
        self.segundoPlano.start(1000)
    def temporizador(self):
        #self.valor += int(self.division)
        self.valor += self.division
        if(self.valor >= 100):
            self.pb_1.setValue(100)
        else:
            self.pb_1.setValue(int(self.valor))
        if(self.valor >= 100):
            self.segundoPlano.stop()
            self.lbl_descarga.setText('Downloading complete')
            self.pb_1.setVisible(False)
            self.label_3.setVisible(False)
            comando = "color: rgb(0, 255, 0);"
            self.lbl_descarga.setStyleSheet(comando)
        print(self.valor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())