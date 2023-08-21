
edad = int(input("Introduce tu edad"))
name = str(input("Introduce tu nombre"))

if(edad <= 9 ):
    print("Eres menor de edad" + name)
elif(edad >= 13 | edad <= 17):
    print("eres adolecente"+ name)

elif(edad >= 18 | edad < 60):
    print("Eres mayor de edad " + name)
    
else:
    print("Estas viejo" + name)
    

