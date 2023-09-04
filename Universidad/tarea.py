respuesta = "SI"

while respuesta.upper() == "SI":
    nombre = ""
    while not nombre or "void" in nombre.upper():
        nombre = input("Buen día, por favor escriba su nombre: ")

    edad = 0
    while edad <= 0:
        try:
            edad = int(input(f"Bienvenido {nombre}, escriba su edad por favor: "))
        except ValueError:
            print("Edad no válida. Intente nuevamente.")

    email = " "
    while not email or "void" in email.upper():
        email = input("Por favor introduce un email: ")

    id = 0
    while id <= 0:
        try:
            id = int(input("Favor de generar un ID: "))
        except ValueError:
            print("id no válido. Intente nuevamente.")

    domi = ""
    while not domi or "void" in domi.upper():
        domi = input("Por último, aportenos su domicilio por favor: ")

    print(f"Nombre: {nombre}, Edad: {edad}, Email: {email}, Id: {id}, Domicilio: {domi}, Bienvenido a la familia")

    respuesta = input("¿Desea agregar a otro empleado? (SI/NO) ").upper()
    


print("Adiós")
print(my_lista)