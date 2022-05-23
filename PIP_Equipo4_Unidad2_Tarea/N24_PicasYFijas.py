import sys, random
from QLabelClickeable import clickable
from PyQt5 import uic, QtWidgets,QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
qtCreatorFile = 'N24_PicasYFijas.ui' #Nombre del archivo aqui
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.L = []#Declaracion de la lista donde se guardara el numero aleatorio generado por la computadora
        self.usuario = [0,0,0,0]# Declaracion de la lista donde se guardaran los numeros aleatorios ingresados por el usuario
        self.j = 0#Variables auxiliares
        self.aux = 0#Variables auxiliares
        self.vidas = 0#Vidas del usuario
        self.picas = 0#picas
        self.fijas = 0#Fijas
        QMessageBox.information(self, '\tImportante', '🎰 Picas y Fijas 🎰\n\n'#Mensaje emergente con indicaciones de como empezar el juego
                                                      '🔴 Ingresa nombre del jugador\n\n'
                                                      '🔴 Ingresa la cantidad de intentos en el cual crees adivinar el número\n\n'
                                                      '🔴 Selecciona tu avatar\n\n'
                                                      '🔴 Finalmente dale al botón Comenzar, es importante seguir estos pasos o no podrás comenzar a jugar')

        #Area de Signals y configuraciones incicales
        self.btn_comenzar.clicked.connect(self.comenzar)#Boton comenzar enlazado a funcion comenzar
        self.ValidarN = QtGui.QIntValidator()#Variable validadora para el area de intentos
        self.txt_intentos.setValidator(self.ValidarN)#Validacion de solo numeros en el area de intentos
        self.gb_numeros.setEnabled(False)#Se deshabilita el group box para que no pueda ingresar nada antes de rellenar lo solicitado
        self.rb_1.toggled.connect(self.color1)#Radio Buttons enlazados a la funcion cambios de colores (Verde o negro)
        self.rb_2.toggled.connect(self.color2)
        self.rb_3.toggled.connect(self.color3)
        self.rb_4.toggled.connect(self.color4)
        self.colorV = f'background-color: rgb({0}, {255}, {0});' \
                      f'color: rgb({0}, {0}, {0});' \
                      f'border: 3px solid Green;' \
                      f'font: 48pt "Wide Latin";'#Declaracion de los colores para los radio buttons y labels de los numeros(Verde)
        self.colorB = f'background-color: rgb({0}, {0}, {0});' \
                      f'color: rgb({255}, {255}, {255});' \
                      f'border: 3px solid Black;' \
                      f'font: 48pt "Wide Latin";'#Declaracion de los colores para los radio buttons y labels de los numeros(Negro)
        self.rb_1.setStyleSheet(self.colorB)#Se establecen los  radio buttons en negro
        self.rb_2.setStyleSheet(self.colorB)
        self.rb_3.setStyleSheet(self.colorB)
        self.rb_4.setStyleSheet(self.colorB)
        self.btn_cambiar.clicked.connect(self.cambiar)#Boton cambiar enlazado a la funcion cambiar numero del usuario
        self.btn_elejir.clicked.connect(self.elegir)#Boton elejir para confirmar que el numero generado por el usuario es que quiere comprobar
        self.btn_comprobar.clicked.connect(self.comprobar)#Boton comprobar enlazado a la funcion para comprobar el numero ingresado por el usuario con el generado
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)
        self.milis = 0
        self.segundos = 0
        self.minutos = 0
        self.count = 1
        self.horizontalSlider.valueChanged.connect(self.cambioimg)#Horizontal Slider enlazado con la funcion cambio imagen para mostrar diferentes imagenes de personajes
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(44)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        ruta1 = 'C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/Personajes'#Ruta de la carpeta donde estaran los personajes
        self.listaimg = [f"{ruta1}/1.png",#Lista con las imagenes de los personajes
                         f"{ruta1}/2.png",
                         f"{ruta1}/3.png",
                         f"{ruta1}/4.png",
                         f"{ruta1}/5.png",
                         f"{ruta1}/6.png",
                         f"{ruta1}/7.png",
                         f"{ruta1}/8.png",
                         f"{ruta1}/9.png",
                         f"{ruta1}/10.png",
                         f"{ruta1}/11.png",
                         f"{ruta1}/12.png",
                         f"{ruta1}/13.png",
                         f"{ruta1}/14.png",
                         f"{ruta1}/15.png",
                         f"{ruta1}/16.png",
                         f"{ruta1}/17.png",
                         f"{ruta1}/18.png",
                         f"{ruta1}/19.png",
                         f"{ruta1}/20.png",
                         f"{ruta1}/21.png",
                         f"{ruta1}/22.png",
                         f"{ruta1}/23.png",
                         f"{ruta1}/24.png",
                         f"{ruta1}/25.png",
                         f"{ruta1}/26.png",
                         f"{ruta1}/27.png",
                         f"{ruta1}/28.png",
                         f"{ruta1}/29.png",
                         f"{ruta1}/30.png",
                         f"{ruta1}/31.png",
                         f"{ruta1}/32.png",
                         f"{ruta1}/33.png",
                         f"{ruta1}/34.png",
                         f"{ruta1}/35.png",
                         f"{ruta1}/36.png",
                         f"{ruta1}/37.png",
                         f"{ruta1}/38.png",
                         f"{ruta1}/39.png",
                         f"{ruta1}/40.png",
                         f"{ruta1}/41.png",
                         f"{ruta1}/42.png",
                         f"{ruta1}/43.png",
                         f"{ruta1}/44.png"
                         ]
        self.img_1.setPixmap(QtGui.QPixmap('C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/silueta.png'))#Ruta donde se establece incialmente el label de seleccion del personaje con una imagen de una silueta
        self.img_2.setPixmap(QtGui.QPixmap('C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/siluetab.png'))#Ruta donde se establece incialmente el label de seleccion del personaje con una imagen de una silueta completa
        ruta2 = 'C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/VistaPersonaje'#Ruta donde se encuentra la carpeta de vista de los personajes
        self.listaimg2 = [f"{ruta2}/1.png",#lista con la vista de los personajes
                         f"{ruta2}/2.png",
                         f"{ruta2}/3.png",
                         f"{ruta2}/4.png",
                         f"{ruta2}/5.png",
                         f"{ruta2}/6.png",
                         f"{ruta2}/7.png",
                         f"{ruta2}/8.png",
                         f"{ruta2}/9.png",
                         f"{ruta2}/10.png",
                         f"{ruta2}/11.png",
                         f"{ruta2}/12.png",
                         f"{ruta2}/13.png",
                         f"{ruta2}/14.png",
                         f"{ruta2}/15.png",
                         f"{ruta2}/16.png",
                         f"{ruta2}/17.png",
                         f"{ruta2}/18.png",
                         f"{ruta2}/19.png",
                         f"{ruta2}/20.png",
                         f"{ruta2}/21.png",
                         f"{ruta2}/22.png",
                         f"{ruta2}/23.png",
                         f"{ruta2}/24.png",
                         f"{ruta2}/25.png",
                         f"{ruta2}/26.png",
                         f"{ruta2}/27.png",
                         f"{ruta2}/28.png",
                         f"{ruta2}/29.png",
                         f"{ruta2}/30.png",
                         f"{ruta2}/31.png",
                         f"{ruta2}/32.png",
                         f"{ruta2}/33.png",
                         f"{ruta2}/34.png",
                         f"{ruta2}/35.png",
                         f"{ruta2}/36.png",
                         f"{ruta2}/37.png",
                         f"{ruta2}/38.png",
                         f"{ruta2}/39.png",
                         f"{ruta2}/40.png",
                         f"{ruta2}/41.png",
                         f"{ruta2}/42.png",
                         f"{ruta2}/43.png",
                         f"{ruta2}/44.png"
                         ]
        ruta4 = 'C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/Victorias'#Ruta donde se encuentra la carpeta de la pose de victoria de los personajes
        self.listaimg3 = [f"{ruta4}/1.png",#lista de imagenes con las poses de victoria de los personajes
                          f"{ruta4}/2.png",
                          f"{ruta4}/3.png",
                          f"{ruta4}/4.png",
                          f"{ruta4}/5.png",
                          f"{ruta4}/6.png",
                          f"{ruta4}/7.png",
                          f"{ruta4}/8.png",
                          f"{ruta4}/9.png",
                          f"{ruta4}/10.png",
                          f"{ruta4}/11.png",
                          f"{ruta4}/12.png",
                          f"{ruta4}/13.png",
                          f"{ruta4}/14.png",
                          f"{ruta4}/15.png",
                          f"{ruta4}/16.png",
                          f"{ruta4}/17.png",
                          f"{ruta4}/18.png",
                          f"{ruta4}/19.png",
                          f"{ruta4}/20.png",
                          f"{ruta4}/21.png",
                          f"{ruta4}/22.png",
                          f"{ruta4}/23.png",
                          f"{ruta4}/24.png",
                          f"{ruta4}/25.png",
                          f"{ruta4}/26.png",
                          f"{ruta4}/27.png",
                          f"{ruta4}/28.png",
                          f"{ruta4}/29.png",
                          f"{ruta4}/30.png",
                          f"{ruta4}/31.png",
                          f"{ruta4}/32.png",
                          f"{ruta4}/33.png",
                          f"{ruta4}/34.png",
                          f"{ruta4}/35.png",
                          f"{ruta4}/36.png",
                          f"{ruta4}/37.png",
                          f"{ruta4}/38.png",
                          f"{ruta4}/39.png",
                          f"{ruta4}/40.png",
                          f"{ruta4}/41.png",
                          f"{ruta4}/42.png",
                          f"{ruta4}/43.png",
                          f"{ruta4}/44.png"
                          ]
        self.lbl_nombre.setVisible(False)#Lugar donde aparecera el nombre en caso que pierda se establece como no visible
        self.lbl_nombre2.setVisible(False)  # Lugar donde aparecera el nombre en caso que gane se establece como no visible
        self.btn_reiniciar.setVisible(False)#Se desabilita el boton reinciar
        self.btn_reiniciar.setEnabled(False)#Se oculta el boton reinicar
        self.btn_reiniciar.clicked.connect(self.reiniciar)#Boton reinicar enlazado a la funcion reiniciar donde se establecen todos los valores como al principio
        self.control = 0
        self.img_3.setVisible(False)#Label donde aparecera la imagen con la frase you win o you lose sea dado el caso, se establece como oculto

    #Area de los Slots
    def cambioimg(self):
        #Funcion cambio imagen donde se guarda en una variable 'numero' el valor actual del horizontal Slider si este es diferente de 0 se cambia la imagen de acuerdo a la lista de imagenes
        #del personaje en cambio si este valor es 0 se establece la imagen de la silueta que estaba establecida al principio
        numero = self.horizontalSlider.value()
        if(numero!=0):
            self.img_1.setPixmap(QtGui.QPixmap(self.listaimg[numero-1]))
        else:
            ruta3 = 'C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/silueta.png'
            self.img_1.setPixmap(QtGui.QPixmap(ruta3))
    def unico(self, x, lista):
        #Funcion unico nos devuelve un valor booleano dado una variable tipo int y una lista donde recorre la lista y comprueba en ella que el valor x no este
        #, si no esta devuelve un True si este ya se encuentra en la lista devuelve un False y sale del ciclo for, retornando el valor booleano
        esUnico = True
        for i in range(len(lista)):
            if x == lista[i]:
                esUnico = False
                break
        return esUnico
    def comenzar(self):
        #Funcion comenzar se guardan lo ingresado en los line text de nombre, intentos, asi como tambien el valor actual de el Horizontal Slider, y se comprueba que estos espacios no esten vacios para
        #en el nombre y en el numero de intentos, con if(len(variable)==0, en el caso del horizontal Slider y su valor se compara igual sabiendo que si este es 0 no se habra escogido ningun personaje
        #si una vez comprobado que estos sean diferentes de 0, entra al siguiente if donde se hace la comparacion de que cada uno de los datos sean diferentes de 0, para cada caso que sea igual a 0 saltara
        #Una ventana emergente diciendo que tal espacio esta vacio o no se selecciono
        nombre = self.txt_nombre.text()
        intentos = self.txt_intentos.text()
        valor = self.horizontalSlider.value()
        if(len(intentos)==0):
            QMessageBox.information(self, '\tImportante', 'USTED DEBE INGRESAR UN NUMERO DE INTENTOS')
        if(len(nombre)==0):
            QMessageBox.information(self, '\tImportante', 'USTED DEBE INGRESAR UN NOMBRE')
        if (valor == 0):
            QMessageBox.information(self, '\tImportante', 'SELECCIONE UN PERSONAJE EN LA BARRA ROJA DE ABAJO DEL PERSONAJE')
        if ((len(intentos) != 0) and (len(nombre) != 0) and (valor!= 0)):
            #Entrado en este if el numero de intentos se convierte a tipo entero, y este se guarda en self.vidas que seran las vidas del usuario, asi como otra condicion donde se evaluara que el numero de intentos
            #ingresado sea mayor a 4 si esto no es asi saltara un ventana emergente diciendo que el numero de intentos debe ser mayor a 4, una vez corrobarado que sea mayor a 4, entrara al else
            intentos = int(intentos)
            self.vidas = intentos
            if (intentos < 4):
                QMessageBox.information(self, '\tImportante', 'EL NUMERO DE INTENTOS DEBE SER IGUAL O MAYOR A 4')
            else:
                #dentro de este else ya habriamos comprobado que los text line no esten vacios asi como el numero de intentos sea mayor a 4  y asi como tambien que el usuario escogiera un personaje enseguida
                #se generara un numero random de 4 digitos, haciendo que mientras j una variable auxiliar sea menor a 4 se generara el primer digito random y enseguida se comprobara con la funcion unico
                #si la funcion unico nos regresa un True indicando que el numero x comparado con la lista no esta en ella a lo que procedera a agregarse en esta e incrementando j + 1, y asi hasta que la variable j
                #sea 4 saldra del ciclo while
                while self.j < 4:
                    x = random.randint(1, 9)
                    if self.unico(x, self.L):
                        self.L.append(x)
                        self.j += 1
                self.btn_comenzar.setEnabled(False)#Se deshabilita el boton comenzar
                self.horizontalSlider.setEnabled(False)#Se deshabilita el horizontal Slider
                self.txt_nombre.setEnabled(False)#Se deshabilita el ingreso de un nombre
                self.txt_intentos.setEnabled(False)#se deshabilita el ingreso de intentos
                self.gb_numeros.setEnabled(True)#Se habilita groupBox donde se encuentran el area de ingreso del numero de usuario
                self.rb_1.setChecked(True)#Primer radio button se establece como True mientras que los otros 3 se establece en False
                self.rb_2.setChecked(False)
                self.rb_3.setChecked(False)
                self.rb_4.setChecked(False)
                self.rb_1.setEnabled(True)#Los radioButtons se establecen como verdaderos para que el usuario pueda seleccionar un radio button y generar un numero aleatorio en el lugar seleccionado
                self.rb_2.setEnabled(True)
                self.rb_3.setEnabled(True)
                self.rb_4.setEnabled(True)
                self.btn_cambiar.setEnabled(True)#Boton cambiar se establece como habilitado para que el usuario cambie el numero en el lugar del radio button seleccionado
                self.btn_elejir.setEnabled(False)#Se deshabilita el boton elegir
                self.btn_comprobar.setEnabled(False)#Se deshabilita el boton comprobar
                #Mensaje emergente donde se le da al usuario como funciona el juego asi como el uso de los botones
                QMessageBox.information(self, '\tImportante', '🎰 Estas apunto de comenzar a jugar Picas y Fijas 🎰\n\n'
                                                              '🔴 "Debes ingresar un numero de 4 dígitos"\n'
                                                              '   ♦Seleccionar el circulo de arriba marcado en verde\n'
                                                              '   ♦Pulsar el boton amarillo para crear un digito, cambiar un digito o cambiar el numero\n'
                                                              '   ♦Pulsar el boton verde para elegir el numero creado\n'
                                                              '   ♦Pulsar el boton rojo para comprobar tu "numero" elegido con el numero generado\n\n'
                                                              '🔴 EL juego te mostrara cuantos fueron fijas y cuantos picas\n\n'
                                                              '🔴 Fijas: Número correcto en la posición correcta\n\n'
                                                              '🔴 Picas: Número correcto en la posición incorrecta\n\n'
                                                              '🔴 El juego termina cuando se te acaben los intentos o cuando adivines el número\n\n',QMessageBox.Ok)
                #cambios se establece para cambiar el fondo a color negro donde se mostrara al personaje seleccionado
                cambios = f'background-color: rgb({255}, {255}, {255});' \
                              f'border: 10px solid Black;' \
                              f'border-radius: 10px;'
                self.img_2.setStyleSheet(cambios)#Se modifaca el label con cambios
                self.img_2.setPixmap(QtGui.QPixmap(self.listaimg2[self.horizontalSlider.value()-1]))#Se establece la imagen del personaje en el label correspondiente con el valor del slider - 1
                self.segundoPlano.start(10)#Se inicia el temporizador
                self.btn_reiniciar.setEnabled(False)#Se deshabilita el boton iniciar
    def cambiar(self):
        #Funcion cambiar cambia el digito seleccionado con el radioButton
        self.btn_comprobar.setEnabled(False)#Se deshabilita el boton comprobar
        opcion = self.btn_cambiar.text()#opcion guarda el texto del boton amarillo
        #Si opcion es cambiar numero se establece el radio button en verde como habilitado mientras que los demas tambien se habilitan para que pueda seleccionar cual posicion, cambiar el digito y se cambia el texto
        #del boton a cambiar digito y entra al else
        if(opcion =='Cambiar Numero'):
            if (self.rb_1.isChecked()):
                self.lbl_1.setEnabled(True)
                self.rb_1.setEnabled(True)
            else:
                self.rb_1.setEnabled(True)
            if (self.rb_2.isChecked()):
                self.rb_2.setEnabled(True)
                self.lbl_2.setEnabled(True)
            else:
                self.rb_2.setEnabled(True)
            if (self.rb_3.isChecked()):
                self.rb_3.setEnabled(True)
                self.lbl_3.setEnabled(True)
            else:
                self.rb_3.setEnabled(True)
            if (self.rb_4.isChecked()):
                self.rb_4.setEnabled(True)
                self.lbl_4.setEnabled(True)
            else:
                self.rb_4.setEnabled(True)
            self.btn_cambiar.setText('Cambiar digito')
        else:
            #dentro del else se establece un valor booleano como Falso para que sea la validacion del ciclo while
            validar = False
            while validar != True:
                #mientras que validar sea diferente de True este ciclo seguira
                x = random.randint(1, 9)#Se genera un numero random
                if self.unico(x, self.usuario):#Se llama a la funcion unico
                    #Si unico nos regresa un True el numero random generado del 1 al 9 se agrega a la lista de los numeros del usuario en un indice en especifico apoyandonos de la varible aux
                    #Despues se elimina el valor del indice en aux + 1
                    self.usuario.insert(self.aux, x)
                    self.usuario.pop(self.aux + 1)
                    #Se comprueba en que posicion se agregara el numero generado con el uso del radiobutton si esta seleccionado
                    if (self.rb_1.isChecked()):
                        self.lbl_1.setText(str(x))
                    if (self.rb_2.isChecked()):
                        self.lbl_2.setText(str(x))
                    if (self.rb_3.isChecked()):
                        self.lbl_3.setText(str(x))
                    if (self.rb_4.isChecked()):
                        self.lbl_4.setText(str(x))
                    validar = True#validar cambia a True haciendo que el ciclo while termine
            #Se guardan los valores de los labels donde se muestran los numeros del usuario
            n1 = self.lbl_1.text()
            n2 = self.lbl_2.text()
            n3 = self.lbl_3.text()
            n4 = self.lbl_4.text()
            #Si el usuario no ha generado un numero para todos las posiciones de los digitos el boton elegir quedara inhabilitado hasta que esto cambie
            if((len(n1)!=0) and (len(n2)!=0) and (len(n3)!=0) and (len(n4)!=0)):
                self.btn_elejir.setEnabled(True)
    def elegir(self):
        #Funcion Elegir deshabilita la seleccion para el cambio de numeros asi como tambien asimismo, como tambien cambia el texto del boton amarillo a cambiar numero
        #Y por ultimo se habilita el boton para comprobar el numero del usuario con el generado
        self.lbl_1.setEnabled(False)
        self.lbl_2.setEnabled(False)
        self.lbl_3.setEnabled(False)
        self.lbl_4.setEnabled(False)
        self.rb_1.setEnabled(False)
        self.rb_2.setEnabled(False)
        self.rb_3.setEnabled(False)
        self.rb_4.setEnabled(False)
        self.btn_elejir.setEnabled(False)
        self.btn_cambiar.setText('Cambiar Numero')
        self.btn_comprobar.setEnabled(True)
    def comprobar(self):
        #Funcion comprobar esta funcion comprobara el numero del usuario con el numero generado por la computadora y mostrara ventanas emergentes señalando el estado actual de pijas y picas asi como vidas restantes
        #con variaciones de si gano se mostrara la leyenda de usted gano y si perdio se mostrara la leyenda mas suerte para la proxima, asi como tambien agregando en un listview vidas, picas, fijas y tiempo en que
        #se intento o se gasto una vida
        picas = 0
        fijas = 0
        self.vidas -= 1#Se reduce la vida en uno ya que el usuario comprobo el numero
        # Se hace el chequeo de cuantos numeros son picas y cuantas fijas de los ingresados por el usuario
        for i in range(len(self.L)):
            if (self.usuario[i] == self.L[i]):
                # si el numero del usuario en la posicion i es igual al numero generado en la misma posicion esta sera una fija
                fijas += 1  # aumenta el valor de fijas
        for e in self.usuario:
            if ((e in self.L) == True):
                # Si el elemento e esta en la lista nos retornara un True y esta sera pica
                picas += 1  # aumenta el numero de picas
        self.picas = picas - fijas  # Se saca el verdadero valor de las picas restandoles las fijas
        self.fijas = fijas  # se guardan las fijas en self.fijas para usarlas en otras funciones
        # Se obtiene el valor de los labels del cronometro
        milisegundos = self.lbl_milis.text()
        minutos = self.lbl_min.text()
        segundos = self.lbl_seg.text()
        # Se hace una cadena con las vidas, picas, fijas, y el tiempo
        cadena = f'Vidas: {self.vidas}.❤ - Picas: {self.picas}. - Fijas: {self.fijas}. - Tiempo {self.count}.- {minutos} : {segundos} : {milisegundos}'
        self.listWidget.addItem(cadena)  # Se añade la cadena en el listView
        if(self.vidas!=0):#Si el usuario todavia tiene vidas entra en este if
            if (fijas != 4):#Si las fijas todavia no son las 4 entra en el if
                #Muestra un ventana emergente mostrando el estado actual de vidas, picas, y fijas
                QMessageBox.information(self, '\tImportante', f'🎰 Picas y Fijas 🎰\n\n'
                                                          f'🔴 Numero de Picas Actuales: {self.picas}\n\n'
                                                          f'🔴 Numero de fijas Actuales: {self.fijas}\n\n'
                                                          f'🔴 Vidas restantes {self.vidas}❤️\n\n'
                                                          f'🔴 Se te acaba el tiempo esponja')
                self.count += 1#Aumenta contador para el numero de intentos
                print(self.L)
            else:#Si las fijas todas son 4 entra en el else
                if (self.segundoPlano.isActive()):
                    self.segundoPlano.stop()#Se detiene el temporizador si esta activado
                self.img_3.setPixmap(QtGui.QPixmap('C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/win1.jpg'))#Se establece la imagen donde se mostrara you win
                self.img_3.setVisible(True)#Se hace visible el label donde se mostrara la imagen de you win
                #Muestra un mensaje emergente indicando que el usuario gano mostrando el numero que adivino asi como el numero de intentos en que lo logro asi como el tiempo transcurrido y las vidas restantes
                QMessageBox.information(self, f'\tFelicidades Ganastes', f'🎰 Picas y Fijas 🎰\n\n'
                                                              f'🔴 Felicidades Ganastes: "{self.txt_nombre.text()}"\n\n'
                                                              f'🔴 Numero adivinado: {self.L}\n\n'
                                                              f'🔴 Numero de intentos: {self.count}\n\n'
                                                              f'🔴 Tiempo transcurrido: {minutos} : {segundos} : {milisegundos}\n\n'
                                                              f'🔴 Vidas sobrantes {self.vidas} ❤\n\n'
                                                              f'🔴 Ganaste Esponja!!!!\n'
                                                                         '⠄⠄⠄⠄⢀⣠⣶⣶⣶⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⣄⡀⠄⠄⠄⠄⠄\n'
                                                                         '⠄⠄⠄⢠⣾⡟⠁⠄⠈⢻⣿⡀⠄⠄⠄⠄⠄⠄⠄⣼⣿⡿⠋⠉⠻⣷⠄⠄⠄⠄\n'
                                                                         '⠄⠄⠄⢸⣿⣷⣄⣀⣠⣿⣿⡇⠄⠄⠄⠄⠄⠄⢰⣿⣿⣇⠄⠄⢠⣿⡇⠄⠄⠄\n'
                                                                         '⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄\n'
                                                                         '⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄\n'
                                                                         '⠄⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄\n'
                                                                         '⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄\n'
                                                                         '⠄⣿⣿⣿⣿⣿⡏⣍⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣩⡍⣿⣿⣿⣷⠄\n'
                                                                         '⠄⣿⣿⣿⣿⣿⣇⢿⠻⠮⠭⠭⠭⢭⣭⣭⣭⣛⣭⣭⠶⠿⠛⣽⢱⣿⣿⣿⣿⠄\n'
                                                                         '⠄⣿⣿⣿⣿⣿⣿⣦⢱⡀⠄⢰⣿⡇⠄⠄⠄⠄⠄⠄⠄⢀⣾⢇⣿⣿⣿⣿⡿⠄\n'
                                                                         '⠄⠻⢿⣿⣿⣿⢛⣭⣥⣭⣤⣼⣿⡇⠤⠤⠤⣤⣤⣤⡤⢞⣥⣿⣿⣿⣿⣿⠃⠄\n'
                                                                         '⠄⠄⠄⣛⣛⠃⣿⣿⣿⣿⣿⣿⣿⢇⡙⠻⢿⣶⣶⣶⣾⣿⣿⣿⠿⢟⣛⠃⠄⠄\n'
                                                                         '⠄⠄⣼⣿⣿⡘⣿⣿⣿⣿⣿⣿⡏⣼⣿⣿⣶⣬⣭⣭⣭⣭⣭⣴⣾⣿⣿⡄⠄⠄\n'
                                                                         '⠄⣼⣿⣿⣿⣷⣜⣛⣛⣛⣛⣛⣀⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄\n'
                                                                         '⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣭⣙⣛⣛⣩⣭⣭⣿⣿⣿⣿⣷⡀\n')
                #cambios se modifica el label donde se mostrara la imagen del personaje en pose de victoria
                cambios = f'background-color: rgb({0}, {0}, {0});' \
                          f'border: 10px solid Black;' \
                          f'border-radius: 10px;'

                self.img_2.setStyleSheet(cambios)#Se modifica el label
                self.img_2.setPixmap(QtGui.QPixmap(self.listaimg3[self.horizontalSlider.value()-1]))#Se establece la imagen del personaje en el label correspondiente con el valor del slider - 1
                self.lbl_nombre2.setText(self.txt_nombre.text().upper())  # Se modifica el label para mostrar el nombre en la imagen you win
                self.lbl_nombre2.setVisible(True)  # Se hace visible el label donde se mostrara el nombre que se ingreso
                self.btn_cambiar.setEnabled(False)#Se deshabilita el boton cambiar
                self.btn_comprobar.setEnabled(False)#Se deshabilita el boton comprobar
                #Se establece los valores del cronometro en 0
                self.milis = 0
                self.segundos = 0
                self.minutos = 0
                self.count = 0
                self.lbl_milis.setText(str(self.milis))
                self.lbl_min.setText(str(self.minutos))
                self.lbl_seg.setText(str(self.segundos))
                self.btn_reiniciar.setEnabled(True)#Se habilita el boton iniciar
                self.btn_reiniciar.setVisible(True)#Se hace visible el boton iniciar
        else:#Si las vidas del usuario llegan a 0
            if (self.segundoPlano.isActive()):
                self.segundoPlano.stop()#Se detiene el temporizador si esta activado
            self.img_3.setPixmap(QtGui.QPixmap('C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/lose1.jpg'))#Se establece la imagen donde se mostrara you lose
            self.img_3.setVisible(True)# Se hace visible el label donde se mostrara la imagen de you lose
            # Muestra un mensaje emergente indicando que el usuario perdio mostrando el numero que no adivino asi como el numero de intentos que hizo asi como el timepo transcurrido y las vidas
            QMessageBox.information(self, f'\tPerdistes esta vez', f'🎰 Picas y Fijas 🎰\n\n'
                                                                     f'🔴 Haz perdido: "{self.txt_nombre.text()}", mas suerte para la proxima\n\n'
                                                                     f'🔴 Numero que se debia adivinar: {self.L}\n\n'
                                                                     f'🔴 Numero de intentos: {self.count}\n\n'
                                                                     f'🔴 Tiempo transcurrido: {minutos} : {segundos} : {milisegundos}\n\n'
                                                                     f'🔴 Vidas: {self.vidas} ❤ , como tu cuenta de banco\n\n'
                                                                     f'🔴 Mas suerte para la proxima Esponja\n'
                                                                   '⣿⢳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⠄\n'
                                                                   '⢣⣿⣿⡿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠄⠄\n'
                                                                   '⣾⣿⡿⣱⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⢋⢿⣏⡻⣿⣿⣿⣿⣿⣿⣿⣷⡄⠄\n'
                                                                   '⣿⡿⣽⣿⣿⣿⣿⣷⣌⠛⢱⣿⣿⣿⡟⡫⠾⢸⣧⠹⠊⢻⣿⣿⣿⡟⣿⣿⡝⣦\n'
                                                                   '⣿⢳⣿⣿⣿⣿⠟⢕⣛⠇⣦⣍⠻⠫⠼⠓⣘⢸⡟⠸⣛⣓⡛⢿⣿⡇⣝⢿⣷⡈\n'
                                                                   '⠃⣿⣿⢟⣫⣶⣾⣿⣿⠘⠋⣡⢨⠉⠩⣭⣔⠘⠡⠝⢒⢠⠄⠘⡟⣷⢿⣯⢻⡇\n'
                                                                   '⡟⠟⡕⣛⣿⣭⣽⣶⣶⡑⢿⡇⠐⠈⠄⣸⠿⠾⠰⠿⣇⠄⠄⠁⢀⣿⠘⢻⠸⡇\n'
                                                                   '⢱⣿⡇⣿⣿⣿⣿⣿⣿⣏⡳⠶⠶⠶⢖⣒⣚⣩⣾⣷⣶⣶⣶⣿⡟⠋⠄⠸⠁⠁\n'
                                                                   '⡸⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣭⣾⣿⣿⣷⣮⣭⣭⣭⣭⡅⠄⠄⠄⠄⠄\n'
                                                                   '⣷⢹⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄\n'
                                                                   '⣿⢸⡇⣿⣿⣿⡿⣩⣶⡶⢶⣶⣮⣭⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣛⣣⠄⠄⠄⠄\n'
                                                                   '⣿⢸⡇⣿⣿⣏⢧⡛⠿⠿⠷⠶⢶⣤⣭⣛⣛⠿⠿⠿⢟⣛⣛⣛⣛⠁⠄⠄⠄⠄\n'
                                                                   '⣙⢸⢃⣿⣿⣿⣦⣿⣿⣿⣿⣿⣷⣶⣭⣭⣭⣭⣭⣭⣭⡭⠉⠋⠁⠄⠄⠄⠄⠄\n'
                                                                   '⣿⣨⣒⠤⢬⣭⣝⣛⡻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠛⠄⠄⠄⠄⠄⠄⠄⠄⠄\n'
                                                                   '⣿⣿⣿⣿⣷⣶⣶⣭⣭⣭⣭⣭⣭⣭⣭⣭⣭⣵⣶⣦⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n')
            # cambios se modifica el label donde se mostrara la imagen de una lapida
            cambios = f'border: 10px solid Black;' \
                      f'border-radius: 10px;'
            self.img_2.setStyleSheet(cambios)#Se modifica el label
            self.img_2.setPixmap(QtGui.QPixmap('C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/rip.png'))#Se establece la imagen de rip en el label indicado
            self.lbl_nombre.setText(self.txt_nombre.text().upper())#Se modifica el label para mostrar el nombre en la lapida
            self.lbl_nombre.setVisible(True)#Se hace visible el label donde se mostrara el nombre que se ingreso
            self.btn_cambiar.setEnabled(False)#Se deshabilita el boton cambiar
            self.btn_comprobar.setEnabled(False)#Se deshabilita el boton comprobar
            self.btn_reiniciar.setEnabled(True)#Se habilita el boton reiniciar
            self.btn_reiniciar.setVisible(True)#Se hace visible el boton reiniciar
            # Se establece los valores del cronometro en 0
            self.milis = 0
            self.segundos = 0
            self.minutos = 0
            self.count = 0
            self.lbl_milis.setText(str(self.milis))
            self.lbl_min.setText(str(self.minutos))
            self.lbl_seg.setText(str(self.segundos))
        self.btn_comprobar.setEnabled(False)#Se deshabilita a si mismo el boton en cualquier caso
    def reiniciar(self):
        #reinicia los valores al estado inical asi como todo los objetos de la interfaz a como estaban en el inicio
        self.btn_comenzar.setEnabled(True)
        self.horizontalSlider.setEnabled(True)
        if (self.segundoPlano.isActive()):
            self.segundoPlano.stop()
        self.milis = 0
        self.segundos = 0
        self.minutos = 0
        self.count = 0
        self.lbl_milis.setText(str(self.milis))
        self.lbl_min.setText(str(self.minutos))
        self.lbl_seg.setText(str(self.segundos))
        self.rb_1.setChecked(True)
        self.rb_2.setChecked(False)
        self.rb_3.setChecked(False)
        self.rb_4.setChecked(False)
        self.lbl_1.setText('')
        self.lbl_2.setText('')
        self.lbl_3.setText('')
        self.lbl_4.setText('')
        self.lbl_nombre.setVisible(False)
        self.lbl_nombre2.setVisible(False)
        self.txt_nombre.setEnabled(True)
        self.txt_intentos.setEnabled(True)
        self.gb_numeros.setEnabled(False)
        self.btn_reiniciar.setVisible(False)
        self.listWidget.clear()
        self.horizontalSlider.setValue(0)
        ruta3 = 'C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/siluetab.png'
        self.img_2.setPixmap(QtGui.QPixmap(ruta3))
        ruta3 = 'C:/a/PIP_Equipo4_Unidad2_Tarea/imagenes/silueta.png'
        self.img_1.setPixmap(QtGui.QPixmap(ruta3))
        self.img_3.setVisible(False)
        self.btn_reiniciar.setEnabled(False)
        self.L.clear()
        self.j = 0
    def temporizador(self):
        #Funcion temporizador modifica los valores de los labels para simular un temporizador
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
    #las funciones colores se enlazan con la seleccion de los radioButton para hacer el cambio correspondiente tanto de los radioButtons asi como de los labels que estan debajo
    # ya sea color verde o negro si se establece en verde modifica tambien el color del numero en negro mientras que el color esta en negro se establece el color de los numeros en blanco
    def color1(self):
        self.aux = 0
        if (self.rb_1.isChecked()):
            self.rb_1.setStyleSheet(self.colorV)
            self.lbl_1.setStyleSheet(self.colorV)
            self.lbl_2.setEnabled(False)
            self.lbl_3.setEnabled(False)
            self.lbl_4.setEnabled(False)
        else:
            self.rb_1.setStyleSheet(self.colorB)
            self.lbl_1.setStyleSheet(self.colorB)
            self.lbl_2.setEnabled(True)
            self.lbl_3.setEnabled(True)
            self.lbl_4.setEnabled(True)
    def color2(self):
        self.aux = 1
        if (self.rb_2.isChecked()):
            self.rb_2.setStyleSheet(self.colorV)
            self.lbl_2.setStyleSheet(self.colorV)
            self.lbl_1.setEnabled(False)
            self.lbl_3.setEnabled(False)
            self.lbl_4.setEnabled(False)
        else:
            self.rb_2.setStyleSheet(self.colorB)
            self.lbl_2.setStyleSheet(self.colorB)
            self.lbl_1.setEnabled(True)
            self.lbl_3.setEnabled(True)
            self.lbl_4.setEnabled(True)
    def color3(self):
        self.aux = 2
        if (self.rb_3.isChecked()):
            self.rb_3.setStyleSheet(self.colorV)
            self.lbl_3.setStyleSheet(self.colorV)
            self.lbl_1.setEnabled(False)
            self.lbl_2.setEnabled(False)
            self.lbl_4.setEnabled(False)
        else:
            self.rb_3.setStyleSheet(self.colorB)
            self.lbl_3.setStyleSheet(self.colorB)
            self.lbl_1.setEnabled(True)
            self.lbl_2.setEnabled(True)
            self.lbl_4.setEnabled(True)
    def color4(self):
        self.aux = 3
        if (self.rb_4.isChecked()):
            self.rb_4.setStyleSheet(self.colorV)
            self.lbl_4.setStyleSheet(self.colorV)
            self.lbl_1.setEnabled(False)
            self.lbl_2.setEnabled(False)
            self.lbl_3.setEnabled(False)
        else:
            self.rb_4.setStyleSheet(self.colorB)
            self.lbl_4.setStyleSheet(self.colorB)
            self.lbl_1.setEnabled(True)
            self.lbl_2.setEnabled(True)
            self.lbl_3.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())