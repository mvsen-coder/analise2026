def imc(a, b):
    y = a / (b * b)
    if y < 18.5:
        print(f"Seu imc é {y} e isso indica magreza")
    elif y >= 18.5 and y <= 24.9:
        print(f"Seu imc é {y} e isso indica normalidade")
    elif y >= 25 and y <= 29.9:
        print(f"Seu imc é {y} e isso indica sobrepeso")
    elif y >= 30 and y <= 34.9:
        print(f"Seu imc é {y} e isso indica obesidade grau I")
    elif y >= 35 and y <= 39.9:
        print(f"Seu imc é {y} e isso indica obesidade grau II")
    elif y >= 40:
        print(f"Seu imc é {y} e isso indica obesidade grau III")
peso = int(input("Digite o seu peso "))
altura = int(input("Digite a sua altura em centimetros "))
altura_metro = altura / 100
x = imc(peso, altura_metro)