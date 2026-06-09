def imc(a, b):
    return a / (b * b)

peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura em centimetros: "))
altura_metro = altura / 100
c = imc(peso, altura_metro)
print(f"seu imc é: {c}")