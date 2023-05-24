import os
if os.system:
    os.system("cls")
Salir = 1

while True :
    Nombre = input("Digite su nombre: ")
    Cedula = input("Digite cedula: ")
    Cantidad = int(input("Digite la cantidad: "))
    Valor1 = int(input("Digite el valor1: "))
    Valor2 = int(input("Digite el valor2: "))
    
    if Salir==1:
        break
if os :
    os.system("clear")
    os.system("cls")
    
print("**********************Gracias por su compra**************************")
print("*********************************************************************")
print("****************************Tienda***********************************") 
print(f"Nombre: {Nombre}")
print(f"Cedula: {Cedula}")
print("*********************************************************************")
print("*********************************************************************")
print("*********************************************************************")
print(f"Cantidad: {Cantidad}")
print(f"Valor: {Valor1}")
print(f"Valor: {Valor2}")
print("*********************************************************************")
print(f"Vuelto: {Cantidad - (Valor1 + Valor2)}")
print("*********************************************************************")
print("*********************************************************************")
print("*********************************************************************") 
print("*********************************************************************")



