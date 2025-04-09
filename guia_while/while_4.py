numero = int(input("Ingrese un numero. 0 para finalizar: "))
sumaPositivos = 0
productoNegativos = 1

while numero != 0:
    if numero >0:
        sumaPositivos += numero
    else:
        productoNegativos = int(numero) * productoNegativos
    numero = int(input("Ingrese un numero. 0 para finalizar: "))

print(sumaPositivos)
print(productoNegativos)