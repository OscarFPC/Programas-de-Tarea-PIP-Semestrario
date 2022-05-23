#Un artículo de N pesos debe ser pagado con gatos,
# donde cada gato equivale a 5 pesos.
# Solo se aceptan 4 pesos o menos, lo demás deberá ser pagado en gatos
import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N12_PagandoConGatos.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        validarN = QtGui.QIntValidator()
        self.txt_precio.setValidator(validarN)
        self.txt_gatos.setEnabled(False)
        self.txt_pesos.setEnabled(False)
        self.btn_pagar.clicked.connect(self.calcular)

    #Area de los Slots
    def calcular(self):
        precio = int(self.txt_precio.text())
        if(precio>5):
            gatos = round(precio/5)
            pesos = precio%5
            self.txt_gatos.setText(str(gatos))
            self.txt_pesos.setText((str(pesos)))
        else:
            self.txt_gatos.setText('0')
            self.txt_pesos.setText(str(precio))
        print(gatos, pesos)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())