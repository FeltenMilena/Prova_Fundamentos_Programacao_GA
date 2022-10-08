partida = 0
timeCasa = 0
golsTimeCasa = 0
timeVisitante = 0
golsTimeVisitante = 0
totalGolsRodada = 0
empates = 0
timeMaisGols = 0
quantidadeTimeMaisGols = 0
quantidadeGolsPartida = 0
continuar = 's'

def jogo():
    try:
        global partida
        global timeCasa
        global golsTimeCasa
        global timeVisitante
        global golsTimeVisitante
        print('\n..:: Partida', partida + 1, '::..')
        timeCasa = input('\nTime da casa: ')
        golsTimeCasa = int(input('Gols marcados: '))
        timeVisitante = input('\nTime da visitante: ')
        golsTimeVisitante = int(input('Gols marcados: '))
    except:
        print('Digitação Incorreta')
        return jogo()    


while continuar in 'Ss':
    jogo()
    partida += 1
    
    totalGolsRodada += golsTimeCasa + golsTimeVisitante

    if golsTimeCasa == golsTimeVisitante:
        empates += 1

    if golsTimeCasa > quantidadeTimeMaisGols:
        quantidadeTimeMaisGols = golsTimeCasa
        timeMaisGols = timeCasa

    if golsTimeVisitante > quantidadeTimeMaisGols:
        quantidadeTimeMaisGols = golsTimeVisitante
        timeMaisGols = timeVisitante

    if golsTimeCasa + golsTimeVisitante > quantidadeGolsPartida:
        quantidadeGolsPartida = golsTimeCasa + golsTimeVisitante
        partidaMaisGols = timeCasa + ' x ' + timeVisitante
    continuar = 'x'
    while continuar not in 'SsNn':
        continuar = input('\nContinuar registrando jogos? (S/N): ')
        
print('\n..:: Relatório da Rodada ::..')
print('Quantidade de jogos realizados:', partida)
print('Quantidade total de gols da rodada:', totalGolsRodada)
print('Média de gols por partida:', totalGolsRodada / partida)
print('Quantidade de empates:', empates)
print('Jogo com maior quantidade total de gols:', partidaMaisGols, 'gols:', 
quantidadeGolsPartida)
print('Time que fez mais gols:', timeMaisGols, 'gols:', quantidadeTimeMaisGols)