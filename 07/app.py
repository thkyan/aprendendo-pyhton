maiorNota = 0
contador = 0
nota = 0 
somaNotas = 0

while contador < 3:
    nota = float(input("Digite a nota do aluno"))
    somaNotas = somaNotas+nota

    contador+=1

    if(contador==1):
        maiorNota=nota
    else:
        if(nota>maiorNota):
            maiorNota=nota

media = somaNotas/contador

print(f'a media de notas é {media}'
      f'a maior nota foi {maiorNota}')