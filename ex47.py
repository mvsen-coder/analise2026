def mostra_maior(valor1, valor2):
    if valor1 > valor2:
        print(f"O maior valor é: {valor1}")
    elif valor2 > valor1:
        print(f"O maior valor é {valor2}")
    else:
        print("os dois valores são iguais.")
v1 = int(input("Digite um valor "))
v2 = int(input("Digite um outro valor "))
x = mostra_maior(v1, v2)