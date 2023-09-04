text = "Ella sabe programar en python"

"""
#Nos permite saber si el texto 'javascript' esta dentro del string
print('javascript' in text) #false: no esta

print('python' in text) #True si esta

if 'python' in text:
    print("Lo hiciste bien")
else:
    print('lo hiciste mal')
    
    #LEN TE PERMITE SABER LA LONGUITUD DEL STRING
    """
size = len("Amor")

print(size)

#Upper te permite colocar todo el texto en mayusculas
print(text.upper())
#Lower te permite colocar todo el texto en minusculas
print(text.lower())
#permite saber cuantas veces se repite algo
print(text.count("a"))
#cambia las mayusculas por minusculas y vicebersa
print(text.swapcase())
#Permite saber si el texto empieza con la palabra indexada
print(text.startswith("Ella"))
#permite saber si el texto termina con la palabra indexada
print(text.endswith("python"))
#Permite remplazar el caracter A con el B 
print(text.replace("python", "go"))

text_2 ="Este es un titulo"
print(text_2)
#Hace que la primera letra cambie a mayuscula
print(text_2.capitalize())
#Cada inicial de las palabras se vuelve mayuscula
print(text_2.title())
#Te dice si es un digito
print(text_2.isdigit())