
edad = int(input("Introduce tu edad: "))
name = str(input("Introduce tu nombre: "))

if edad < 9 :
    print(f"Eres menor de edad:{name}")
elif edad < 18:
    
    print(f"eres adolecente:{name}")

elif edad < 60:
    print(f"Eres mayor de edad:{name}")
else:
    print(f"Estas viejo Felicidades anciano:{name}")
    


