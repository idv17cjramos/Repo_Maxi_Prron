
#Bienvenido Saint Yeipi
 
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
operacion=str.lower(operacion)


 
def suma():
    sumita = input("Introduce numeros: ")
    sumita = [int(x) for x in sumita.split (" ") ]
    total = 0
    for numero in sumita:
        total += numero
    print ("La suma es:", total)
 
def resta():
    restita = input("Introduce numeros: ")
    restita = [int(x) for x in restita.split (" ") ]
    total = 0
    for numero in restita:
        total = numero
    print ("La resta es:", total)
 
def multiplicacion():
    x  =  int(input("Escribe el primer número que quieres multiplicar: "))
    y  =  int(input("Escribe el segundo número que quieres multiplicar: "))
    print (x*y)
  
def division():
    x  =  int(input("Escribe el dividendo: "))
    y  =  int(input("Escribe el divisor: "))
    print (x/y)
 


if (operacion== "suma"):
    suma()
elif(operacion=="multiplicacion"):
    multiplicacion()
elif (operacion == "division" ):
    division()
elif (operacion == "guebito con cacsun" ):
    print("Estas reprobado para toda la vida :)")