'use stricht'

num = 0
fact = 1
i = 1
respuesta = "SI"

while respuesta.upper() == "SI":
    while True:
        try:
           num = int(input("Escribe un numero: "))
           break
        except ValueError:
            print("Solo datos numericos por favor")
    i = 1
    fact = 1
    while i <= num:
        fact *= i # fact = fact * i
        i += 1 #i = i + 1
    print(f"El factorial de {num} es {fact}")
    respuesta = input("Deseas repetir el proceso (Si/No): ")
print("adios")
    
