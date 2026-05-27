#idd = int(input("digite sua idade "))
#gen = (input("Você se identifica com o genero Masculino ou Feminino? ")).lower().strip()
#if idd >= 18 and gen == "masculino":
#    print("Você está apto para o alistamento militar")
#else:
#    print("Você não está apto para o alistamento militar")
#
#
idd = int(input("digite sua idade "))
print("escolha o seu genero")
print("1 para masculino")
print("2 para feminino")
opção = int(input("digite o numero da opção "))
if opção == 1 and idd >= 18:
    print("Você esta apto para o alistamento militar")
else:
    print("Você não esta apto para o alistamento militar")
