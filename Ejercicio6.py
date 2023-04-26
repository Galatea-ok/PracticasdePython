"""Practica 6"""
email=input("Introduce email: ")
contadorArroba=0
ContadorPunto=0
for i in range(len(email)):
    if email[i]=="@":
        contadorArroba=contadorArroba+1
    if email[i]==".":
        ContadorPunto=1
if ContadorPunto==0 or contadorArroba!=1:
    print("email incorrecto")
else:
    print("email correcto")