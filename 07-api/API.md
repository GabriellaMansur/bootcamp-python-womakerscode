# API's
## Introdução aos protocolos web
* Protocolos da internet são um conjunto de regras que definem como as coisas devem acontecer na rede. Eles permitem a comunicação entre dispositivos
* **HTTP**(*HyperText Transfer Protocol*): projetado par enviar conteúdos pela internet. Quando você digita um URL no seu navegador, ele envia uma solicitação HTTP para o servidor web, que responde com a página desejada. Funciona como um “idioma” que permite que navegadores e servidores se comuniquem para exibir páginas, imagens e outros recursos na web.
* **Proxy**: é um servidor intermediário que atua como uma ponte entre o seu dispositivo e o servidor da web desejado. Eles são responsáveis por ajudar a operar as camadas de comunicação entre o pedido e a resposta dessa pedido.Algumas das suas funções saõ: intermediação de solicitações e respostas, mascaramento de IP, armazenamento em cache, filtragem de conteúdo, controles de acesso
* **HTTPS**(*HyperText Transfer Protocol Secure*): é uma extnsãp do HTTP que adiciona uma camada de segurança na nossa comunicação. Ele utiliza Transport Layer Security (TLS) ou, anteriormente, Secure Sockets Layer (SSL) para criptografar a comunicação entre um cliente e um servidor. Tem como objetivo principalautenticar o site acessado e proteger a privacidade e integridade dos dados trocados durante a transmissão
### Métodos de requisição HTTP
* `GET`: faz uma consulta a um registro ou uma coleção de resgistros do servidor
* `POST`: envia dados para crira um "novo registro" no servidor (banco de dados)
* `PUT`: envia dados para atualizar um registo existente no servidor
* `DELETE`: excluir registros do servidor
* `PATCH`: envia dados para atualizar parcialmnete em um resgistro existente no servidor
* `CONNECT`: é usado para abrir uma conexão com o servidor remoto.É usado em cenários como conexões seguras (por exemplo, HTTPS).
* `OPTIONS`: descreve as opções de comunicação para um recurso específico. Permite uq eo cliente descubra quais métodos de requisição que o servidor suporta
* `TRACE`: foi projetado para fins de diagnóstico durante o desenvolvimento.Executa um teste de chamada loop-back junto com o caminho para o recurso de destino.
* `HEAD`: É útil quando você só precisa das informações do cabeçalho (como tamanho do arquivo) sem baixar todo o conteúdo.

## O que são API's?
* São interfaces que permitem a comunicação e a integração entre diferentes aplicações de softwares demnaira padronizada, sem que um sistema precise conhecer detalhes internos de implementação do outro
* Tipos de API's (arquiteturas)
    * REST: mais leve, pode ser armazenado em cache e mais fácil de atualizar
    * SOAP: sobrecraga extra, mais largura de banda, mais trabalho em ambas as extremidades.

## Flask
* Micro framwork de Python
* Criar um ambiente virtual `py -3 -m venv .venv`
* Ativar `.\.venv\Scripts\activate`
* Instalar o Flask `pip install Flask` 
* Para executar `flask --app [nome_arquivo] run`
* Estrutura básica
    * ```python
        from flask import Flask

        app = Flask(__name__)

        @app.route('/')
        def hello_world():
            return 'Olá'
    ```

## FastAPI
* Configuração do ambiente virtual `py -3 -m venv .venv`
* Instalar o FastAPI `pip install "fastapi[all]`
* Inicialização do servidor `uvicorn app:app --reaload`
* Suas características são:
    * Facilidade de uso
    * Escalabiliade
    * Desempenho com recursos assíncronos

* Exemplos simples:
```python
from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def root():
    return {"message": "Olá"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, busca: Union[str, int] = None):
    return {"item_id":item_id, "busca": busca}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
```