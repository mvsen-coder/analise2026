'''
cargo = input("insira seu cargo ").lower().strip()
caixa = 1500
vendedor = 2400
gerente = 4000
caixainss = caixa * 0.12
vendedorinss = vendedor * 0.12
gerenteinss = gerente * 0.12
caixairrf = caixa * 0.08
vendedorirrf = vendedor * 0.14
gerenteirrf = gerente *0.14
caixafinal = caixa - caixainss - caixairrf
vendedorfinal = vendedor - vendedorinss - vendedorirrf
gerentefinal = gerente - gerenteinss - gerenteirrf
if cargo == "caixa":
    print(f"Cargo: caixa. salario final com descontos: R$ {caixafinal}. valor descontado do irrf: R$ {caixairrf}. valor descontado do inss: R$ {caixainss}")
elif cargo == "vendedor":
    print(f"Cargo: vendedor. salario final com descontos: R$ {vendedorfinal}. valor descontado do irrf: R$ {vendedorirrf}. valor descontado do inss: R$ {vendedorinss}")
elif cargo == "gerente":
    print(f"Cargo: gerente. salario final com descontos: R$ {gerentefinal}. valor descontado do irrf: R$ {gerenteirrf}. valor descontado do inss: R$ {gerenteinss}")
else:
    print("Não trabalha aqui")
'''

cargo = input("insira seu cargo ").lower().strip()
if cargo == "caixa":
    sal = 1500
elif cargo == "vendedor":
    sal = 2400
elif cargo == "gerente":
    sal = 4000
else:
    sal = 0
    print("Não trabalha aqui")
inss = sal * 0.12
if (sal > 2000):
    irrf = sal * 0.14
else:
    irrf = sal * 0.08
salfinal = sal - irrf - inss
print(f"seu salário é R$ {sal:.0f}")
print(f"o desconto de inss é R$ {inss:.0f}")
print(f"o desconto de irrf é R$ {irrf:.0f}")
print(f"o salário final é R$ {salfinal:.0f}")