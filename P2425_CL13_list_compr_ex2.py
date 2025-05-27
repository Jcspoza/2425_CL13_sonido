# Ex1: cuadrados de los numero del 1 al 10, pares
cuadradosNumerosPar = [] # creamos una lista vacia
for x in range(1, 11):
    if x % 2 == 0:
        cuadradosNumerosPar.append(x * x)
        # vamos añadiendo cuadrados solo si par
    
print(cuadradosNumerosPar)