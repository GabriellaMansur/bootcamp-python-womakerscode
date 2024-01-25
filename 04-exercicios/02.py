numero = int(input('Informe um número: '))

def inverteNumero(numero):
    numero_invertido = int(str(numero)[::-1])
    print(f'O reverso do número informado é {numero_invertido}')

inverteNumero(numero)
