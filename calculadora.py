from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from math import *

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calculadora.ui", self)
        #Seteamos los operadores
        self.operador = ""
        #self.operador2 = ""
        self.ban = "0"
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
        self.boton_coma.clicked.connect(self.click_coma)
        #Listeners de Eventos de los botones de las operaciones
        self.suma.clicked.connect(self.sumar)
        self.resta.clicked.connect(self.restar)
        self.producto.clicked.connect(self.multiplicar)
        self.division.clicked.connect(self.dividir)
        self.potencia.clicked.connect(self.potencias)
        self.raiz.clicked.connect(self.raiz2)
        self.igual.clicked.connect(self.resultado)
        self.borrartodo.clicked.connect(self.eliminarTodo) 
        self.borrar.clicked.connect(self.borrarOperador) 
        self.borrardigito.clicked.connect(self.borrarDigitos) 

    def sumar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        self.operacion = "suma"
        if (self.ban=='0'):
            operador=self.Calculo.text()  
            operador+= "+"   
            self.Calculo.setText(operador)
        else:
            self.Calculo.clear()
            self.Calculo.setText(self.operador)
            self.operador+= "+"   
            self.Calculo.setText(self.operador)

    def restar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        self.operacion = "resta"
        if (self.ban=='0'):
            operador=self.Calculo.text()  
            operador+= "-"   
            self.Calculo.setText(operador)
        else:
            self.Calculo.clear()
            self.Calculo.setText(self.operador)
            self.operador+= "-"   
            self.Calculo.setText(self.operador)

    def multiplicar(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        self.operacion = "producto"
        if (self.ban=='0'):
            operador=self.Calculo.text()  
            operador+= "*"   
            self.Calculo.setText(operador)
        else:
            self.Calculo.clear()
            self.Calculo.setText(self.operador)
            self.operador+= "*"   
            self.Calculo.setText(self.operador) 

    def dividir(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        self.operacion = "division"
        if (self.ban=='0'):
            operador=self.Calculo.text()  
            operador+= "/"   
            self.Calculo.setText(operador)
        else:
            self.Calculo.clear()
            self.Calculo.setText(self.operador)
            self.operador+= "/"   
            self.Calculo.setText(self.operador)

    def potencias(self):
        #Si ya tiene asignado un operador, agregamos el otro con el mismo botón
        self.operacion = "potencia"
        if (self.ban=='0'):
            operador=self.Calculo.text()  
            operador+= "**"   
            self.Calculo.setText(operador)
        else:
            self.Calculo.clear()
            self.Calculo.setText(self.operador)
            self.operador+= "**"   
            self.Calculo.setText(self.operador)              

    def raiz2(self):
        self.operacion = "raiz"
        if (self.ban=='0'):
            operador=self.Calculo.text()
            if (operador==''):
                operador+= "sqrt ("   
                self.Calculo.setText(operador)
            else:
                operador= "sqrt ("
                operador+=self.Calculo.text()
                self.Calculo.setText(operador)    
        else:
            self.Calculo.clear()
            self.Calculo.setText(self.operador)
            self.operador+= "sqrt ("    
            self.Calculo.setText(self.operador)
     

    def resultado(self):
        #Se procede a la operación dependiendo del tipo y siempre y cuando este determinado el primer operador.
        self.ban=1
        if(self.operacion == "suma"):
            operador = eval(self.Calculo.text())
            res=str(operador)
            operador = self.Calculo.text()
            operador+= "=" 
            operador+=res 
            self.Calculo.setText(operador)
            self.operador=res
            self.operacion=''        

        if(self.operacion == "resta"):
            operador = eval(self.Calculo.text())
            res=str(operador)
            operador = self.Calculo.text()
            operador+= "=" 
            operador+=res 
            self.Calculo.setText(operador)
            self.operador=res
            self.operacion=''   


        if(self.operacion == "producto"):
            operador = eval(self.Calculo.text())
            res=str(operador)
            operador = self.Calculo.text()
            operador+= "=" 
            operador+=res 
            self.Calculo.setText(operador)
            self.operador=res
            self.operacion='' 

        if(self.operacion == "division"):
            operador =self.Calculo.text()
            try:
                    res= str(eval(operador))
                    operador = self.Calculo.text()
                    operador+= "=" 
                    operador+=res 
                    self.Calculo.setText(operador)
                    self.operador=res
                    self.operacion=''
            except :
                
                    self.Calculo.setText("No se puede dividir entre cero ") 
  
                
        if(self.operacion == "potencia"):
            operador =self.Calculo.text()
            #operador+= ")"
            #self.Calculo.setText(operador)
            try:
                    res= str(eval(operador))
                    operador = self.Calculo.text()
                    operador+= "=" 
                    operador+=res 
                    self.Calculo.setText(operador)
                    self.operador=res
                    self.operacion=''
            except :
                    self.Calculo.setText("Error -") 


        if(self.operacion == "raiz"):
            operador =self.Calculo.text()
            operador+= ")"
            self.Calculo.setText(operador)
            try:
                    res= str(eval(operador))
                    operador = self.Calculo.text()
                    operador+= "=" 
                    operador+=res 
                    self.Calculo.setText(operador)
                    self.operador=res
                    self.operacion=''
            except :
                
                    self.Calculo.setText("Error -") 

    def eliminarTodo(self):
        self.Calculo.clear()
        self.operador=''
        self.operacion=''
        self.ban="0"

    def borrarDigitos(self):
        valor=self.Calculo.text()
        self.Calculo.setText(valor[:len(valor)-1])

    def borrarOperador(self):
        if(self.operacion == ""):
            self.Calculo.clear()
            self.operador1=''
        else:
            self.Calculo.clear()
            self.operador2=''      
           
       


    #Eventos de asignación de valores al label
    def click_1(self):
        if(self.ban==1):
           #self.Calculo.setText("")
           operador=self.Calculo.text()  
           operador+= "1"   
           self.Calculo.setText(operador)
           self.ban=0
        else:
           operador=self.Calculo.text()  
           operador+= "1"   
           self.Calculo.setText(operador)

    def click_2(self): 
        if(self.ban==1):
           # self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "2"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "2"   
            self.Calculo.setText(operador) 
    
    def click_3(self): 
        if(self.ban==1):
           #  self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "3"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "3"   
            self.Calculo.setText(operador)

    def click_4(self): 
        if(self.ban==1):
           # self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "4"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "4"   
            self.Calculo.setText(operador)
    
    def click_5(self): 
        if(self.ban==1):
            #self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "5"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "5"   
            self.Calculo.setText(operador)
    
    def click_6(self): 
        if(self.ban==1):
           # self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "6"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "6"   
            self.Calculo.setText(operador)
    
    def click_7(self): 
        if(self.ban==1):
          #  self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "7"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "7"   
            self.Calculo.setText(operador)
    
    def click_8(self): 
        if(self.ban==1):
           # self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "8"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "8"   
            self.Calculo.setText(operador)
    
    def click_9(self): 
        if(self.ban==1):
          #  self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "9"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "9"   
            self.Calculo.setText(operador)
    
    def click_0(self): 
        if(self.ban==1):
          #  self.Calculo.setText("")
            operador=self.Calculo.text()  
            operador+= "0"   
            self.Calculo.setText(operador)
            self.ban=0
        else:
            operador=self.Calculo.text()  
            operador+= "0"   
            self.Calculo.setText(operador)

    def click_coma(self): 
        operador=self.Calculo.text()  
        if(operador==''):
            operador+= "0."   
            self.Calculo.setText(operador)   
        else:
            operador+= "."   
            self.Calculo.setText(operador)         

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()