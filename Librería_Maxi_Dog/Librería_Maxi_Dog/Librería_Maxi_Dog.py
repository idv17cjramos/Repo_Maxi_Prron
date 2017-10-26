#Bienvenido Saint Yeipi
#Importamos el tiempo...
import time
import sys
import random

def presentacion(): 
    print ("Bienvenido a la librería Maxi Dog")
    print ("-"*80+  "\n")
    print ("¿Qué es lo que deseas hacer el día de hoy? \n\nIntroduce el numero de la función y después aprieta enter\n")
     
    print(" 1.-Suma")
    print(" 2.-Resta")
    print(" 3.-Multiplicación")
    print(" 4.-División")
    print(" 5.-Modulo")
    print(" 6.-Metros a pulgadas")
    print(" 7.-Pulgadas a metros")
    print(" 8.-Raiz")
    print(" 9.-Potencia")
    print("10.-Decimal a hexadecimal")
    print("11.-Hexadecimal a decimal")
    print("12.-Binario a decimal")
    print("13.-Decimal a binario")
    print("14.-Metros a yardas")
    print("15.-Yardas a metros")
    print("16.-Metros a pulgadas")
    print("17.-Pulgadas a metros")
    print("18.-Calcular Indice de Masa Corporal")
    print("19.-Calcular si es numero primo")
    print("20.-Extras")
    print ("-"*80+  "\n")

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
    print ("El resultado es: \n", total) #Que pendejos multiplicaron por 0, apendejamiento momentaneo :C
 
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
    numeroBase = input("Escriba el número que quiera elevar: ")
    exponente = input("Escriba el exponente al que lo quiera elevar: ")
    if (exponente == 0):
        print ("Elevaste a cero, tu resultado es 1")
    alCuadrado = 2
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
 
def numeroprimo():
    x= int(input("Introduzca un numero entero:"))
    contador=2
    esPrimo = True
    while(contador < x ):
      if(x % contador == 0):
        esPrimo = False
      contador = contador + 1
    if(esPrimo):
        print ("Su numero es primo")
    else:
        print ("Su numero no es primo, es tio")

def HexadecimalaDecimal():
   NumoerAconvertir = input ("introduce el número en Hexadecimal que quieras convertir a decimal: ")
   Numeroconvertido = int(NumoerAconvertir,16)
   
   print ("El número convertido a decimal es: " + str(Numeroconvertido))

def ahorcado():
    frases = {"InFamous":["no pidas una vida mas facil pide ser mas fuerte","todo hombre es responsable del bien que no ha hecho","no pienso hacer esto cada vez para que tu mojes"],
              "Terminator":["i will be back","hasta la vista baby","estoy viejo no obsoleto"],
              "Star Wars":["luke soy tu padre","siempre en movimiento esta el futuro","no lo intentes hazlo"],          
              "Harry Potter":["para una mente bien preparada la muerte es solo la siguiente gran aventura","es hora de elegir entre lo que es facil y lo que es correcto","la gente encuentra mas facil perdonar a los demas por equivocarse que por acertar"],
              "God Of War":["la medida de un hombre es lo que hace con el poder","la esperanza es para los debiles pandora","en la oscuridad el fuego de la esperanza nos liberara"]}
    
    categoria = random.choice(list(frases.keys()))
    frase = random.choice(frases[categoria])
    
    dibujo = ['''
    
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
    
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    palabra = list(frase)
    vacio = "_"*len(frase)
    correctas = list(vacio)
    errores = 0
    turnos = 0
    flag = True
    perder = False
    ganar = False
    print("vamos a jugar con frases de " + str(categoria))

    while(ganar == False and perder == False):
        print(dibujo[errores])
        print(*correctas)
        intento = input("Ingresa una letra y averigua si esta dentro de la palabra secreta: ")
        if (intento in correctas):
            print("Ya usaste esa letra!")
            flag = True
        contador = 0
        while (contador < len(palabra)):
            espacios = " "
            if (espacios in palabra[contador]):
               correctas[contador] = espacios
            if (intento in palabra[contador]):
                correctas[contador] = intento
            contador = contador + 1
            if (contador == len(palabra) and flag == False):
                print("correcto!")
        if(intento not in palabra):
            print("No esta!")
            errores = errores + 1
        if (errores == 7):
            print ("Perdiste, moriras agonizantemente")
            print("PD: La palabra era " + str(frase))
            perder = True
        if (correctas == palabra):
            print(*correctas)
            print("Eres una chingoneria, le atinaste!")
            print("PD: Y solo te tomo " +str(turnos) + " intentos!")
            ganar = True
        turnos += 1

def serpientesyescaleras():
    tiros = 0
    pasos = 0
    indice = 0
    turno = 0
    logro1 = False
    logro2 = True
    ganar = False
    
    portales =             (1,38,
                            4,14,
                            9,31,
                            17,7,
                            21,42,
                            28,84,
                            51,67,
                            54,34,
                            62,19,
                            64,60,
                            72,91,
                            80,99,
                            93,73,
                            95,75,
                            98,79)
    posiciones = []
    nombres = []
    
    n = int(input("Cuantos jugadores habra? "))
    
    while (indice < n):
        print("Cual es el nombre del jugador " + str(indice + 1) + "? ")
        nu = input()
        posiciones.append(0)
        nombres.append(str(nu))
        indice = indice + 1
    
    while (ganar == False):
        print("Es turno de " + nombres[turno])
        input ("Presiona una tecla para lanzar los dados: ")
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        tiros+=1
        print ("Dado 1: " +str( dado1) + "    Dado 2: "+str(dado2)+"    Suma: "+ str(dado1+dado2))
        print ("Avanzas de la posicion " +str(posiciones[turno])) 
        posiciones[turno] = posiciones[turno]+dado1+dado2
        pasos = pasos+dado1+dado2
        if(posiciones[turno]>100):
            deMas=posiciones[turno] -100
            posiciones[turno] = 100 - deMas 
        SyEi= 0
        while(SyEi < len(portales)):
            if(portales[SyEi] == posiciones[turno]):
                if(portales[SyEi] < portales[SyEi+1]):
                    print("Subes por una escalera de la posicion " + str (posiciones[turno]) +" a la posicion"+ 
                    str (portales[SyEi]))
                else:
                    print("Caes por una serpiente de la posicion " + str(portales[SyEi]) + " a la posicion" + 
                    str(portales[SyEi + 1]))
                    logro2 = False
                posiciones[turno] = portales[SyEi + 1]
            SyEi = SyEi + 2
    
    
        print ("A la posicion "+str(posiciones[turno]))
        if (dado1 == 1 and dado2 == 1 and logro1 == False):
            print ("Logro desbloqueado: PAR DE ASES!")
            logro1 = True
        if(posiciones[turno] == 100):
            ganar = True
            if (logro2 == True):
                print ("Domador de serpientes!")
            print (nombres[turno] + "\nTiraste " + str(tiros) + " veces"  )
            print ("Avanzaste " + str(pasos) + " pasos")
        turno = turno + 1
        if (turno >= n):
            turno = 0

def guebitohKonCacsum():
    print("Guebitoh Kon Cacsum...")
    time.sleep(2)
    print("mmmmm uma delisia :v")
    time.sleep(2)
    print("e.e")
    time.sleep(2)
    print("Es neta, vato? >:V")
    time.sleep(3)
    print("no, ya enserio, estas reprobado para toda la vida :)")

continuar = True
presentacion()

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
    elif(operacion == "10"):
        print("esta operacion aun no esta disponible")
    elif (operacion=="11"):
        HexadecimalaDecimal()
    elif (operacion == "12"):
        binarioaDecimal()
    elif (operacion == "13"):
        decimalaBinario()
    elif (operacion == "14"):
        metrosaYardas()
    elif (operacion == "15"):
        yardasaMetros()
    elif (operacion == "16"):
        metrosaPulgadas()
    elif (operacion == "17"):
        pulgadasaMetros()
    elif (operacion == "18"):
        IMC()
    elif(operacion =="19"):
        numeroprimo()
    elif(operacion =="20"):
        print("1.-Ahorcado")
        print("2.-Serpientes y Escaleras")
        print("?.-Secreto")

        easter = input("Que quieres jugar?\n")
        easter = str.lower(easter)
        if(easter == "1"):
            ahorcado()
        elif(easter == "2"):
            serpientesyescaleras()
        else:
            guebitohKonCacsum()

    pregunta = input('Quieres hacer otra operacion?(escribe "si" o "no")\n')
    presentacion()
    if(pregunta =="no"):
        continuar=False