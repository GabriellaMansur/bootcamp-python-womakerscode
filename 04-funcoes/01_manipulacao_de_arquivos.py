# Manipulação de arquivos

def multiplicacao():
    mult = 10*2
    # criando arquivo 
    file = 'arquivo.txt'
    
    #abertura somente para leitura
    #arquivo_leitura = open(file, "r")

    # abertura para escrita
    arquivo_escrita = open(file, "w")
    arquivo_escrita.write(f'O resultado da multiplicacao eh: {mult}')
    arquivo_escrita.close() #fechando o arquivo

    #abertura de arquivos binários
    #arquivo_binario = open(file, "wb")


    #abertura somente para leitura
    arquivo_leitura = open(file, "r")
    leitura = arquivo_leitura.read()
    arquivo_leitura.close()
    print(leitura)
    


multiplicacao()