set_countries = {"Mex", "Col", "bol"}
size = len(set_countries)
print(size)

#Comprueba que la vaariable este en el set
print("Col" in set_countries)
print("pe" in set_countries)

#add agrega  variables a los sets

set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

#update Añade cualquier tipo de objeto iterable como: listas, tuplas.
set_countries.update({'ar', 'ecua'})

print(set_countries)

#remove Quita datos de los sets
set_countries.remove('ar')

print(set_countries)

#Discard Elimina un elemento y si ya existe no lanza ningún error.
set_countries.discard('arg')
print(set_countries)
set_countries.add("arg")
print(set_countries)

#Clear elimina todos los datos
#set_countries.clear()
#print(set_countries)

#pop  Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
set_countries.pop()
print(set_countries)