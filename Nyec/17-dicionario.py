"""

dict = {}
for i in range(1,11):
    dict[i] = i * 2
    print(dict)
    
dict_v2 = {i : i * 2 for i in range(1,5)}
print(dict_v2)
"""
"""
import random

countries = ["col", "Mex", "Bol", "Per"]
population = {}
for country in countries:
    population[country] = random.randint(1,100)
    print(population)
    

population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)
"""
names = ["nico", "zule", "santi"]
age = [12, 43, 95]

print(list(zip(names,age)))

new_dic = {names: age for (names,age) in zip(names, age) }

print(new_dic)

