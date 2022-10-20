def run(Palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    es_palabra = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
             return False

    palabra = input("escribe una palabra: ")

    es_palindromo = palindormo(palabra)

    if es_palindromo == True:

        print("esa palabra es un palindomo")

    else:

        print("no es palindomo")

if __name__ == '__main__':
    run()