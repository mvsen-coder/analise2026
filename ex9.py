val = float(input("digite um valor "))
porcentagem = int(input("digite a porcentagem (ex: 15):"))
resultado = val * (porcentagem / 100)
print(f"{porcentagem}% de {val} é {resultado:.0f}")