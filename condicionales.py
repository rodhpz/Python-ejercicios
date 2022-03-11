#Ejercicios Condicionales

#ejercicio1

edad=int(input("ingrese su edad: " ))
if edad>18:
    print("es mayor de edad")
else:
    print("es menor de edad") 


#ejercicio2 

password="123456"
contraseña=input("ingrese su contraseña: ")
if contraseña==password:
    print("su contraseña es correcta")
else:
    print("su contraseña es incorrecta")    


#ejercicio3

numero=int(input("ingrese un numero: "))
if numero%2==0:
   print("el numero es par")
else:
   print("el numero es impar") 


#jercicio4

numentero=int(input("ingrese un numero entero: "))
if numentero<0:
    print("el numero es negativo")
elif numentero>0:
    print("el numero es positivo")  


#ejercicio5

num=int(input("ingrese un numero: "))
num2= int(input("ingrese un segundo numero: "))
if num==num2:
    print("los numeros son iguales")
else:
    print("los numeros son diferentes")


#ejercicio6

preciounitario=int(input("ingrese el precio: "))
cantidad=int(input("ingrese la cantidad: "))
if cantidad>20:
   descuento=10
if cantidad<=20 and cantidad >10:
    descuento=5
if cantidad<=10:
   descuento=0

monto=preciounitario*cantidad(descuento//100)
print("monto a pagar {} con {}% de descuento".format(monto,descuento))


#ejercicio7

año=int(input("introduzca año: "))
if año%4==0  and año%100!=0 or año%400==0:
    print("el año es bisiesto")
else:
    print("el no es no es bisiesto")   




