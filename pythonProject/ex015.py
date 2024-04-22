km = float(input('Digite quantos km você rodou com o carro?: ')) * 0.15
dias = int(input('Quantos dias ficou em posse do carro?: ')) * 60
pg = km + dias
print('O valor a pagar é de: R$ {}'.format(pg))