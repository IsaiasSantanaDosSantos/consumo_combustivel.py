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
combustivel = float(input('Digite a quantidade de combustivél que abasteceu: '))
km_rodado = km_final - km_inicial
consumo = km_rodado / combustivel
# A aplicação aguarda 1.5 segundos para execultar a proxima parte.
sleep(1.5)
tipo_comb = 0
# Enquanto 'tipo_comb for diferente de 3:
while tipo_comb != 3:
    print('Qual o combustivél usado?\nDigite:\n[ 1 ] Para ÁLCOOL\n[ 2 ] Para GASOLINA\n[ 3 ] Para SAIR')
    tipo_comb = int(input('Digite sua opção: '))
# Se 'tipo_comb for igual a 1:
    if tipo_comb == 1:
        print('~' * 50)
        print('Seu veiculo rodou em média {} com cada litro de álcool.'.format(consumo))
        print('~' * 50)
# Se 'tipo_comb' for igual a 2:
    elif tipo_comb == 2:
        print('^' * 50)
        print('Seu veicúlo rodou em média {:3f} com cada litro de gasolina.'.format(consumo))
        print('^' * 50)

    elif tipo_comb == 3:
        print('Saindo...')
# Se 'tipo_comb diferente de 1 ou 2:
    else:
        print('=' * 38)
# O progama pergunta novamente até escolher uma das 2 opção corretas.
        print('A opção \033[0:31m{}\033[m é inválida. Tente novamente!'.format(tipo_comb))
        print('=' * 38)
# Agradece
print('Obrigado por utilizar nossa aplicação!')
print('Estamos finalizando...')
# A aplicação aguarda 1.7 segundos para execultar a proxima parte.
sleep(1.7)
# Finaliza de forma visual.
print('Finalizado!')
