print('BEM VINDO AO PROGRAMA')
usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario == 'admin' and senha == 'admin123':
    print('Acesso permitido')
else:
    print('Acesso negado. Tente novamente')
