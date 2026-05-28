temp = float(input("insira a temperatura "))
if temp >=18 and temp <=30:
    print(f"{temp}° é considerado agradável")
elif temp <18:
    print(f"{temp}° é considerado frio")
else:
    print(f"{temp}° é considerado calor")