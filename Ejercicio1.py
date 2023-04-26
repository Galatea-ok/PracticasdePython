#Ejercicio 1.1
num1=(int(input("Introduce un numero: ")))
num2=(int(input("Introduce otro numero: ")))
def devuelveMax(n1,n2):
   if n1<n2:
      print(n2)
   elif n2<n1:
        print(n1)
   else:
       print("son iguales")
print("El numero mas grande es:  ")
devuelveMax(num1,num2)
