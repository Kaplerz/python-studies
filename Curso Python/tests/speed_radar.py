velocidade = 80
posicao = 50

RADAR_1 = 60
POSICAO_1 = 50
ALCANCE = 2

    
if posicao >= (POSICAO_1 - ALCANCE) and posicao <= (POSICAO_1 + ALCANCE) and velocidade > RADAR_1:
    print('Velocidade acima do padrão.')
    print('Veículo multado.')
else:
    print('Velocidade padrão.')
    print('Veículo não multado.')