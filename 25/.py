carrinho = []

carrinho.append(('produto 1', 40))
carrinho.append(('produto 2', 25))
carrinho.append(('produto 3', 50))

total = sum([float(y) for x, y in carrinho])

print(total)