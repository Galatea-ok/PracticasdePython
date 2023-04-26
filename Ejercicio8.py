"""Practica 8"""
numero = int(input("introduce un numero: "))
SUMA = 0
while numero > 0:
    suma = SUMA+numero
    numero = int(input("introduzca otro numero: "))
print("La suma de los numeros introducidos es", str(suma))
