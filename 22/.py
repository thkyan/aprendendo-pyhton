
lista_de_num_inteiros = [
    [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10], 
    [1, 1, 2, 3 , 4, 5, 6, 6, 7, 8, 9, 10],
    [10, 10, 9, 8, 7, 5, 4, 3, 2, 1, 6],
    [3, 3, 4, 4, 5, 6, 7, 8, 9, 10, 1, 2],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrar_numeros_duplicados(lista_num_inteiros2):
    numeros_checados = set()
    primeiro_duplicado = -1

    for numero in lista_num_inteiros2:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)



    return primeiro_duplicado

for lista_numeros in lista_de_num_inteiros:
    print(encontrar_numeros_duplicados(lista_numeros))