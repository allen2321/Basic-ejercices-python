from tkinter import Menu


Menu = """
Bienvenido al combersor de monedas 

1 - Pesos Mrxicanos
2 - pesos Argentinos
3 - pesos Chilenos

Elige una opcion: """
opcion = int(input(Menu))

if opcion == 1:
   pesos = input("¿Cuantos pesos Mexicanos tienes?: ")
   pesos = float(pesos)
   valor_dolar = 22
   dolares = pesos / valor_dolar
   dolares = round(dolares, 2)
   dolares = str(dolares)
   print(" Tienes $" + dolares + " dolares")
elif opcion == 2:  
   pesos = input("¿Cuantos pesos Argentinos tienes?: ")
   pesos = float(pesos)
   valor_dolar = 65
   dolares = pesos / valor_dolar
   dolares = round(dolares, 2)
   dolares = str(dolares)
   print(" Tienes $" + dolares + " dolares")
elif opcion == 3:
   pesos = input("¿Cuantos pesos Chilenos tienes?: ")
   pesos = float(pesos)
   valor_dolar = 3875
   dolares = pesos / valor_dolar
   dolares = round(dolares, 2)
   dolares = str(dolares)
   print(" Tienes $" + dolares + " dolares")
else:
   print("coloca una opcion");
        









