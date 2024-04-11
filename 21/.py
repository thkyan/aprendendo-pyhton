# def funcao(agr, agr2):
#     return agr * agr2

# var = funcao(2,3)

# a = lambda x, y: x * y

# print(a(2, 2))

# lista = [
#     ['p1', 13],
#     ['p2', 1],
#     ['p3', 18],
#     ['p4', 8],
# ]

# # lista.sort(key=lambda item:[1], reverse = True)
# print(sorted(lista, key = lambda item: item[1]))

#########################

perguntas = {
    'pergunta 1':{
        'pergunta': 'quanto eh 2 + 2?',
        'respostas': {'a': '1','b': '3','c': '4',},
        'resposta_certa':'letra c',
    },
    'pergunta 2':{
        'pergunta': 'quanto eh 2 + 1?',
        'respostas': {'a': '1','b': '3','c': '4',},
        'resposta_certa':'letra b',
    },
}
print()
respostas_certas = 0 
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')
    

if resposta_usuario == pv['resposta_certa']:
    print('acertouuu!')
    respostas_certas =+ 1
else:
    print('errou!')

print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'vc acertou {respostas_certas} respostas.')
print(f'sua porcetagem de acerto foi de {porcentagem_acerto}%')