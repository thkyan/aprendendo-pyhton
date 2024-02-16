nome = 'thayna'
idade = 17
altura = 1.60
e_menor = idade < 18
peso = 60
imc = peso / altura**2

print('nome:', nome)
print('idade:', idade)
print('altura:', altura)
print('é menor:', e_menor)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))