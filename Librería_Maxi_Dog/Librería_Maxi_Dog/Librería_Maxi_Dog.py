#Bienvenido Saint Yeipi
#Importamos el tiempo...
import time


 

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
print("Metros a pulgadas")
print ("-"*80+  "\n")

operacion=input("Que operacion quieres realizar? ")
#Conversor a minusculas
operacion=str.lower(operacion)
#Operaciones
def suma():
    sumita = input("Introduce numeros: ")
    sumita = [int(x) for x in sumita.split (" ") ]
    total = 0
    for numero in sumita:
        total += numero
    print ("La suma es:", total)
 
def resta():
    x  =  int(input("Escribe el primer numero: "))
    y  =  int(input("Escribe el segundo número: "))
    print (x-y)

def multiplicacion():
    x  =  int(input("Escribe el primer número que quieres multiplicar: "))
    y  =  int(input("Escribe el segundo número que quieres multiplicar: "))
    print (x*y)
  
def division():
    x  =  int(input("Escribe el dividendo: "))
    y  =  int(input("Escribe el divisor: "))
    print (x/y)


def potencia():
    numeroBase = int(input("Escriba el número que quiera elevar: "))
    exponente = int(input("Escriba el exponente al que lo quiera elevar: ")) 
    if (exponente == 0):
        print ("Elevaste a cero, tu resultado es 1")
    elif(exponente == nul):
        print(numeroBase*numeroBase)

#Menu

if (operacion== "suma"):
    suma()
elif(operacion=="multiplicacion"):
    multiplicacion()
elif (operacion == "division" ):
    division()
elif (operacion == "resta" ):
    resta()
elif (operacion == "potencia" ):
    potencia()
#Easter egg
elif (operacion == "guebito con cacsun" ):
    print("mmmmm uma delisia :v")
    time.sleep(3)
    print("e.e")
    time.sleep(2)
    print("Es neta, vato? >:V")
    time.sleep(3)
    print("no, ya enserio, estas reprobado para toda la vida :)")
