carrinho = {}

carrinho['batata palha'] = 2
carrinho['arroz'] = 1
carrinho['creme de leite'] = 2
carrinho['refrigerante'] = 2

precosProdutos = {
    'batata palha': 6.50,
    'arroz': 18.99,
    'creme de leite': 4.50,
    'refrigerante': 6.50
}

totalCarrinho = sum(carrinho[produto] * precosProdutos[produto] for produto in carrinho)

print(f'O total do carrinho de compras é R$ {totalCarrinho:.2f}')