estoque = [{ "id":1, "nome": "Mochila", "quantidade": 4, "preco": 289.90 },
           { "id":2, "nome": "Boné", "quantidade": 15, "preco": 50.00 },
           { "id":3, "nome": "Casaco", "quantidade": 7, "preco": 149.90 },
            ]

# estoque.append({ "id": len(estoque)+1, "nome": input("nome: "), "quantidade": int(input("qtd: ")), "preco": float(input("preço: ")) })

# print(estoque)

i = 0
while True:
    if input("Digite 0 para finalizar") == "0":
        break
    estoque.append({ "id": len(estoque)+1, "nome": input("nome: "), "quantidade": int(input("qtd: ")), "preco": float(input("preço: ")) })

for i in estoque:
    print(f'Produto: {i["nome"]} | {i["quantidade"]} unidades em estoque | valor: R$ {i["preco"]}')

print(estoque[1]["nome"]) #vai imprimir o nome do segundo produto



lista = []
lista.append("A")
lista.append("A")
lista.append("Bola")
lista.append("A")
lista.remove("A") #remove o primeiro A que encontrar na lista