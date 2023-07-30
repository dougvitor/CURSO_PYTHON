"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 90  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

carro_ultrapassou_velocidade_permitida_radar_1 = velocidade > RADAR_1

carro_dentro_do_range_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_dentro_do_range_radar_1 and \
    carro_ultrapassou_velocidade_permitida_radar_1

if carro_ultrapassou_velocidade_permitida_radar_1:
    print('Velocidade do carro utrapassou à permitida pelo radar 1')

if carro_dentro_do_range_radar_1:
    print('Carro dentro do range de detecção do radar 1')

if carro_multado_radar_1:
    print('Carro multado em radar 1')