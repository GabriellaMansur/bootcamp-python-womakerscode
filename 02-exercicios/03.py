nota = float(input('Digite uma nota entre 0 e 10: '))
while nota > 10 or nota < 0:
    nota = float(input('Valor inválido. Digite novamente: '))

print(f'Sua nota é {nota}')

