#Bienvenido Saint Yeipi
#Importamos el tiempo...
import time
import sys
#Presentacion
 
print ("Bienvenido a la librería Maxi Dog")
print ("-"*80+  "\n")
print ("¿Qué es lo que deseas hacer el día de hoy? \n\nIntroduce el numero de la función y después aprieta enter\n")
 
print("1.-Suma")#
print("2.-Resta")#
print("3.-Multiplicación")#
print("4.-División")#
print("5.-Potencia")#
print("6.-Raíz")#
print("7.-Módulo")#
print("8.-Binario a hexadecimal")
print("9.-Hexadecimal a binario")
print("10.-Decimal a hexadecimal")
print("11.-Hexadecimal a decimal")
print("12.-Binario a decimal")
print("13.-Decimal a binario")
print("14.-Metros a yardas")#
print("15.-Yardas a metros")#
print("16.-Metros a pulgadas")#
print("17.-Pulgadas a metros")#
print("18.-Calcular Indice de Masa Corporal")#
print ("-"*80+  "\n")

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
    numeroBase = float(input("Escriba el número que quiera radicar: "))
    exponente = float(input("Escriba la radical a la que lo quiera radicalizar: "))
    if (exponente == "0"):
        print ("Radicaste a cero, tu resultado es un error")
        sys.exit()
    resultado = abs(numeroBase) ** (1/exponente)
    if(numeroBase<0):
        print (str(resultado) + "i" +"\nTu numero es imaginario")
        return
    try:
        print (str(numeroBase ** (1/exponente)))
    except (ValueError):
        print("No introdujiste radical, se sacara raiz cuadrada.")
        print("El resultado es: ")
        print(str(numeroBase ** (1/cuadrada)))
 
def potencia():
    numeroBase = int(input("Escriba el número que quiera elevar: "))
    exponente = int(input("Escriba el exponente al que lo quiera elevar: "))
    if (exponente == 0):
        print ("Elevaste a cero, tu resultado es 1")
    elif(exponente == nul):
        print(numeroBase*numeroBase)
 
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
 
def IMC():
    sexo=input("Eres mujer u hombre? ")
    peso=float(input("Introduce tu peso en kilos: "))
    estatura=float(input("Introduce tu estatura en metros: "))
    sexo.lower()
    imc=(peso/(estatura)**2)
    print (str(imc))
    if (imc<18.5):
        print ("Tienes peso abjo")
    elif (imc>=18.5 and imc<25):
        print ("Tienes peso ideal")
    elif (imc>=25.0 and imc<30):
        print ("Tienes Sobrepeso")
    elif (imc>=30 and imc<35):
        print ("Tienes obesidad")
    elif (imc>=35 and imc<40):
        print ("Tienes Obesidad 2")
    elif (imc<=40):
        print ("Tienes obesidad mórbida")
    if(sexo=="hombre"):
        estatura=estatura*100
        ideal=(estatura-100)*0.90
        print ("Tu peso ideal es " + str(ideal))
    elif(sexo=="mujer"):
        estatura=estatura*100
        ideal=(estatura-100)*0.85
        print ("Tu peso ideal es " + str(ideal))
 
def decimalaBinario():
    numero = int(input("Ingresa el número que quieres convertir a binario: "))
    listaBinarial = []
    while(numero>0):
        residuo=numero%2
        listaBinarial.append(residuo)
        numero = numero//2
    listaReversa = reversed(listaBinarial)
    print("Tu número binario es: ")
    print(*listaReversa)
 
def binarioaDecimal():
    binario = input("Ingresa el número binario a convertir a decimal: ")
    decimal = 0
    for x in binario:
        decimal = decimal*2 + int(x)
    print ("Tu número en decimal es: \n" + str(decimal))
 
 
 
 
#Menu
continuar = True
while(continuar==True):
    #Selector de operacion
    operacion=input("Que operacion quieres realizar? ")
    #Conversor a minusculas
    operacion=str.lower(operacion)
    if (operacion== "1"):
        suma()
    elif(operacion=="2"):
        resta()
    elif (operacion == "3" ):
        multiplicacion()
    elif (operacion == "4" ):
        division()
    elif (operacion == "5" ):
        modulo()
    elif(operacion=="6"):
        metrosaPulgadas()
    elif(operacion=="7"):
        pulgadasaMetros()
    elif (operacion == "8" ):
        raiz()
    elif (operacion == "9" ):
        potencia()
    elif (operacion == "14"):
        metrosaYardas()
    elif (operacion=="11"):
        yardasaMetros()
    elif (operacion== "18"):
        IMC()
    elif (operacion == "13"):
        decimalaBinario()
    elif (operacion == "12"):
        binarioaDecimal()
    elif(operacion == "10"):
        decimalaHexadecimal()

    #Easter egg
    elif (operacion == "guebito con cacsun" ):
        print("mmmmm uma delisia :v")
        time.sleep(3)
        print("e.e")
        time.sleep(2)
        print("Es neta, vato? >:V")
        time.sleep(3)
        print("no, ya enserio, estas reprobado para toda la vida :)")
    pregunta = input('Quieres hacer otra operacion?(escribe "si" o "no")\n')
    if(pregunta =="no"):
        continuar=False