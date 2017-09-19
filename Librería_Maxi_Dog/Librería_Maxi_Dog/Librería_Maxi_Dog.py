
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
    numeros=int(input("Introduce los numeros que quieras sumar, separados por un espacio: \n"))
    numeros =  int(input("Escribe los numeros que quieres sumar, separados por un espacio: \n").split(separator(" ")))
    print(numeros)
    print ("The sum of numbers is: ")+str(sum(numeros))


suma()