import string


def run():
   compañeros = int(input('¿Cuantos acompañantes tienes?'))
   dinero = int(input('cuanto dinero tienen'))
   if dinero < 15:
    print("Solo les alcanza para el helado de limon")
   elif dinero > 15:
    print('alcanza para el helado de vainilla')
   elif dinero > 20 | dinero > 30:
       print("Te alcanza para el de chocolate")
   elif dinero > 30:
    print("Te alcanza la de menta chocolatada")
    



   


   














if __name__ == '__main__':
    run()