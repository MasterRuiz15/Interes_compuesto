## Programa

# input
C = int(input("Por favor digete el valor inicial: "))
print("Su capital inicial fue de: "+ str(C))

# processing
n = 0
d = 2 * C

while (C<d):
    C = C + 5*C/100
    n = n + 1

# output
print("Su capital Final es de: "+ str(C), "en "+ str(n), "meses")