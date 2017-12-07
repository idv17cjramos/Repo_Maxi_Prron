#Bienvenido Saint Yeipi
#Importamos el tiempo...

#Lo de abajo es para poder usar caracteres que no estan en el teclado americano
#!/usr/bin/env python
#-*- coding: utf-8 -*-

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
    print("14.-Binario a hexadecimal")
    print("15.-Hexadecimal a binario")
    print("16.-Metros a yardas")
    print("17.-Yardas a metros")
    print("18.-Metros a pulgadas")
    print("19.-Pulgadas a metros")
    print("20.-Calcular Indice de Masa Corporal")
    print("21.-Calcular si es numero primo")
    print("22.-Calcular numeros en un rango")
    print("23.-Extras")
    print ("-"*80+  "\n")

def suma():
    permitidos=["1","2","3","4","5","6","7","8","9","0"," ",".","-"]
    #Solicita un input del usuario
    sumita = input("Introduce numeros a sumar (Separados por un espacio): ")
    comprobar=0
    comprobado=False
    while(comprobado==False):
        if(sumita==""):
            print("Introduce solo numeros")
            sumita=input("Introduce numeros a sumar (Separados por un espacio): ")
        elif (comprobar<len(sumita)):
            while(comprobar<len(sumita)):
                if(sumita[comprobar]in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print("Introduce solo numeros")
                    sumita=input("Introduce numeros a sumar (Separados por un espacio): ")
                if(not sumita==""):
                    comprobado=True
    #Crea una lista en base a los numeros introducidos por el usuario, separandolos por un espacio
    sumita = [(x) for x in sumita.split (" ") ]
    #Elimina letras en caso de haber
    #Suma todos los elementos de la lista "sumita"
    if sumita[len(sumita)-1]=="":
        del sumita[len(sumita)-1]
    total = 0
    for numero in sumita:
        total += float(numero)
    deci=total%1
    if (deci==0):
        total=int(total)
    else:
        total=total
    #Imprime el resultado de la suma
    print ("El resultado es:",total)
 
def resta():
    restita1=[]

    #Solicita un los minuendos, los convierte en una lista separando por un espacio y suma todos los elementos de la lista
    while True:
        try:
            restita1 = int(input("Introduce minuendo: "))
            break
        except:
            print ("Introduce solo un numero")
    
    restita2=[]
    #Solicita los sustraendos, los convierte en una lista separando por un espacio y resta todos los elementos de la lista
    permitidos=["1","2","3","4","5","6","7","8","9","0"," ",".","-"]
    restita2 = input("Introduce sustraendos (Separados por un espacio): ")
    comprobar=0
    comprobado=False
    while(comprobado==False):
        if(restita2==""):
            print("Introduce solo numeros")
            restita2=input("Introduce sustraendos (Separados por un espacio): ")
        elif (comprobar<len(restita2)):
            while(comprobar<len(restita2)):
                if(restita2[comprobar]in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print("Introduce solo numeros")
                    restita2=input("Introduce sustraendos (Separados por un espacio): ")
                if(not restita2==""):
                    comprobado=True
    restita2 = [(x) for x in restita2.split (" ") ]

    total2 = 0
    #for numero2 in restita2:
    #    total2 -= int(numero2)
    #Suma los minuendos y los sustraendos e imprime el resultado
    restita2=list(map(int, restita2))
    restita3=sum(restita2)
    final=restita1-restita3
    print ("El resultado es:",final)
 
def multiplicacion():
    permitidos=["1","2","3","4","5","6","7","8","9","0"," ",".","-"]
    #Solicita los numeros a multiplicar
    multi = input("Introduce numeros que quieras multiplicar (Separados por un espacio): ")
    comprobar=0
    comprobado=False
    while(comprobado==False):
        if(multi==""):
            print("Introduce solo numeros")
            multi=input("Introduce numeros a multiplicar (Separados por un espacio): ")
        elif (comprobar<len(multi)):
            while(comprobar<len(multi)):
                if(multi[comprobar]in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print("Introduce solo numeros")
                    multi=input("Introduce numeros a multiplicar (Separados por un espacio): ")
                if(not multi==""):
                    comprobado=True
    #Crea una lista de los numeros introducidos, separandolos por espacios
    multi = [(x) for x in multi.split (" ") ]
    #Multiplica en orden los elementos de la lista en forma de producto acumulado e imprime el resultado
    total = 1
    for numero in multi:
        total *= float(numero)
    deci=total%1
    if (deci==0):
        total=int(total)
    else:
        total=total
    print ("El resultado es:", total) 

def division():
    #Solicita el dividendo y checa si son numeros
    while True:
        try:
            dividendo  =  int(input("Escribe el dividendo: "))
            break
        except:
            print ("Introduce solo numeros")
    #Solicita el divisor
    while True:
        try:
            divisor  =  int(input("Escribe el divisor: "))
            break
        except:
            print("Introduce solo numeros")
    #divide el dividendo entre el dividor e imprime el resultado
    cociente=(int(dividendo)/int(divisor))
    verificador=(int(dividendo)%int(divisor))
    if verificador==0:
        print (int(cociente))
    else:
        print (cociente)
 
def modulo():
 #Solicita el dividendo
    while True:
        try:
            dividendo  =  int(input("Escribe el dividendo: "))
            break
        except:
            print ("Introduce solo numeros")
    #Solicita el divisor
    while True:
        try:
            divisor  =  int(input("Escribe el divisor: "))
            break
        except:
            print("Introduce solo numeros")
    #divide el dividendo entre el divisor e imprime el residuo
    print ("El resultado es: ")
    print (int(dividendo)%int(divisor))
 
def raiz():
    cuadrada = 2
    #Solicita el numero base y el exponente y checa si son numeros
    while True:
        try:
            numeroBase = float(input("Escriba el radicando: "))
            break
        except:
            print("Introduce solo numeros")
    while True:
        try:
            exponente = float(input("Escriba el indice: "))
            break
        except:
            print("Introduce solo numeros")
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
 #Este ya quedo
def potencia():
    permitidos=["1","2","3","4","5","6","7","8","9","0","",".","-"]
    #Solicita el numero base y el exponente
    numeroBase = input("Introduce el coeficiente: ")
    comprobar=0
    comprobado=False
    while(comprobado==False):
        if(numeroBase==""):
            print("Introduce solo numeros")
            numeroBase=input("Introduce el coeficiente: ")
        elif (comprobar<len(numeroBase)):
            while(comprobar<len(numeroBase)):
                if(numeroBase[comprobar]in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print("Introduce solo numeros")
                    numeroBase=input("Introduce el coeficiente: ")
                if(not numeroBase==""):
                    comprobado=True
    exponente = input("Introduce el exponente al que lo quiera elevar: ")
    comprobar=0
    comprobado=False
    while(comprobado==False):
        if(exponente==""):
            print("Introduce solo numeros")
            exponente=input("Introduce el exponente al que lo quiera elevar: ")
        elif (comprobar<len(exponente)):
            while(comprobar<len(exponente)):
                if(exponente[comprobar]in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print("Introduce solo numeros")
                    exponente=input("Introduce el exponente al que lo quiera elevar: ")
                if(not exponente==""):
                    comprobado=True
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
    while True:
        try:
            metros=float(input("Escribe la cantidad de metros a convertir: "))
            break
        except:
            print ("Introduce solo numeros")
    #Esta es la equivalencia de yardas por metro
    yardas = 1.09361
    #Se multiplican los metros por su equivalencia en yardas y se imprime el resultado
    print ("El resultado es: ")
    print ((metros*yardas),"yardas")
 
def yardasaMetros():
    #Se solicitan al usuario los yardas a convertir
    while True:
        try:
            yardas=float(input("Escribe la cantidad de yardas a convertir: "))
            break
        except:
            print ("Introduce solo numeros")
    #Esta es la equivalencia en metros por yarda
    metros = 0.9144
    #Se multiplican las yardas por su equivalencia en metros y se imprime el resultado
    print ("El resultado es: ")
    print ((yardas*metros),"metros")

def metrosaPulgadas():
    #Se solicita al usuario la cantidad de metros
    while True:
        try:
            metros = float(input("Escribe la cantidad de metros a convertir: "))
            break
        except:
            print ("Introduce solo numeros")
    #Equivalencia de pulgadas en un metro
    pulgadas = 39.3701
    #Se imprime el resultado y se multiplica pulgadas(que es valor continuo) por metros(que es la cantidad que se le pide al usuario)
    print ("El resultado es: ")
    print ((metros*pulgadas),"pulgadas")
 
def pulgadasaMetros():
    #Se solicita al usuario la cantidad de pulgadas
    while True:
        try:
            pulgadas = float(input("Escribe la cantidad de pulgadas a convertir: "))
            break
        except:
            print ("Introduce solo numeros")
    #Equivalencia de metrso en una pulgada
    metros = 0.0254
    #Se imprime el resultado y se multiplica metros(que es valor continuo) por pulgadas(que es la cantidad que se le pide al usuario)
    print ("El resultado es: ")
    print (pulgadas*metros,"metros")
 
def IMC():
    #Se le pide al usuario que meta su sexo, peso y estatura.
    while True:
        sexo=input("Eres mujer u hombre? ")
        if sexo.lower()== "mujer" or sexo.lower()=="hombre":
            break
        else:
            print("Solo puedes introducir mujer u hombre")
    while True:
        try:
            peso=float(input("Introduce tu peso en kilos: "))
            break
        except:
            print ("Introduce solo numeros")
    while True:
        try:
            estatura=float(input("Introduce tu estatura en metros: "))
            break
        except:
            print("Introduce solo numeros")
    # Sexo se pasa a minúsculas
    sexo.lower()
    #Se calcula el IMC con la fórumla y se imprime la cantidad del índice de masas corporal.
    imc=(peso/(estatura)**2)
    print ("Tu indice de masa corporal es: " + str(imc))
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
    while True:
        try:
            numero = int(input("Ingresa el número que quieres convertir a binario: "))
            break
        except:
            print("Introduce solo numeros")
    listaBinarial = []
    #Mientras el input sea mayor a cero, se hace el siguiente bucle
    while(numero>0):
        #Calcula el módulo del input
        residuo=numero%2
        #Mete el input en una lista
        listaBinarial.append(str(residuo))
        #Divide input entre 2
        numero = numero//2
    #Reacomoda la lista de atrás hacia adelante
    listaReversa = reversed(listaBinarial)
    #Imprime lista al revés como el número binario.
    print("Tu número binario es:","".join(listaReversa))

def BinarioaHexa():
    permitidos=["0","1"]
    numero=input("Introduce el numero binario que quieres convertir a hexadecimal: ")
    comprobar=0
    comprobado=False
    while(comprobado==False):
        if(numero==""):
            print("Introduce solo numeros")
            numero=input("Introduce numeros a sumar (Separados por un espacio): ")
        elif (comprobar<len(numero)):
            while(comprobar<len(numero)):
                if(numero[comprobar]in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print("Introduce solo numeros")
                    numero=input("Introduce numeros a sumar (Separados por un espacio): ")
                if(not numero==""):
                    comprobado=True
    decimal=0
    Hexa=""
    for x in numero:
        decimal=decimal*2+int (x)
    decimal=int(decimal)
    while ((decimal//2)!=0):
        Hexa=str(decimal%2)+Hexa
        decimal=decimal//2
    bina=(str(decimal)+Hexa)
    hexadecimal=hex(int(bina,2))
    print ("Tu resultado es",hexadecimal)

def HexaABinario():
    permitidos=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    Hexadecimal=input("Introduce el numero hexadecimal que quieres convertir a binario: 0x")
    comprobado=False
    comprobar=0
    while(comprobado==False):
        if(Hexadecimal==""):
            print("Introduce solo numeros")
            Hexadecimal=input("Introduce numeros a sumar (Separados por un espacio): ")
        elif (comprobar<len(Hexadecimal)):
            while(comprobar<len(Hexadecimal)):
                if(Hexadecimal[comprobar]in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print("Introduce solo numeros")
                    Hexadecimal=input("Introduce numeros a sumar (Separados por un espacio): ")
                if(not Hexadecimal==""):
                    comprobado=True
    Hexadecimal=int(Hexadecimal,16)
    listaBinarial = []
    while(Hexadecimal>0):
        #Calcula el módulo del input
        residuo=Hexadecimal%2
        #Mete el input en una lista
        listaBinarial.append(str(residuo))
        #Divide input entre 2
        Hexadecimal = Hexadecimal//2
    #Reacomoda la lista de atrás hacia adelante
    #listaReversa = reversed(listaBinarial)
    listaBinarial.reverse()
    #Imprime lista al revés como el número binario.
    #print ("".join(listaBinarial))
    print("Tu número binario es:","".join(listaBinarial))


def binarioaDecimal():
    #Usuario mete el número binario que va a convertir a decimal
    permitidos=["0","1"]
    binario = input("Ingresa el número binario a convertir a decimal: 0x")
    comprobar=0
    comprobado=False
    while(comprobado==False):
        if(binario==""):
            print("Introduce solo numeros")
            binario=input("Introduce numeros a sumar (Separados por un espacio): ")
        elif (comprobar<len(binario)):
            while(comprobar<len(binario)):
                if(binario[comprobar]in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print("Introduce solo numeros")
                    binario=input("Introduce numeros a sumar (Separados por un espacio): ")
                if(not binario==""):
                    comprobado=True
    #Se crea variable decimal, la cual nos ayudará en el proceso de conversión.
    decimal = 0
    for x in binario:
        decimal = decimal*2 + int(x)
    print ("Tu número en decimal es:",str(decimal))

def numeroprimo():
    #Usuario introduce número que quiere saber si es primo
    while True:
        try:
            x= int(input("Introduzca un numero entero: "))
            break
        except:
            print ("Introduce solo numeros")
    #Bandera de primo es igual a verdadero
    esPrimo = True
    #Mientras el contador sea menor a x(x siendo el input del número)
    if x>1:
      for i in range(2,x):
        if (x%i)==0:
            esPrimo=False
    #Si la bandera se mantiene como verdadera dice que el numero es primo
      if(esPrimo==True):
          print ("El numero",x,"es primo")
    #Si la bandera cambia lanza un mensaje diciendo que no es primo
      else:
          print ("El numero",x,"no es primo")
    else:
        print("El numero",x,"no es primo")

def HexadecimalaDecimal():
   permitidos=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
   NumoerAconvertir = input ("Introduce el número en Hexadecimal que quieras convertir a decimal: 0x")
   #Hexadecimal=input("Introduce el numero hexadecimal que quieres convertir a binario: ")
   comprobado=False
   comprobar=0
   while(comprobado==False):
       if(NumoerAconvertir==""):
           print("Introduce solo numeros")
           NumoerAconvertir=input("Introduce numeros a sumar (Separados por un espacio): ")
       elif (comprobar<len(NumoerAconvertir)):
           while(comprobar<len(NumoerAconvertir)):
               if(NumoerAconvertir[comprobar]in permitidos):
                   comprobar+=1
               else:
                   comprobar=0
                   print("Introduce solo numeros")
                   NumoerAconvertir=input("Introduce numeros a sumar (Separados por un espacio): ")
               if(not NumoerAconvertir==""):
                   comprobado=True
   Numeroconvertido = int(NumoerAconvertir,16)
   
   print ("El número convertido a decimal es: " + str(Numeroconvertido))

def decimalaHexadecimal():
    n = input("Ingresa el número decimal que quieres convertir a hexadecimal: ")
    Hexa=""
    permitidos=["1","2","3","4","5","6","7","8","9","0"]
    comprobar=0
    comprobado=False
    while (comprobado==False):
        if (n==""):
            print ("Ingrese solo numeros")
            n=int(input("Ingresa el número decimal que quieres convertir a hexadecimal: "))
        elif (comprobar<len(n)):
            while (comprobar<len(n)):
                if(n[comprobar] in permitidos):
                    comprobar+=1
                else:
                    comprobar=0
                    print ("Ingrese solo numeros")
                    n=(input("Ingresa el número decimal que quieres convertir a hexadecimal: "))
            if(not n==""):
                comprobado=True
    n=int(n)
    while ((n//2)!=0):
        Hexa=str(n%2)+Hexa
        n=n//2
    bina=(str(n)+Hexa)
    hexadecimal=hex(int(bina,2))
    print ("Tu resultado es",hexadecimal)

def ahorcado():
    #diccionarios con frases que se va a jugar
    frases = {"InFamous":["no pidas una vida mas facil pide ser mas fuerte","todo hombre es responsable del bien que no ha hecho","no pienso hacer esto cada vez para que tu mojes"],
              "Terminator":["i will be back","hasta la vista baby","estoy viejo no obsoleto"],
              "Star Wars":["luke soy tu padre","siempre en movimiento esta el futuro","no lo intentes hazlo"],          
              "Harry Potter":["para una mente bien preparada la muerte es solo la siguiente gran aventura","es hora de elegir entre lo que es facil y lo que es correcto","la gente encuentra mas facil perdonar a los demas por equivocarse que por acertar"],
              "God Of War":["la medida de un hombre es lo que hace con el poder","la esperanza es para los debiles pandora","en la oscuridad el fuego de la esperanza nos liberara"]}
    #elección de categoría de manera random
    categoria = random.choice(list(frases.keys()))
    #Elección de frase de manera random
    frase = random.choice(frases[categoria])
    #Sprites del aahorcado
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
    #--------------------------------
    #VARIABLES
    #------------------------------
    palabra = list(frase)
    vacio = "_"*len(frase)
    correctas = list(vacio)
    errores = 0
    turnos = 0
    flag = True
    perder = False
    ganar = False
    #---------------------------------
    #
    #---------------------------------

    print("Vamo a jugál con frases de " + str(categoria))

    while(ganar == False and perder == False):
    #Impresión de los errores que ha cometido el jugador
        print(dibujo[errores])
        print(*correctas)
    #checar si el jugador usa una letra, que ya había usado con anterioridad y  checar si la letra que usa es correcta
        intento = input("Ingresa una letra y averigua si esta dentro de la palabra secreta: ")
        if (intento in correctas):
            print("Ya usaste esa letra!")
            flag = True
        contador = 0
    #Game loop, checa  input de usuario, ve si está en la frase que va a usar
        while (contador < len(palabra)):
            espacios = " "
            if (espacios in palabra[contador]):
               correctas[contador] = espacios
            if (intento in palabra[contador]):
                correctas[contador] = intento
            contador = contador + 1
    #IMpresión de si está correcto o no
            if (contador == len(palabra) and flag == False):
                print("correcto!")
        if(intento not in palabra):
            print("No esta!")
            errores = errores + 1
    #Si los errores son 7, se acaba el juego, se dibuja el sprite final y se le dice al jugador la frase que era
        if (errores == 7):
            print ("Perdiste, moriras agonizantemente")
            print("PD: La palabra era " + str(frase))
            perder = True
    #Si todas las letras se adivinan, se le notifica al jugador y acaba el juego.
        if (correctas == palabra):
            print(*correctas)
            print("Eres una chingoneria, le atinaste!")
            print("PD: Y solo te tomo " +str(turnos) + " intentos!")
            ganar = True
        turnos += 1

def PrimosEnRango():
    Numeros=[]
    verificar=0
    EsPrimo=True
    while True:
        try:
            menor= int(input("Introduzca el primer número del rango: "))
            break
        except:
            print ("Introduce solo numeros")
    print("")
    while True:
        try:
            mayor=int(input("Introduzca el último número del rango: "))
            break
        except:
            print ("Introduce solo numeros")

    for i in range(menor,mayor+1):
        if i>1:
            for num in range(2,i):
                if (i%num)==0:
                    break
            else:
                Numeros.append(i)
    print("\n"+"Los numeros primos en ese rango son:",*Numeros)

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
    time.sleep(1)

#bandera para saber si el usuario quiere hacer otra operación
continuar = True

#Se manda a llamar la función presentación, la cual ha ce un display del mensaje de bienvenida y le pregunta al usuario qué función es la que quiere hacer.
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
        BinarioaHexa()
    elif (operacion == "15"):
        HexaABinario()
    elif (operacion == "16"):
        metrosaYardas()
    elif (operacion == "17"):
        yardasaMetros()
    elif (operacion=="18"):
        metrosaPulgadas()
    elif(operacion =="19"):
        pulgadasaMetros()
    elif(operacion=="20"):
        IMC()
    elif(operacion=="21"):
        numeroprimo()
    elif(operacion=="22"):
        PrimosEnRango()
    elif(operacion =="23"):
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

    print(" ")
    pregunta = input('Quieres hacer otra operacion?(escribe "Si" o "No")\n')
    if not pregunta=="si" or not pregunta== "no":
        print ('Escribe "Si" o "No"\n')
        pregunta=input('Quieres hacer otra operacion?(escribe "Si" o "No")\n')
        if(pregunta =="no"):
            print("Gracias por usar la calculadora :D")
            time.sleep(2)
            print("Te queremos ieipi, no nos repruebes de por vida D:")
            time.sleep(1)
            sys.exit()
        elif(pregunta=="si"):
            presentacion()
            continue

