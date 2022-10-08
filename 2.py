##Questão 2

def validaMes(mesDig):
  mes = 0
  while mes not in range(1, 13):
    mes = input(mesDig)
    listaMes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    if mes in listaMes:
      mes = int(mes)
    else:
      print('Valor deve ser entre 1 e 12')
      mes = 0
  return mes

def exibirMes(mesInicial, mesFinal):
  for intervaloMes in range (mesInicial, mesFinal):
    if intervaloMes == 1: print('{} Janeiro'.format(intervaloMes))
    elif intervaloMes == 2: print('{} Fevereiro'.format(intervaloMes))
    elif intervaloMes == 3: print('{} Março'.format(intervaloMes))
    elif intervaloMes == 4: print('{} Abril'.format(intervaloMes))
    elif intervaloMes == 5: print('{} Maio'.format(intervaloMes))
    elif intervaloMes == 6: print('{} Junho'.format(intervaloMes))
    elif intervaloMes == 7: print('{} Julho'.format(intervaloMes))
    elif intervaloMes == 8: print('{} Agosto'.format(intervaloMes))
    elif intervaloMes == 9: print('{} Setembro'.format(intervaloMes))
    elif intervaloMes == 10: print('{} Outubro'.format(intervaloMes))
    elif intervaloMes == 11: print('{} Novembro'.format(intervaloMes))
    else: print('{} Dezembro'.format(intervaloMes))
    
mesInicial = 1
mesFinal = 0
while mesInicial > mesFinal:
  mesInicial = validaMes('\nInsira o mês inicial: ')
  mesFinal = validaMes('Insira o mês final: ')
  if mesInicial > mesFinal:
    print('Mês inicial deve ser menor ou igual ao mês final')
print('\n..:: Intervalo de Mês Informado ::..\n')
exibirMes(mesInicial, mesFinal+1)