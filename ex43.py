def roubo(a):
    return a * 0.275
salario = int(input("digite seu salario: "))
c = roubo(salario)
n = salario - c
print(f"Você vai ser roubado em {c} reais todo mês")
print(f"vai sobrar para o beta {n} reais por mês")