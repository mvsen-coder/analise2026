
dia = input("insira o dia da semana ")
diatratado = dia.lower().strip()
hrs = int(input("no formato de 24h, insira a hora em que sua aula finaliza (ex: 21, 22)"))
if diatratado in ["sexta", "sexta feira", "sexta-feira"] and hrs == 21:
    print("sextou! você merece 1 chopp")
elif diatratado in ["sexta", "sexta feira", "sexta-feira"] and hrs == 22:
    print("sextou! você merece pelo menos 2 chopps")
else:
    print("ainda não sextou! não saia da rotina, e vá estudar")