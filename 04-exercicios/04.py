dinheiro = float(input('Digite quanto dinheiro, em real, você tem na carteira: R$ '))

conversao = {
    'Dólar Americano': 4.91,
    'Peso Argentino': 0.02,
    'Dólar Australiano': 3.18,
    'Dólar Canadense': 3.64,
    'Franco Suiço': 0.42,
    'Euro': 5.36,
    'Libra Esterlina': 6.21
}

for moeda, valor in conversao.items():
    print(f'Com R$ {dinheiro:.2f}, você pode comprar {dinheiro / valor:.2f} {moeda}.')