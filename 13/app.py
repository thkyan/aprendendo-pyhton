nome = input('Qual o seu nome?')
quantidadeLetras = len(nome)

if quantidadeLetras <= 4:
    print('Seu nome é curto.')
elif quantidadeLetras <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
