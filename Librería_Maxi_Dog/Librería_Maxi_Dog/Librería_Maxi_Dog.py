
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

operacion=input()
operacion=str.lower(operacion)
separator = " "

def suma():
<<<<<<< HEAD
    # Aqui se hace la machaca *pas pas*
    sumita = input("Introduce numeros: ")
    sumita = [int(x) for x in sumita.split (" ") ] 
    total = 0 
    for numero in sumita:
        total += numero
    print ("La suma es:", total)
=======
    numeros=int(input("Introduce los numeros que quieras sumar, separados por un espacio: \n"))
    numerosSeparados=[numeros.split(" ")]
    return (numerosSeparados)
print (suma())
#    numeros =  int(input("Escribe los numeros que quieres sumar, separados por un espacio: \n").split(separator(" ")))
#    print(numeros)
#    print ("The sum of numbers is: ")+str(sum(numeros))
>>>>>>> 4f25e961a9820f40fedb86e951cef83a83c886bc

def resta():
    # Aqui se hace la machaca *pas pas*
    restita = input("Introduce numeros: ")
    restita = [int(x) for x in restita.split (" ") ] 
    total = 0 
    for numero in restita:
        total = numero
    print ("La resta es:", total)

suma()
<<<<<<< HEAD
resta()
=======

>>>>>>> 4f25e961a9820f40fedb86e951cef83a83c886bc
