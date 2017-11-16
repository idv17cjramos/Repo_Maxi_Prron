#Bienvenido Saint Yeipi
#Importamos el tiempo...
import time
import sys
import random

def presentacion(): 
    #Texto de bienvenida para el usuario, contiene todas las operaciones de la calculadora numeradas
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
    #Solicita un input del usuario
    sumita = input("Introduce numeros a sumar (Separados por un espacio): ")
    #Crea una lista en base a los numeros introducidos por el usuario, separandolos por un espacio
    sumita = [int(x) for x in sumita.split (" ") ]
    #Suma todos los elementos de la lista "sumita"
    total = 0
    for numero in sumita:
        total += numero
    #Imprime el resultado de la suma
    print ("El resultado es:\n",total)
 
def resta():
    #Solicita un los minuendos, los convierte en una lista separando por un espacio y suma todos los elementos de la lista
    restita1 = input("Introduce minuendos (Separados por un espacio): ")
    restita1 = [int(x) for x in restita1.split (" ") ]
    total1 = 0
    for numero1 in restita1:
        total1 += numero1
    #Solicita los sustraendos, los convierte en una lista separando por un espacio y resta todos los elementos de la lista
    restita2 = input("Introduce sustraendos(Separados por un espacio): ")
    restita2 = [int(x) for x in restita2.split (" ") ]
    total2 = 0
    for numero2 in restita2:
        total2 -= numero2
    #Suma los minuendos y los sustraendos e imprime el resultado
    print ("El resultado es: ")
    print (int(total1) + int(total2))
 
def multiplicacion():
    #Solicita los numeros a multiplicar
    multi = input("Introduce numeros que quieras multiplicar (Separados por un espacio): ")
    #Crea una lista de los numeros introducidos, separandolos por espacios
    multi = [int(x) for x in multi.split (" ") ]
    #Multiplica en orden los elementos de la lista en forma de producto acumulado e imprime el resultado
    total = 1
    for numero in multi:
        total *= numero
    print ("El resultado es: \n", total) 

def division():
    #Solicita el dividendo
    x  =  int(input("Escribe el dividendo: "))
    #Solicita el divisor
    y  =  int(input("Escribe el divisor: "))
    #divide el dividendo entre el dividor e imprime el resultado
    print ("El resultado es: ")
    print (x/y)
 
def modulo():
    #Solicita el dividendo
    x  =  int(input("Escribe el dividendo: "))
    #Solicita el divisor
    y  =  int(input("Escribe el divisor: "))
    #divide el dividendo entre el divisor e imprime el residuo
    print ("El resultado es: ")
    print (x%y)
 
def raiz():
    cuadrada = 2
    #Solicita el numero base y el exponente
    numeroBase = float(input("Escriba el número que quiera radicar: "))
    exponente = float(input("Escriba la radical a la que lo quiera radicalizar: "))
    #Si el exponente es igual a 0 lanza un mensaje de error y sales de la operacion
    if (exponente == "0"):
        print ("Radicaste a cero, tu resultado es un error")
        sys.exit()
    #Eleva el valor absoluto del numero base a la potencia de la fracción 1/exponente
    resultado = abs(numeroBase) ** (1/exponente)
    #Si el numero base es negativo imprime el resultado y notifica que el resultado es un numero imaginario
    if(numeroBase<0):
        print (str(resultado) + "i" +"\nTu numero es imaginario")
        return
    #Imprime el resultado
    try:
        print (str(numeroBase ** (1/exponente)))
    #Si no se introdujo ningún exponente, se toma el 2 como valor por defecto, se notifica al usuario y se imprime el resultado
    except (ValueError):
        print("No introdujiste radical, se sacara raiz cuadrada.")
        print("El resultado es: ")
        print(str(numeroBase ** (1/cuadrada)))
 
def potencia():
    #Solicita el numero base y el exponente
    numeroBase = input("Escriba el número que quiera elevar: ")
    exponente = input("Escriba el exponente al que lo quiera elevar: ")
    #Al elevar a la 0 el resultado será 1
    if (exponente == 0):
        print ("Elevaste a cero, tu resultado es 1")
    alCuadrado = 2
    #Imprime el resultado
    try:
        print (int(numeroBase) ** int(exponente))
    #Si no se introdujo un exponente se toma el 2 como valor por defecto, se notifica al usuario y se imprime el resultado
    except (ValueError):
        print("No introdujiste exponente, se elevará al cuadrado.")
        print("El resultado es: ")
        print(int(numeroBase) ** int(alCuadrado))
 
def metrosaYardas():
    #Se solicitan al usuario los metros a convertir
    metros=float(input("Escribe la cantidad de metros a convertir: "))
    #Esta es la equivalencia de yardas por metro
    yardas = 1.09361
    #Se multiplican los metros por su equivalencia en yardas y se imprime el resultado
    print ("El resultado es: ")
    print (metros*yardas)
 
def yardasaMetros():
    #Se solicitan al usuario los yardas a convertir
    yardas=float(input("Escribe la cantidad de yardas a convertir: "))
    #Esta es la equivalencia en metros por yarda
    metros = 0.9144
    #Se multiplican las yardas por su equivalencia en metros y se imprime el resultado
    print ("El resultado es: ")
    print (yardas*metros)

def metrosaPulgadas():
    #Se solicita al usuario la cantidad de metros
    metros = float(input("Escribe la cantidad de metros a convertir: "))
    #Equivalencia de pulgadas en un metro
    pulgadas = 39.3701
    #Se imprime el resultado y se multiplica pulgadas(que es valor continuo) por metros(que es la cantidad que se le pide al usuario)
    print ("El resultado es: ")
    print (metros*pulgadas)
 
def pulgadasaMetros():
    #Se solicita al usuario la cantidad de pulgadas
    pulgadas = float(input("Escribe la cantidad de pulgadas a convertir: "))
    #Equivalencia de metrso en una pulgada
    metros = 0.0254
    #Se imprime el resultado y se multiplica metros(que es valor continuo) por pulgadas(que es la cantidad que se le pide al usuario)
    print ("El resultado es: ")
    print (pulgadas*metros)
 
def IMC():
    #Se le pide al usuario que meta su sexo, peso y estatura.
    sexo=input("Eres mujer u hombre? ")
    peso=float(input("Introduce tu peso en kilos: "))
    estatura=float(input("Introduce tu estatura en metros: "))
    # Sexo se pasa a minúsculas
    sexo.lower()
    #Se calcula el IMC con la fórumla y se imprime la cantidad del índice de masas corporal.
    imc=(peso/(estatura)**2)
    print ("Tu indice de masa cormporal es: " + str(imc))
    #Se empiezan a hacer comparaciones del IMC obtenido con los valores "sanos" del IMC. Se imprime alguno de los casos
    if (imc<18.5):
        print ("Tienes peso bajo")
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
    #Se compara el input del usuario para saber si es hombre o mujer, con eso se elige una operación, se calcula el peso ideal del usuario
    # Y se imprime el resultado.
    if(sexo=="hombre"):
        estatura=estatura*100
        ideal=(estatura-100)*0.90
        print ("Tu peso ideal es " + str(ideal))
    elif(sexo=="mujer"):
        estatura=estatura*100
        ideal=(estatura-100)*0.85
        print ("Tu peso ideal es " + str(ideal))
 
def decimalaBinario():
    #Se le pide al usuario que ingrese el número que quiere convertir a binario.
    numero = int(input("Ingresa el número que quieres convertir a binario: "))
    listaBinarial = []
    #Mientras el input sea mayor a cero, se hace el siguiente bucle
    while(numero>0):
        #Calcula el módulo del input
        residuo=numero%2
        #Mete el input en una lista
        listaBinarial.append(residuo)
        #Divide input entre 2
        numero = numero//2
    #Reacomoda la lista de atrás hacia adelante
    listaReversa = reversed(listaBinarial)
    #Imprime lista al revés como el número binario.
    print("Tu número binario es: ")
    print(*listaReversa)
 
def binarioaDecimal():
    #Usuario mete el número binario que va a convertir a decimal
    binario = input("Ingresa el número binario a convertir a decimal: ")
    #Se crea variable decimal, la cual nos ayudará en el proceso de conversión.
    decimal = 0
    
    for x in binario:
        decimal = decimal*2 + int(x)
    print ("Tu número en decimal es: \n" + str(decimal))
 
def numeroprimo():
    #Usuario introduce número que quiere saber si es primo
    x= int(input("Introduzca un numero entero:"))
    contador=2
    #Bandera de primo es igual a verdadero
    esPrimo = True
    #Mientras el contador sea menor a x(x siendo el input del número)
    while(contador < x ):
      Si 
      if(x % contador == 0):
        esPrimo = False
      contador = contador + 1
    #Si la 
    if(esPrimo):
        print ("Su numero es primo")
    #Chistorete
    else:
        print ("Su numero no es primo, es tio")

def HexadecimalaDecimal():
   NumoerAconvertir = input ("introduce el número en Hexadecimal que quieras convertir a decimal: ")
   Numeroconvertido = int(NumoerAconvertir,16)
   
   print ("El número convertido a decimal es: " + str(Numeroconvertido))

def decimalaHexadecimal(n):
    n = int(input("Ingresa el número decimal que quieres convertir a hexadecimal: "))
    x=(n%16)
    Hex=""
    
   # if (n<0):
   #     print ("0")
   # else:
   #     x=(n%16)
        #if (x<10):
         #   print(x)
    #while (True):
    #    x = n
    #    x = x // 16
    #    if (x > 15):
    #        x = x//16
    if (x < 10):
        Hex=x 
    if (x == 10):
        Hex="A"
    if (x == 11):
        Hex="B"
    if (x == 12):
        Hex="C"
    if (x == 13):
        Hex="D"
    if (x == 14):
        Hex="E"
    if (x == 15):
        Hex="F"
    
    if (n - x!=0):
        return decimalaHexadecimal(n/16)+str(Hex)
    else:
        return str(Hex)
    #print (str(n%16)+ Hex)

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

def PrimosEnRango():
    menor= int(input("Introduzca el primer numero del rango: "))
    mayor=int(input("Introduzca el ultimo numero del rango: "))
    while (menor<=mayor):
        numeros=[]
        mayor+=1
    #contador=2
    #esPrimo = True
    #while(contador < x ):
    #  if(x % contador == 0):
    #    esPrimo = False
    #  contador = contador + 1
    #if(esPrimo):
    #    print ("Su numero es primo")
    #else:
    #    print ("Su numero no es primo, es tio")

def serpientesyescaleras():
    #Declara Variables del juego
    tiros = 0
    pasos = 0
    indice = 0
    turno = 0
    logro1 = False
    logro2 = True
    ganar = False
    
#Tupula con las posiciones de las serpientes y escaleras
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
 #Listas en las que se almacenan posiciones y nombres  de jugador(es)
    posiciones = []
    nombres = []
    # Se piden número de jugadores al usuario(s)
    n = int(input("Cuantos jugadores habra? "))
    #Se meten en la lista de nombres y se crea su posición en 0
    while (indice < n):
        print("Cual es el nombre del jugador " + str(indice + 1) + "? ")
        nu = input()
        posiciones.append(0)
        nombres.append(str(nu))
        indice = indice + 1
    #Ciclo de los turnos  de los jugadores
    while (ganar == False):
        print("Es turno de " + nombres[turno])
        input ("Presiona una tecla para lanzar los dados: ")
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        tiros+=1
   #Tiro de dados y avance de posición
        print ("Dado 1: " +str( dado1) + "    Dado 2: "+str(dado2)+"    Suma: "+ str(dado1+dado2))
        print ("Avanzas de la posicion " +str(posiciones[turno])) 
        posiciones[turno] = posiciones[turno]+dado1+dado2
        pasos = pasos+dado1+dado2
        if(posiciones[turno]>100):
            deMas=posiciones[turno] -100
            posiciones[turno] = 100 - deMas 
        SyEi= 0
    #comparación de las posicioes actuales con la tupula que contiene las serpientes y escaleras. Se checa si sube de posicion o si baja de posicion 
        while(SyEi < len(portales)):
            if(portales[SyEi] == posiciones[turno]):
                if(portales[SyEi] < portales[SyEi+1]):
                    print("Subes por una escalera de la posicion " + str (posiciones[turno]) +" a la posicion "+ 
                    str (portales[SyEi]))
                else:
                    print("Caes por una serpiente de la posicion " + str(portales[turno]) + " a la posicion " + 
                    str(portales[SyEi + 1]))
                    logro2 = False
                posiciones[turno] = portales[SyEi + 1]
            SyEi = SyEi + 2
    
    
        print ("A la posicion "+str(posiciones[turno]))
    #Si los dados son 1 y 1 se imprime par de ases, lo que hace que el primer Logro sea true
        if (dado1 == 1 and dado2 == 1 and logro1 == False):
            print ("Logro desbloqueado: PAR DE ASES!")
            logro1 = True
        if(posiciones[turno] == 100):
            ganar = True
    #al final de la partida se checa si la persona no cayé en una serpiente, de ser así se imprime el logro 2
            if (logro2 == True):
                print ("Domador de serpientes!")
            print (nombres[turno] + "\nTiraste " + str(tiros) + " veces"  )
            print ("Avanzaste " + str(pasos) + " pasos")
        turno = turno + 1
        if (turno >= n):
            turno = 0

def guebitohKonCacsum():
    #Esta es la magia que le da substancia a todo este programa, sin esto el programa no sirve.
    #algunas personas dirían que gracias a esto... se hace la magia.
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
    
    #Menu, el usuairo mete el número de la operación a realizar, después se llama a la función y se hizo la magia.
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
        decimalaHexadecimal()
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
        #Con los easter eggs es como el menú, sólo que llama a toda las funciones de juego.
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
        print("Gracias por usar la calculadora :D")
        time.sleep(2)
        print("Te queremos ieipi, no nos repruebes de por vida D:")
        time.sleep(1)
        sys.exit()


