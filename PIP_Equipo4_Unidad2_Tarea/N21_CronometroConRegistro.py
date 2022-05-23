#Al cronómetro de hoy, agregar boton que
# agregue marcas de tiempo a un list widget
import sys

from PyQt5 import uic, QtWidgets,QtGui, QtCore

qtCreatorFile = 'N21_CronometroConRegistro.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_pausar.clicked.connect(self.pausar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_pausar.setVisible(False)
        self.btn_reiniciar.setVisible(False)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)
        self.milis = 0
        self.segundos = 0
        self.minutos = 0
        self.count = 0

    #Area de los Slots
    def iniciar(self):
        if(self.btn_iniciar.text() == 'Iniciar'):
            self.listWidget.clear()
        self.btn_pausar.setVisible(True)
        self.btn_reiniciar.setVisible(True)
        self.btn_iniciar.setText('Continuar')
        self.btn_iniciar.setVisible(False)
        self.segundoPlano.start(10)

    def pausar(self):
        self.btn_iniciar.setVisible(True)
        self.segundoPlano.stop()

    def reiniciar(self):
        self.btn_pausar.setVisible(False)
        self.btn_reiniciar.setVisible(False)
        self.btn_iniciar.setText('Iniciar')
        self.btn_iniciar.setVisible(True)
        self.milis = 0
        self.segundos = 0
        self.minutos = 0
        if(self.segundoPlano.isActive()):
            self.segundoPlano.stop()
        self.lbl_milis.setText(str(self.milis))
        self.lbl_min.setText(str(self.minutos))
        self.lbl_seg.setText(str(self.segundos))
        self.count = 0

    def agregar(self):
        self.count += 1
        milisegundos = self.lbl_milis.text()
        minutos = self.lbl_min.text()
        segundos = self.lbl_seg.text()
        cadena = f'Tiempo {self.count}.- {minutos} : {segundos} : {milisegundos}'
        self.listWidget.addItem(cadena)
    def temporizador(self):
        self.milis += 1
        if(self.milis == 60):
            self.segundos += 1
            if(self.segundos == 60):
                self.minutos += 1
                self.segundos = 0
            self.milis = 0
        self.lbl_milis.setText(str(self.milis))
        self.lbl_min.setText(str(self.minutos))
        self.lbl_seg.setText(str(self.segundos))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())