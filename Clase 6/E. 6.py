def saludo():
    print("buenos días")

saludo()
print()

def saludo2():
    saludo = "buenos días"
    return saludo

print(saludo2())
print()

def saludo3():
    nombre = input("Escribe tu nombre: ")
    salu = "buenos días " + nombre
    return salu

print(saludo3())