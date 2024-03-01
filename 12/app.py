numero = input('Digite um numero por favor:')

if numero.isdigit():
    numero=int(numero)
    if numero%2==0:
        print(f'{numero} é numero par.')
    else:
        print(f'{numero} é numero impar.')
else:
    print('digite um numero inteiro...')

