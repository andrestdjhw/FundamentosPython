""" Hay tres tipos numéricos distintos: integers, 
    floating point numbers y complex numbers. 
    Además, los booleanos son un subtipo de los enteros.
    Los enteros tiene precisión ilimitada. 
"""
entero = 5
flotante = 2.5
cadena = "Hola"
booleano = True
#Ejercicio numero I
contactenado = print(cadena, entero, flotante, booleano)
#Ejercicio numero II sumatoria de pares hasta 50
contador = 0
while contador <= 50:
    print("Vuelta N: ", contador+2)
    contador+=2