lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_c = [x + y for x, y in zip(lista_a, lista_b)]

for soma in lista_c:
    print(soma)