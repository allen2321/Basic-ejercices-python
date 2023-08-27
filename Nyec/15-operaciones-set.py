set_a = {"mex", "col", "bol"}
set_b = {"pe", 'bol'}

#"union" Realiza la operacion “union” entre dos conjuntos. La unión entre dos conjuntos es 
# sumar los elementos de estos sin repetir elementos.
set_c = set_a.union(set_b)
print(set_c)

#"intersection": Realiza la operacion “intersection” entre dos conjuntos. 
# La intersección entre dos conjuntos es tomar unicamente los elementos en común de los conjutnos.
set_c = set_a.intersection(set_b)
print(set_c)

#difference: Realiza la operacion “difference” entre dos conjuntos. 
# La diferencia entre dos conjuntos es restar los elementos del segundo conjunto al primero.
set_c = set_a.difference(set_b)
print(set_c)

#Symetric-difference:Realiza la operacion “symmetric_difference” entre dos conjuntos. 
# La diferencia simetrica entre dos conjutnos consta de restar todos los elementos de ambos exceptuando el elemento en común.
set_c = set_a.symmetric_difference(set_b)
print(set_c)