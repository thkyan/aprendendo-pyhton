#while True:
#    nome = input('qual o seu nome?')
#    print(f'ola {nome}')
'''
x = 0
while x < 5:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1

print('acabou')
'''
'''
x = 0
while x < 10 :
    y = 0 

    while y < 5 :
        print (f'{x}, {y}')
        y += 1

    x += 1    
'''
while True:
    print()
    num_1 = int(input ('Digite um numero :'))
    num_2 = int(input ('Digite um numero :'))
    operador = int(input ('Digite um operador: '))
    
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um numero.')
        continue
 
    if operador == '+':
        print (num_1 + num_2)
    elif operador == '-':
        print (num_1 + num_2)
    elif operador == '*':
        print (num_1 * num_2)
    elif operador == '/':
        print (num_1 / num_2)
    else:
       print ('operador invalido!')   