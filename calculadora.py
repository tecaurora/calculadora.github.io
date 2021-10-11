from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import math

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        #Seteamos los operadores
        self.operador1 = ""
        self.operador2 = ""
        self.ban = ""
        #Seteamos el tipo de operación a realizar
        self.operacion = ""
        #Listeners de Eventos de los botones de los números
        self.boton1.clicked.connect(self.click_1)
        self.boton2.clicked.connect(self.click_2)
        self.boton3.clicked.connect(self.click_3)
        self.boton4.clicked.connect(self.click_4)
        self.boton5.clicked.connect(self.click_5)
        self.boton6.clicked.connect(self.click_6)
        self.boton7.clicked.connect(self.click_7)
        self.boton8.clicked.connect(self.click_8)
        self.boton9.clicked.connect(self.click_9)
        self.boton0.clicked.connect(self.click_0)
        #Listeners de Eventos de los botones de las operaciones
        self.suma.clicked.connect(self.sumar)
        self.resta.clicked.connect(self.restar)
        self.producto.clicked.connect(self.multiplicar)
        self.division.clicked.connect(self.dividir)
        self.potencia.clicked.connect(self.potencias)
        self.raiz.clicked.connect(self.raiz2)
        self.igual.clicked.connect(self.resultado)
        self.borrartodo.clicked.connect(self.eliminarTodo) 
        self.borrar.clicked.connect(self.borrardigito) 

    def sumar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == ""):
            self.operador1 = eval(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "suma"
        else:
            self.operador2 = eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador1+self.operador2))

    def restar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == ""):
            self.operador1 = eval(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "resta"
        else:
            self.operador2 = eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador1-self.operador2))

    def multiplicar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == ""):
            self.operador1 = eval(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "producto"
        else:
            self.operador2 = eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador1*self.operador2))   

    def dividir(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == ""):
            self.operador1 = eval(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "division"
        else:
            self.operador2 = eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador1*self.operador2))

    def potencias(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        if(self.operador1 == ""):
            self.operador1 = eval(self.Calculo.text())
            self.Calculo.setText("")
            self.operacion = "potencia"
        else:
            self.operador2 = eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador1**self.operador2))                  

    def raiz2(self):
        if(self.operador1 == ""):
            self.operacion = "raiz"
        else:
            self.operador2=eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador2 ** 0.5)) 
     

    def resultado(self):
        #Se procede a la operación dependiendo del tipo y siempre y cuando este determinado el primer operador.
        self.ban=1
        if(self.operacion == "suma"):
            self.operador2 = eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador1+self.operador2))
            self.operador1=''
            self.operador2=''
            self.operacion=''
        if(self.operacion == "resta"):
            self.operador2 = eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador1-self.operador2))
            self.operador1=''
            self.operador2=''
            self.operacion=''   
        if(self.operacion == "producto"):
            self.operador2 = eval(self.Calculo.text())
            self.Calculo.setText(str(self.operador1*self.operador2))
            self.operador1=''
            self.operador2=''
            self.operacion=''
        if(self.operacion == "division"):
            self.operador2 = eval(self.Calculo.text())
            if(self.operador2 == 0):
               self.Calculo.setText("No se puede dividir entre cero") 
            else:   
               self.Calculo.setText(str(self.operador1/self.operador2))
            self.operador1=''
            self.operador2=''
            self.operacion=''    
        if(self.operacion == "potencia"):
            self.operador2 = self.Calculo.text()
            if(self.operador2 == ''):
                self.Calculo.setText("No ingreso exponente") 
            else: 
                self.operador2 = eval (self.Calculo.text())
                self.Calculo.setText(str(self.operador1**self.operador2))
            self.operador1=''
            self.operador2=''
            self.operacion=''
        if(self.operacion == "raiz"):
            self.operador2 = eval (self.Calculo.text())
            self.Calculo.setText(str(self.operador2 ** 0.5 ))
            self.operador1=''
            self.operador2=''
            self.operacion=''

    def eliminarTodo(self):
        self.Calculo.clear()

    def borrardigito(self):
        valor=self.Calculo.text()
        self.Calculo.setText(valor[:len(valor)-1])
           
       


    #Eventos de asignación de valores al label
    def click_1(self):
        if(self.ban==1):
           self.Calculo.setText("")
           self.Calculo.setText(self.Calculo.text() + "1")
           self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "1")   

    def click_2(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "2")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "2")  
    
    def click_3(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "3")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "3")
    def click_4(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "4")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "4")
    
    def click_5(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "5")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "5")
    
    def click_6(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "6")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "6")
    
    def click_7(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "7")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "7")
    
    def click_8(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "8")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "8")
    
    def click_9(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "9")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "9")
    
    def click_0(self): 
        if(self.ban==1):
            self.Calculo.setText("")
            self.Calculo.setText(self.Calculo.text() + "0")
            self.ban=0
        else:
           self.Calculo.setText(self.Calculo.text() + "0")

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()