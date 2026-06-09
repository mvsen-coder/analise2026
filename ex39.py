numero_secreto = 42
palpite = 0
print("Tente adivinhar o número secreto entre 1 e 100.")

while palpite != numero_secreto:
    try:
        entrada = input("Seu palpite: ")
        palpite = int(entrada)
        if palpite < numero_secreto:
            print("Muito baixo. Tente um numero maior")
        elif palpite > numero_secreto:
            print("Muito alto. Tente um numero menor")
        else:
            print(f"Parabéns! Voce acertou o numero secreto: {numero_secreto}!")
    except ValueError:
                print("Por favor, digite apenas numeros inteiros")