lista_numeros = []
for i in range (0,5):
    x = int(input("digite um numero: "))
    lista_numeros.append(x)
print(lista_numeros)
for x in lista_numeros:
    y = x % 2
    if y == 1:
        print(f"{x} é um numero impar")
    else:
        print(f"{x} é um numero par")