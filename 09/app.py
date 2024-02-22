num1 = input('insira um numero:')
num2 = input('insira outro numero:')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('nao pude converter os numeros para realizar a conta')