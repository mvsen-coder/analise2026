nota = 0
while nota >= 0 and nota <= 10:
    try:
        nota = int(input("Digite uma nota entre 0 e 10: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número")
print(f"Nota inválida registrada: {nota}")