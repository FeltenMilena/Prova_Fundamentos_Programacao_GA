#Questão 1
base = float(input('Informe a medida da base da embalagem em cm: '))
altura = float(input('Informe a medida da altura da embalagem em cm: '))
profundidade = float(input('Informe a medida da profundidade da embalagem em cm): '))
peso = float(input('Informe o peso da embalagem em kg: '))
distancia = float(input('Informe a distância que será percorrida pela encomenda em km: '))

volume = base * altura * profundidade
print('O volume da embalagem é {:.2F} cm³'.format(volume))

frete = volume * peso * distancia / (7.5 * 10**4)
print('O valor do frete é R$ {:.2F}'.format(frete))