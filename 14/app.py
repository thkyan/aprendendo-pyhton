horario = input('Digite um horario (0-23):')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horario deve estar entre 0 e 23.')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')            
else:
    print('Digite um horario e 0 a 23!')