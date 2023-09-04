

# no tiene un par key-value, así me doy cuenta que es un set, un conjunto.
set_countries = {"Mex", "Col", "bol"}
print(set_countries)
#print(type(set_countries))

# si yo pongo algo repetido, él me lo quita al imprimir
#set_countries2 = {'col', 'mex', 'bol', 'col'}
#print (set_countries2) # {'col', 'mex', 'bol'}

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(("abc" , "cvd", 'as', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4,]
set_numbers = set(numbers)
print(set_numbers)


size = len(set_countries)
print(size)