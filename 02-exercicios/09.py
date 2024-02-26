print('Esse programa mmostra a quantidade de números pares e ímpares inseridos')

numeros = []
lista_pares = []
lista_impares = []

for i in range(3):
    numero = int(input('Digite um número inteiro positivo: '))
    if numero < 0:
        print('[ERRO]: número menor que zero. Digite um número positivo')
    else:
        numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

qtd_pares = len(lista_pares)
qtd_impares = len(lista_impares)



print(f'Há {qtd_pares} números pares')
print(f'Há {qtd_impares} números pares')

