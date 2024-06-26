# Prova prática

Uma API RESTful simples para gerenciamento de blog, construída com FASTAPI. Permite criar, listar, atualizar e deletar posts no blog.

## Começando

Estas instruções irão te ajudar a configurar uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

Antes de iniciar, você precisará ter instalado em sua máquina as seguintes ferramentas:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

Isso é necessário para criar o ambiente de contêineres e rodar a aplicação utilizando o Docker Compose.

### Executando a aplicação

Para iniciar o container, execute:

```
docker compose up 
```

A aplicação estará acessível em `http://localhost:8000`

![image](https://github.com/VZeferino/M10/assets/99190423/4396ec01-8ffd-4ec2-961c-be9a72d56c71)

### Teste de que a roda está funcionando

##### FASTAPI
![image](https://github.com/VZeferino/M10/assets/99190423/ad8359e6-b051-4850-a7cc-afffc8ef5964)

### Sistema de logs

Foi criado além do config dentro do arquivo 
logging.basicConfig(
    filename='informations_blog.log',
    level=logging.WARNING, 
    format='%(asctime)s:%(levelname)s:%(message)s'
)

Não identifiquei o erro mas não estava salvando na raiz do projeto.

![image](https://github.com/VZeferino/M10/assets/99190423/f6e8457d-ea94-497e-9b53-7e05aa8483b7)

### Testes de rota

No projeto também há o arquivo collection.json para importar as requisições que eu fiz no thunderclient e testá-las.
