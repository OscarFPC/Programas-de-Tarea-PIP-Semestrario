#10 preguntas verdadero falso y
# que solo sea un examen de 5 preguntas aleatorias
# con cuenta regresiva
import sys, random

from PyQt5 import uic, QtWidgets,QtGui, QtCore

qtCreatorFile = 'N20_ExamenConTiempo.ui' #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Area de Signals y configuraciones incicales
        self.btn_empezar.clicked.connect(self.empezar)
        self.lbl_respuestas.setVisible(False)
        self.btn_min.setVisible(False)
        self.btn_seg.setVisible(False)
        self.rb_a.setEnabled(False)
        self.rb_b.setEnabled(False)
        self.rb_c.setEnabled(False)
        self.rb_d.setEnabled(False)
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)
        self.segundos = 0
        self.minutos = 2
        self.lista = []
        self.respuestasExamen = [18,5,14,27,100,400,25,21,25,15.5,3.1416,110,104,122,11,1005,1,12.6,26.33,1210]
        self.respuesta = []
        self.L = []
        self.j = 0
        self.aux = 0
    #Area de los Slots
    def empezar(self):
        msj = QtWidgets.QMessageBox()
        opcion = self.btn_empezar.text()
        if(opcion == 'Iniciar Examen'):
            msj.setText('Iniciado este Examen dispondra de solo 2 minutos para cada respuesta ')
            msj.exec()
            dataFile = open('Preguntas.csv', 'r')
            for linea in dataFile:
                renglon = linea.strip().split(',')
                for e in renglon:
                    string = e
                    characters = "'"
                    #print(string)
                    for x in range(len(characters)):
                        string = string.replace(characters[x], "")
                    #print(string)
                self.lista.append(renglon)
            print(self.lista)
            self.rb_a.setEnabled(True)
            self.rb_b.setEnabled(True)
            self.rb_c.setEnabled(True)
            self.rb_d.setEnabled(True)
            self.btn_min.setVisible(True)
            self.btn_seg.setVisible(True)
            self.btn_empezar.setText('Confimar Respuesta')
            def unico(x, L):
                esUnico = True
                for i in range(len(L)):
                    if x == L[i]:
                        esUnico = False
                        break
                return esUnico
            while self.j < 11:
                x = random.randint(0, 19)
                if unico(x, self.L):
                    self.L.append(x)
                    self.j += 1
            print(self.L, self.j)
            self.segundoPlano.start(1000)
            self.lbl_pregunta.setText(str(self.lista[int(self.L[self.aux])][0]))
            self.rb_a.setText(str(self.lista[int(self.L[self.aux])][1]))
            self.rb_b.setText(str(self.lista[int(self.L[self.aux])][2]))
            self.rb_c.setText(str(self.lista[int(self.L[self.aux])][3]))
            self.rb_d.setText(str(self.lista[int(self.L[self.aux])][4]))
        else:
            self.aux += 1
            if(self.aux<self.j):
                if (self.rb_a.isChecked()):
                    seleccion = self.rb_a.text()
                elif (self.rb_b.isChecked()):
                    seleccion = self.rb_b.text()
                elif (self.rb_c.isChecked()):
                    seleccion = self.rb_c.text()
                elif (self.rb_d.isChecked()):
                    seleccion = self.rb_d.text()
                else:
                    seleccion = 0
                print(seleccion)
                self.respuesta.append(seleccion)
                self.lbl_pregunta.setText(str(self.lista[int(self.L[self.aux])][0]))
                self.rb_a.setText(str(self.lista[int(self.L[self.aux])][1]))
                self.rb_b.setText(str(self.lista[int(self.L[self.aux])][2]))
                self.rb_c.setText(str(self.lista[int(self.L[self.aux])][3]))
                self.rb_d.setText(str(self.lista[int(self.L[self.aux])][4]))
                self.minutos = 2
                self.segundos = 0
            else:
                self.lbl_pregunta.setText('El examen termino')
                self.rb_a.setText('A')
                self.rb_b.setText('B')
                self.rb_c.setText('C')
                self.rb_d.setText('D')
                self.rb_a.setEnabled(False)
                self.rb_b.setEnabled(False)
                self.rb_c.setEnabled(False)
                self.rb_d.setEnabled(False)
                self.btn_min.setVisible(False)
                self.btn_seg.setVisible(False)
                self.btn_empezar.setText('Ver Calificacion')
                self.segundoPlano.stop()
        if (opcion == 'Ver Calificacion'):
            count = 0
            tam = len(self.L)
            for i in range(len(self.respuesta)):
                a = float(self.respuesta[i])
                b = float(self.respuestasExamen[self.L[i]])
                print(a,',',b)
                if (a == b):
                    count += 1
            print(f'Tuvo un total de: {count} preguntas correctas, de {tam-1}')
            self.lbl_respuestas.setVisible(True)
            self.lbl_respuestas.setText(f'Tuvo un total de: \n'
                                        f'{count}\n'
                                        f'preguntas correctas,\n'
                                        f'de un total de:\n'
                                        f' {tam-1}')
            self.btn_empezar.setVisible(False)
        self.groupBox.setChecked(False)
        self.rb_a.setChecked(False)
        self.rb_b.setChecked(False)
        self.rb_c.setChecked(False)
        self.rb_d.setChecked(False)
    def temporizador(self):
        self.segundos -= 1
        if ((self.segundos == 0) and (self.minutos == 0)):
            self.aux += 1
            if (self.aux < self.j):
                if (self.rb_a.isChecked()):
                    seleccion = self.rb_a.text()
                elif (self.rb_b.isChecked()):
                    seleccion = self.rb_b.text()
                elif (self.rb_c.isChecked()):
                    seleccion = self.rb_c.text()
                elif (self.rb_d.isChecked()):
                    seleccion = self.rb_d.text()
                else:
                    seleccion = 0
                print(seleccion)
                self.respuesta.append(seleccion)
                self.lbl_pregunta.setText(str(self.lista[int(self.L[self.aux])][0]))
                self.rb_a.setText(str(self.lista[int(self.L[self.aux])][1]))
                self.rb_b.setText(str(self.lista[int(self.L[self.aux])][2]))
                self.rb_c.setText(str(self.lista[int(self.L[self.aux])][3]))
                self.rb_d.setText(str(self.lista[int(self.L[self.aux])][4]))
                self.minutos = 2
                self.segundos = 0
            else:
                self.lbl_pregunta.setText('El examen termino')
                self.rb_a.setText('A')
                self.rb_b.setText('B')
                self.rb_c.setText('C')
                self.rb_d.setText('D')
                self.rb_a.setEnabled(False)
                self.rb_b.setEnabled(False)
                self.rb_c.setEnabled(False)
                self.rb_d.setEnabled(False)
                self.btn_min.setVisible(False)
                self.btn_seg.setVisible(False)
                self.btn_empezar.setText('Ver Calificacion')
                self.segundoPlano.stop()
            self.groupBox.setChecked(False)
            self.rb_a.setChecked(False)
            self.rb_b.setChecked(False)
            self.rb_c.setChecked(False)
            self.rb_d.setChecked(False)
        if (self.segundos == -1):
            self.minutos -= 1
            self.segundos = 59
        self.btn_min.setText(str(self.minutos))
        self.btn_seg.setText(str(self.segundos))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())