#valores_celulares = [850, 2230, 3500, 5000]
#    for valor in valores_celulares:
#        arquivo.write(str(valor) + '\n')
valores_celulares = [850, 2230, 3500, 5000]
with open('valores_celulares.txt','r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')