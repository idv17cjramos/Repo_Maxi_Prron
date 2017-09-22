#Bienvenido Saint Yeipi
#Importamos el tiempo...
import time
import sys

#Presentacion

print ("Bienvenido a la librería Maxi Dog")
print ("-"*80+  "\n")
print ("¿Qué es lo que deseas hacer el día de hoy? \n\nIntroduce el nombre de la función y después aprieta enter\n")
 
print("Suma")
print("Resta")
print("Multiplicación")
print("División")
print("Potencia")
print("Raíz")
print("Módulo")
print("Binario a hexadecimal")
print("Hexadecimal a binario")
print("Decimal a hexadecimal")
print("Hexadecimal a decimal")
print("Binario a decimal")
print("Decimal a binario")
print("Metros a yardas")
print("Yardas a metros")
print("Metros a pulgadas")
print("Pulgadas a metros")
print ("-"*80+  "\n")

operacion=input("Que operacion quieres realizar? ")

#Conversor a minusculas
operacion=str.lower(operacion)

#Operaciones
def suma():
    sumita = input("Introduce numeros a sumar (Separados por un espacio): ")
    sumita = [int(x) for x in sumita.split (" ") ]
    total = 0
    for numero in sumita:
        total += numero
    print ("El resultado es: \n",total)
 
def resta():
    restita1 = input("Introduce minuendos (Separados por un espacio): ")
    restita1 = [int(x) for x in restita1.split (" ") ]
    total1 = 0
    for numero1 in restita1:
        total1 += numero1
    restita2 = input("Introduce sustraendos(Separados por un espacio): ")
    restita2 = [int(x) for x in restita2.split (" ") ]
    total2 = 0
    for numero2 in restita2:
        total2 -= numero2
    print ("El resultado es: ")
    print (int(total1) + int(total2))

def multiplicacion():
    multi = input("Introduce numeros que quieras multiplicar (Separados por un espacio): ")
    multi = [int(x) for x in multi.split (" ") ]
    total = 1
    for numero in multi:
        total *= numero
    print ("El resultado es: \n", total) #Que pendejos multiplicaron por 0
  
def division():
    x  =  int(input("Escribe el dividendo: "))
    y  =  int(input("Escribe el divisor: "))
    print ("El resultado es: ")
    print (x/y)

def modulo():
    x  =  int(input("Escribe el dividendo: "))
    y  =  int(input("Escribe el divisor: "))
    print ("El resultado es: ")
    print (x%y)
    
def metrosaPulgadas():
    metros = float(input("Escribe la cantidad de metros a convertir: "))
    pulgadas = 39.3701
    print ("El resultado es: ")
    print (metros*pulgadas)

def pulgadasaMetros():
    pulgadas = float(input("Escribe la cantidad de pulgadas a convertir: "))
    metros = 0.0254
    print ("El resultado es: ")
    print (pulgadas*metros)

def raiz():
    cuadrada = 2
    numeroBase = int(input("Escriba el número que quiera radicar: "))
    exponente = int(input("Escriba la radical a la que lo quiera radicalizar: "))
    if (exponente == "0"):
        print ("Radicaste a cero, tu resultado es un error")
        sys.exit()
    if(exponente<0):
        print (int(numeroBase) ** abs(1/exponente) + "j" +"\n Tu numero es imaginario")
    try:
        print (float(numeroBase) ** float(1/exponente))
    except (ValueError):
        print("No introdujiste radical, se sacara raiz cuadrada.")
        print("El resultado es: ")
        print(float(numeroBase) ** float(1/cuadrada))

def potencia():
    alCuadrado = 2
    numeroBase = int(input("Escriba el número que quiera elevar: "))
    exponente = input("Escriba el exponente al que lo quiera elevar: ") 
    if (exponente == 0):
        print ("Elevaste a cero, tu resultado es 1")
    try:
        print (int(numeroBase) ** int(exponente))
    except (ValueError):
        print("No introdujiste exponente, se elevará al cuadrado.")
        print("El resultado es: ")
        print(int(numeroBase) ** int(alCuadrado))

def metrosaYardas():
    metros=float(input("Escribe la cantidad de metros a convertir: "))
    yardas = 1.09361
    print ("El resultado es: ")
    print (metros*yardas)

def yardasaMetros():
    yardas=float(input("Escribe la cantidad de yardas a convertir: "))
    metros = 0.9144
    print ("El resultado es: ")
    print (yardas*metros)

#Menu
if (operacion== "suma"):
    suma()
elif(operacion=="multiplicacion"):
    multiplicacion()
elif (operacion == "division" ):
    division()
elif (operacion == "resta" ):
    resta()
elif(operacion=="potencia"):
    potencia()
elif(operacion=="raiz"):
    raiz()
elif (operacion == "metros a pulgadas" ):
    metrosaPulgadas()
elif (operacion == "pulgadas a metros" ):
    pulgadasaMetros()
elif (operacion == "metros a yardas"):
    metrosaYardas()
elif (operacion=="yardas a metros"):
    yardasaMetros()
elif (operacion == "modulo"):
    modulo()

#Easter egg
elif (operacion == "guebito con cacsun" ):
    print("mmmmm uma delisia :v")
    time.sleep(3)
    print("e.e")
    time.sleep(2)
    print("Es neta, vato? >:V")
    time.sleep(3)
    print("no, ya enserio, estas reprobado para toda la vida :)")
