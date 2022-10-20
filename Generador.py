import random

def generar_contraseña():
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chars = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    contraseña = mayusculas + minusculas + chars + numeros

    contraseña = []

    for i range(15):
    caracter_random = random.choice(contraseña)
    contraseña.append(caracter_random)




def run():
    contraseña = generar_contraseña()
    print ('tu nueva contraseña es: ' + contraseña)