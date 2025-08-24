carro = {
    "pneus":4,
    "portas":2,
    "motor":1,
    "janelas":4
}

print(carro)

#adicionar itens em um dicionário
carro["teto solar"] = 1
print(carro)

#deletar itens em um dicionário
del carro["motor"]
del carro["janelas"]

print(carro)