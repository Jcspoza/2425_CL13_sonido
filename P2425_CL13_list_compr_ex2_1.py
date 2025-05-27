# Ex1.1: cuadrados de los numero del 1 al 10, pares con List comprehension
cuadradosNumerosParesLC = [x*x for x in range(1,11) if x % 2 == 0] 
    
print(cuadradosNumerosParesLC)