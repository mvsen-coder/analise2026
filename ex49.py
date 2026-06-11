def alistamento (opção, idd):
    if opção == 1 and idd >= 18:
        print("Você esta apto para o alistamento militar")
    else:
        print("Você não esta apto para o alistamento militar")
idade = int(input("digite sua idade "))
print("escolha o seu genero")
print("1 para masculino")
print("2 para feminino")
genero = int(input("digite o numero da opção "))
alistamento(genero, idade)