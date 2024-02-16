nome = 'thiago'
idade = 17
altura = 1.78
peso = 65
ano_atual = 2024
#agora vamos calcular alguns dados baseados nas informações do thiago
imc = peso / altura**2
ano_nasceu = ano_atual - idade-1

print(f'{nome} tem {idade} anos de idade e {altura} de altura, seu imc é: {imc:.2f}, e nasceu em {ano_nasceu}')