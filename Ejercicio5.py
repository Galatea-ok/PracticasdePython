contraseña=input("Introduce contraseña: ")
contador=0
for i in range(len(contraseña)):
    if contraseña[i]==" ":
        contador=1
if len(contraseña)<8 or contador>0:
    print("Contraseña erronea")
else:
    print("Contraseña correcta")