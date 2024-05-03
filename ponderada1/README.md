# API de Lista de Tarefas

Uma API RESTful simples para gerenciamento de tarefas, construída com Flask e Flask-RESTful. Permite criar, listar, atualizar e deletar tarefas. Implementa autenticação básica HTTP para todas as operações.

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

A aplicação estará acessível em `http://localhost:5000/docs` (servidor em flask). Também em `http://localhost:8000/docs` (servidor em fastapi)

![image](https://github.com/VZeferino/M10/assets/99190423/e3b932c3-dc33-41b5-bedd-d5e7e10cfe85)

### Teste de que a roda está funcionando

![image](https://github.com/VZeferino/M10/assets/99190423/47bdbdbd-7257-4616-86f0-dffe906869ed)


### Documentação da API

A documentação completa da API, incluindo todos os endpoints disponíveis, está acessível via Swagger UI em `http://localhost:5000/docs`.
![image](https://github.com/VZeferino/M10/assets/99190423/2c5abd46-ffda-4e22-b6d5-bd00bd9ae0eb)

Também há uma collection feita em uma extensão do github "Thunder Client" para maior organização e facilidade.
![image](https://github.com/VZeferino/M10/assets/99190423/84e94b4b-dcd3-4ad7-9ae4-5997a6b024c3)

## Comparação Flask x FastAPI

Flask é ideal para projetos menores ou quando a simplicidade é prioritária, já que é fácil de aprender e implementar. Por outro lado, FastAPI é mais adequado para ambientes modernos onde o desempenho e a eficiência são essenciais, por ser uma solução assíncrona que melhora significativamente o manejo de requisições simultâneas. 

A escolha entre Flask e FastAPI depende principalmente das necessidades do projeto e da capacidade de lidar com concorrência.

O arquivo do servidor em Fastapi é chamado "newapi".
