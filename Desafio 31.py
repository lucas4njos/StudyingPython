#Exercício Python 031: Desenvolva um programa que
# pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50
# por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Distância em km: '))

if distancia <= 200:
    print(f'Preço: R$ {(distancia*0.5):.2f}')
else:
    print(f'Preço: R$ {(distancia * 0.45):.2f}')
