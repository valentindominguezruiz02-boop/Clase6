x = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10]

maximo = 0
minimo = 0

for num in x:
    if num > maximo:
       maximo = num
    else:
       maximo = maximo
 
print(maximo)

for num in x:
    if num < minimo:
        minimo = num
    else:
        minimo = minimo

print(minimo)