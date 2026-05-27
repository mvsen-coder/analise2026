an = int(input("digite o ano de nascimento "))
at = int(input("digite o ano atual "))
idd = at - an
print(f"Você tem {idd} e é")
if idd >= 18:
    print("maior de idade")
else:
    print("menor de idade")