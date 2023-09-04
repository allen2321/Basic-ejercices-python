class user:
    def __init__(self, nom, pwd):
        self.nom = nom
        self.pwd = pwd
        
u1 = user("Allen", "342")
u2 = user("Carlos", "435")

usuarios = [u1,u2]

n = input("ingrese su usuario")
p = input("ingrese su contraseña")

k = 0

for i in range(len(usuarios)):
    if usuarios [i].nom == n and usuarios [i].pwd == p:
        print(usuarios [i].nom, "Bienvenidos al programa")
        k=1
        break
if k == 0:
   print("intente nuevamente")

