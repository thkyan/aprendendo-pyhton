nomes = ['joao','luiza', 'thayna','thiago']
with open('nomes.txt','r+') as arquivo:
    for nomes in arquivo:
        print(nomes)
    arquivo.write('jully') 
