numeros = [4, 9, 1 , 9, 3]

def m_num(lista):
    numero_m = 0
    canti = 1
    for num in numeros:
        if num > numero_m:
            numero_m = num
        elif num == numero_m:
            canti += 1
    return [numero_m, canti]

print(m_num(numeros))

