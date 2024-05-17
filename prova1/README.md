# API de Pedidos

Uma API RESTful simples para gerenciamento de pedidos, construída com Flask e Flask-RESTful. Permite criar, listar, atualizar e deletar pedidos.

## Começando

Estas instruções irão te ajudar a configurar uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

Antes de iniciar, você precisará ter instalado em sua máquina as seguintes ferramentas:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

Isso é necessário para criar o ambiente de contêineres e rodar a aplicação utilizando o Docker Compose.

## Clonar repositório

Entre na pasta em que deseja copiar este repositório e no terminal rode:

```
git clone https://github.com/VZeferino/M10.git
```

Após isso navegue até a pasta "prova1"

### Executando a aplicação

Para iniciar o container, execute:

```
docker compose up 
```

Dessa forma será instalado as dependencias do arquivo requirements.txt, e irá rodar a aplicação em um container na porta 5000.

### Colection
As rotas estão em uma collection para facilitar as funcionalidades da aplicação, dentro da pasta static.

### Teste de que a rota está funcionando
![image](https://github.com/VZeferino/M10/assets/99190423/6257d8ce-8eb8-4221-a6ab-86f334766197)

É possível criar novos pedidos como acima.

![image](https://github.com/VZeferino/M10/assets/99190423/10fe6488-5073-4900-8c78-908127a8f634)

Também visualizar todos os pedidos

![image](https://github.com/VZeferino/M10/assets/99190423/b3f3a0a4-ff5e-422e-8e36-39a68c47039f)

Editar um pedido

![image](https://github.com/VZeferino/M10/assets/99190423/b7e7eda3-6fa8-4822-9b57-df858a72e79e)

Deletar um pedido

![image](https://github.com/VZeferino/M10/assets/99190423/d34f8367-3ff3-45fd-927c-3280f5a2066c)

E por fim, visualizar um pedido específio (nesse caso, o que foi excluido acima)


