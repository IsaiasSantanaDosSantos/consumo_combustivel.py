from time import sleep

print('↓' * 33)

# Titulo.
print("\033[0:31mCALCULO DE CONSUMO DE CONBUSTIVÉL\033[m")
print('↑' * 33)
print(' ' * 33)
# Orientação.
print('→ Insira os dados solicitados para efetuar o calculo.')
km_inicial = int(input('Digite o KM inicial: '))
km_final = int(input('Digite o KM final: '))
combustivel = float(input('Quantos litros de combustivél que abasteceu: '))
km_rodado = km_final - km_inicial
consumo = km_rodado / combustivel
print('Calculado...')
# A aplicação aguarda 1.5 segundos para execultar a proxima parte.
sleep(1.5)
print('Você rodou \033[0:32m{}\033[m KM com {:.3f} litros de combustivél.'.format(km_rodado, combustivel))
print("Ou seja, seu veiculo está fazendo em média \033[0:32m{:.0f}\033[m km/l.".format(consumo))