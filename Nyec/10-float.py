x = 3.3
y = 1.1 + 2.2

print(x)
print(y)

print(x == y)

#Round sirve para redondear pero el resultado es el mismo
#print(x)
#print(round(y,2))
#print(x == y)

#format permite eliminar los decimales
#Forma de texto
y_str = format(y, ".2g")

print(y_str)

print(y_str == str(x))

#Forma matematica


print('*' * 10)

print(y , x)

tolerance = 0000000.1

print(abs(X-y) < tolerance)