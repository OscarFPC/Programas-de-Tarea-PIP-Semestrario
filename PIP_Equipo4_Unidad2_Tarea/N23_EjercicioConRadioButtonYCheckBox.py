import sys

from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = 'N23_EjercicioConRadioButtonYCheckBox.ui' #Nombre del archivo aqui

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_ver.clicked.connect(self.ver)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        self.rb_a1.toggled.connect(self.activar)
        self.rb_a2.toggled.connect(self.activar)
        self.rb_a3.toggled.connect(self.activar)
        self.rb_a4.toggled.connect(self.activar)
        self.lbl_mostrar.setVisible(False)
        self.groupBox_5.setVisible(False)
        self.colorV = f"background-color: rgb({0}, {255}, {0});" \
                      f"color: rgb({0}, {0}, {0});"
        self.colorB = f"background-color: rgb({0}, {0}, {0});" \
                      f"color: rgb({255}, {255}, {255});"

    #Area de los Slots
    def ver(self):
        m = self.textomotherboard()
        r = self.textoRam()
        g = self.textoGPU()
        c = self.textoCPU()
        f = self.textoFuente()
        a,ca = self.textoAlmacenamiento()
        agregar = self.textoAgregar()
        if((m!=0) and (r!=0) and (g!=0) and (c!=0) and (f!=0) and (a!=0) and (ca!=0)):
            cadena = f'Motherboard: {m}\n\nRam: {r}\n\nGPU: {g}\n\nCPU: {c}\n\nFuente de poder: {f}\n\nAlmacenamiento: {a}\n\n' \
                     f'Capacidad de Almacenamiento: {ca}\n\n{agregar}'
            self.lbl_mostrar.setText(cadena)
            self.lbl_mostrar.setVisible(True)
            self.gb_1.setEnabled(False)
            self.gb_2.setEnabled(False)
            self.gb_3.setEnabled(False)
            self.gb_4.setEnabled(False)
            self.gb_5.setEnabled(False)
            self.gb_6.setEnabled(False)
            self.gb_7.setEnabled(False)
            self.gb_7.setVisible(False)
        else:
            msj = QtWidgets.QMessageBox()
            msj.setText('No ha seleccionado algunos elementos, favor de hacerlo')
            msj.exec()

    def reiniciar(self):
        self.gb_1.setEnabled(True)
        self.gb_2.setEnabled(True)
        self.gb_3.setEnabled(True)
        self.gb_4.setEnabled(True)
        self.gb_5.setEnabled(True)
        self.gb_6.setEnabled(True)
        self.gb_7.setEnabled(True)
        self.gb_7.setVisible(True)
        self.lbl_mostrar.setVisible(False)
        print('ok2')
    def textomotherboard(self):
        motherboard = 0
        if (self.rb_m1.isChecked()):
            motherboard = self.rb_m1.text()
            self.rb_m1.setStyleSheet(self.colorV)
        else:
            self.rb_m1.setStyleSheet(self.colorB)
        if (self.rb_m2.isChecked()):
            motherboard = self.rb_m2.text()
            self.rb_m2.setStyleSheet(self.colorV)
        else:
            self.rb_m2.setStyleSheet(self.colorB)
        if (self.rb_m3.isChecked()):
            motherboard = self.rb_m3.text()
            self.rb_m3.setStyleSheet(self.colorV)
        else:
            self.rb_m3.setStyleSheet(self.colorB)
        return motherboard
    def textoRam(self):
        ram = 0
        if(self.rb_ram1.isChecked()):
            ram = self.rb_ram1.text()
            self.rb_ram1.setStyleSheet(self.colorV)
        else:
            self.rb_ram1.setStyleSheet(self.colorB)
        if (self.rb_ram2.isChecked()):
            ram = self.rb_ram2.text()
            self.rb_ram2.setStyleSheet(self.colorV)
        else:
            self.rb_ram2.setStyleSheet(self.colorB)
        if (self.rb_ram3.isChecked()):
            ram = self.rb_ram3.text()
            self.rb_ram3.setStyleSheet(self.colorV)
        else:
            self.rb_ram3.setStyleSheet(self.colorB)
        if (self.rb_ram4.isChecked()):
            ram = self.rb_ram4.text()
            self.rb_ram4.setStyleSheet(self.colorV)
        else:
            self.rb_ram4.setStyleSheet(self.colorB)
        if (self.rb_ram5.isChecked()):
            ram = self.rb_ram5.text()
            self.rb_ram5.setStyleSheet(self.colorV)
        else:
            self.rb_ram5.setStyleSheet(self.colorB)
        if (self.rb_ram6.isChecked()):
            ram = self.rb_ram6.text()
            self.rb_ram6.setStyleSheet(self.colorV)
        else:
            self.rb_ram6.setStyleSheet(self.colorB)
        if (self.rb_ram7.isChecked()):
            ram = self.rb_ram7.text()
            self.rb_ram7.setStyleSheet(self.colorV)
        else:
            self.rb_ram7.setStyleSheet(self.colorB)
        if (self.rb_ram8.isChecked()):
            ram = self.rb_ram8.text()
            self.rb_ram8.setStyleSheet(self.colorV)
        else:
            self.rb_ram8.setStyleSheet(self.colorB)
        if (self.rb_ram9.isChecked()):
            ram = self.rb_ram9.text()
            self.rb_ram9.setStyleSheet(self.colorV)
        else:
            self.rb_ram9.setStyleSheet(self.colorB)
        if (self.rb_ram10.isChecked()):
            ram = self.rb_ram10.text()
            self.rb_ram10.setStyleSheet(self.colorV)
        else:
            self.rb_ram10.setStyleSheet(self.colorB)
        return ram
    def textoGPU(self):
        gpu = 0
        if(self.rb_gpu1.isChecked()):
            gpu = self.rb_gpu1.text()
            self.rb_gpu1.setStyleSheet(self.colorV)
        else:
            self.rb_gpu1.setStyleSheet(self.colorB)
        if (self.rb_gpu2.isChecked()):
            gpu = self.rb_gpu2.text()
            self.rb_gpu2.setStyleSheet(self.colorV)
        else:
            self.rb_gpu2.setStyleSheet(self.colorB)
        if (self.rb_gpu3.isChecked()):
            gpu = self.rb_gpu3.text()
            self.rb_gpu3.setStyleSheet(self.colorV)
        else:
            self.rb_gpu3.setStyleSheet(self.colorB)
        if (self.rb_gpu4.isChecked()):
            gpu = self.rb_gpu4.text()
            self.rb_gpu4.setStyleSheet(self.colorV)
        else:
            self.rb_gpu4.setStyleSheet(self.colorB)
        if (self.rb_gpu5.isChecked()):
            gpu = self.rb_gpu5.text()
            self.rb_gpu5.setStyleSheet(self.colorV)
        else:
            self.rb_gpu5.setStyleSheet(self.colorB)
        if (self.rb_gpu6.isChecked()):
            gpu = self.rb_gpu6.text()
            self.rb_gpu6.setStyleSheet(self.colorV)
        else:
            self.rb_gpu6.setStyleSheet(self.colorB)
        return gpu
    def textoCPU(self):
        cpu = 0
        if(self.rb_cpu1.isChecked()):
            cpu = self.rb_cpu1.text()
            self.rb_cpu1.setStyleSheet(self.colorV)
        else:
            self.rb_cpu1.setStyleSheet(self.colorB)
        if (self.rb_cpu2.isChecked()):
            cpu = self.rb_cpu2.text()
            self.rb_cpu2.setStyleSheet(self.colorV)
        else:
            self.rb_cpu2.setStyleSheet(self.colorB)
        if (self.rb_cpu3.isChecked()):
            cpu = self.rb_cpu3.text()
            self.rb_cpu3.setStyleSheet(self.colorV)
        else:
            self.rb_cpu3.setStyleSheet(self.colorB)
        if (self.rb_cpu4.isChecked()):
            cpu = self.rb_cpu4.text()
            self.rb_cpu4.setStyleSheet(self.colorV)
        else:
            self.rb_cpu4.setStyleSheet(self.colorB)
        if (self.rb_cpu5.isChecked()):
            cpu = self.rb_cpu5.text()
            self.rb_cpu5.setStyleSheet(self.colorV)
        else:
            self.rb_cpu5.setStyleSheet(self.colorB)
        return cpu
    def textoFuente(self):
        fuente = 0
        if(self.rb_f1.isChecked()):
            fuente = self.rb_f1.text()
            self.rb_f1.setStyleSheet(self.colorV)
        else:
            self.rb_f1.setStyleSheet(self.colorB)
        if (self.rb_f2.isChecked()):
            fuente = self.rb_f2.text()
            self.rb_f2.setStyleSheet(self.colorV)
        else:
            self.rb_f2.setStyleSheet(self.colorB)
        if (self.rb_f3.isChecked()):
            fuente = self.rb_f3.text()
            self.rb_f3.setStyleSheet(self.colorV)
        else:
            self.rb_f3.setStyleSheet(self.colorB)
        if (self.rb_f4.isChecked()):
            fuente = self.rb_f4.text()
            self.rb_f4.setStyleSheet(self.colorV)
        else:
            self.rb_f4.setStyleSheet(self.colorB)
        if (self.rb_f5.isChecked()):
            fuente = self.rb_f5.text()
            self.rb_f5.setStyleSheet(self.colorV)
        else:
            self.rb_f5.setStyleSheet(self.colorB)
        if (self.rb_f6.isChecked()):
            fuente = self.rb_f6.text()
            self.rb_f6.setStyleSheet(self.colorV)
        else:
            self.rb_f6.setStyleSheet(self.colorB)
        if (self.rb_f7.isChecked()):
            fuente = self.rb_f7.text()
            self.rb_f7.setStyleSheet(self.colorV)
        else:
            self.rb_f7.setStyleSheet(self.colorB)
        if (self.rb_f8.isChecked()):
            fuente = self.rb_f8.text()
            self.rb_f8.setStyleSheet(self.colorV)
        else:
            self.rb_f8.setStyleSheet(self.colorB)
        if (self.rb_f9.isChecked()):
            fuente = self.rb_f9.text()
            self.rb_f9.setStyleSheet(self.colorV)
        else:
            self.rb_f9.setStyleSheet(self.colorB)
        return fuente
    def activar(self):
        if(self.groupBox_5.isVisible()==False):
            self.groupBox_5.setVisible(True)
        else:
            self.groupBox_5.setVisible(False)
    def textoAlmacenamiento(self):
        almacenamiento = 0
        capacidad = 0
        if(self.rb_a1.isChecked()):
            almacenamiento = self.rb_a1.text()
            self.rb_a1.setStyleSheet(self.colorV)
        else:
            self.rb_a1.setStyleSheet(self.colorB)
        if (self.rb_a2.isChecked()):
            almacenamiento = self.rb_a2.text()
            self.rb_a2.setStyleSheet(self.colorV)
        else:
            self.rb_a2.setStyleSheet(self.colorB)
        if (self.rb_a3.isChecked()):
            almacenamiento = self.rb_a3.text()
            self.rb_a3.setStyleSheet(self.colorV)
        else:
            self.rb_a3.setStyleSheet(self.colorB)
        if (self.rb_a4.isChecked()):
            almacenamiento = self.rb_a4.text()
            self.rb_a4.setStyleSheet(self.colorV)
        else:
            self.rb_a4.setStyleSheet(self.colorB)
        if (self.groupBox_5.isVisible()):
            if (self.rb_c1.isChecked()):
                capacidad = self.rb_c1.text()
                self.rb_c1.setStyleSheet(self.colorV)
            else:
                self.rb_c1.setStyleSheet(self.colorB)
            if (self.rb_c2.isChecked()):
                capacidad = self.rb_c2.text()
                self.rb_c2.setStyleSheet(self.colorV)
            else:
                self.rb_c2.setStyleSheet(self.colorB)
            if (self.rb_c3.isChecked()):
                capacidad = self.rb_c3.text()
                self.rb_c3.setStyleSheet(self.colorV)
            else:
                self.rb_c3.setStyleSheet(self.colorB)
        return almacenamiento, capacidad
    def textoAgregar(self):
        cadena = f'Adicionalmente Usted Agrego: \n'
        count = 0
        if(self.cb_agregar1.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar1.text()},'
            self.cb_agregar1.setStyleSheet(self.colorV)
        else:
            self.cb_agregar1.setStyleSheet(self.colorB)
        if (self.cb_agregar2.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar2.text()},'
            self.cb_agregar2.setStyleSheet(self.colorV)
        else:
            self.cb_agregar2.setStyleSheet(self.colorB)
        if (self.cb_agregar3.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar3.text()},'
            self.cb_agregar3.setStyleSheet(self.colorV)
        else:
            self.cb_agregar3.setStyleSheet(self.colorB)
        if (self.cb_agregar4.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar4.text()},'
            self.cb_agregar4.setStyleSheet(self.colorV)
        else:
            self.cb_agregar4.setStyleSheet(self.colorB)
        if (self.cb_agregar5.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar5.text()},'
            self.cb_agregar5.setStyleSheet(self.colorV)
        else:
            self.cb_agregar5.setStyleSheet(self.colorB)
        if (self.cb_agregar6.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar6.text()},'
            self.cb_agregar6.setStyleSheet(self.colorV)
        else:
            self.cb_agregar6.setStyleSheet(self.colorB)
        if (self.cb_agregar7.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar7.text()},'
            self.cb_agregar7.setStyleSheet(self.colorV)
        else:
            self.cb_agregar7.setStyleSheet(self.colorB)
        if (self.cb_agregar8.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar8.text()},'
            self.cb_agregar8.setStyleSheet(self.colorV)
        else:
            self.cb_agregar8.setStyleSheet(self.colorB)
        if (self.cb_agregar9.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar9.text()},'
            self.cb_agregar9.setStyleSheet(self.colorV)
        else:
            self.cb_agregar9.setStyleSheet(self.colorB)
        if (self.cb_agregar10.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar10.text()},'
            self.cb_agregar10.setStyleSheet(self.colorV)
        else:
            self.cb_agregar10.setStyleSheet(self.colorB)
        if (self.cb_agregar11.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar11.text()},'
            self.cb_agregar11.setStyleSheet(self.colorV)
        else:
            self.cb_agregar11.setStyleSheet(self.colorB)
        if (self.cb_agregar12.isChecked()):
            count = 1
            cadena += f'{self.cb_agregar12.text()},'
            self.cb_agregar12.setStyleSheet(self.colorV)
        else:
            self.cb_agregar12.setStyleSheet(self.colorB)
        if (count!=1):
            cadena = 'Usted no agrego nada.'
        return cadena
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())