name = "Allen"
print(name)

age = "17"

Last_Name = "Zuñiga"
print(Last_Name)

full_name = name + " " + Last_Name

print(full_name)

quote = "i'm Allen"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#Format

#template = "Hola, mi nombre es " + name + " Mi apellido es " + Last_Name
#print(template)

#template = "Hola, mi nombre es  {}   Mi apellido es  {}".format(name,Last_Name)

template = (F"Hola, mi nombre es  {name}   Mi apellido es  {Last_Name}")
print(template)

imprecion = (f"Hola, Tu nombre es {full_name} y tu edad es {age}")
print(imprecion)