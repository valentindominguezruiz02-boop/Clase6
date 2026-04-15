suma_t = 0
canti = 0
while True:
    numero = input("Escribe un numero: ")
    if int(numero) > 0:
        suma_t = suma_t + int(numero)
        canti += 1
    else:
        break
print(suma_t)
print(canti)
print(suma_t//canti)