import random

primeNumbers = []

#Analiza si el número dado es primo o no, calculando el modulo desde el 2 hasta n-1
def check(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    
    return True

#Analiza un rango de números y entrega los que son primos
for n in range(100, 300):
    if check(n):
        primeNumbers.append(n)

#print(primeNumbers)
print(random.choices(primeNumbers))
print(random.choices(primeNumbers))