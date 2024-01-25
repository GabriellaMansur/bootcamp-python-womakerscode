contatos = {'Mary': 16992089895, 'Marilia': 1699858962, 'Pascal': 16992025898}

nome = input('Digite o nome do contato: ')
telefone = contatos.get(nome)

if telefone is None:
    print('Telefone não encontrado')
else:
    print(f'O telefone de {nome} é {telefone}')