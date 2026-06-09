def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    if b == 0:
        print("não é possivel dividir por zero")
        return None
    else:
        return a/b

escolha = ""
while escolha != "0":
    escolha = input("Digite uma opção: 1- somar 2- subtrair 3- multiplicar 4- dividir  ")
    num1 = int(input("digite o primeiro numero: "))
    num2 = int(input("digite o segundo numero: "))
    if escolha == "1":
        x = somar(num1,num2)
    elif escolha =="2":
        x = subtrair(num1,num2)
    elif escolha =="3":
        x = multi(num1,num2)
    elif escolha =="4":
        x = divi(num1,num2)
    print(f"O resultado da operação é {x}")
else:
            print("operação terminada")