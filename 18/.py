'''
preço = 1500
custo = 400
lucro = 800

def carga_tributaria(preço, custo, lucro):
    imposto = preço - custo - lucro
    return imposto/preço

print("A carga tributaria foi de {:.1%}".format(carga_tributaria(preço, custo, lucro)))
'''

# objeto.upper() = deixa a string com letras maiusculas, nao tem parametros
# objeto.sort() = serve para colocar os numeros em ordem crescente e .sort(reverse = true) para ordem decrescente
# objeto.extend(objeto que queira adicionar) = 1 parametro obrigatorio
'''
def padronizar_codigos(lista_codigos, padrao = 'm'):
    for i, item in enumerate(lista_codigos):
        item = item.replace(' ','')
        item = item.strip()
        if padrao == 'm':
            item = item.casefold()
        elif padrao == 'M':
            item = item.upper()
        lista_codigos[i] = item
    return lista_codigos

cod_produtos = [' ABC12 ', 'abc34', 'abC56 ']
print(padronizar_codigos(cod_produtos, 'm'))
'''
'''
vendas = {'VE0001': (9868, 'concluido', ''), 'VE0002': (9642, 'concluido', ''), 'VE0003': (6007, 'cancelado', 'falta de estoque'), 'VE0004':(15562, 'concluido', '')}
def calculo_stockout(dicionario_vendas):
    numerador = 0 
    denominador = 0
    for venda in dicionario_vendas:
        valor, status, motivo = dicionario_vendas[venda]
        if status == 'concluido':
            denominador += valor
        elif status == 'cancelado' and motivo == 'estoque em falta':
            denominador += valor
            numerador += valor
    return numerador/denominador

print('{:.2%}'.format(calculo_stockout(vendas)))
'''

