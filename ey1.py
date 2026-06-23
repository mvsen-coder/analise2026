valor_total = 105.0
saldo_usuario = 100.0
if((input("Voce tem cupom S/N?").lower()) == "s"):
   cupom_valido = True
else:
   cupom_valido = False

if cupom_valido:  #cupom valido ja pergunta sozinho se é true por ser uma variavel booleana. da pra usar o ( if not cupom_valido) tbm pro IF so funcionar se for falso
    valor_total = valor_total * 0.9
    # poderia escrever na forma de decrescimo como por exemplo
    # valor_total -= (valor_total * 0.1)
    # que seria a mesma coisa que escrever valor_total = valor_total - (valor_total * 0.1)


if saldo_usuario >= valor_total:
    print("201 Created - Pedido realizado com sucesso")
else:
    print("4-2 Payment required - Saldo insuficiente")