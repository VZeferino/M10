# Projeto de Sistema de Gerenciamento de Tarefas com Gateway e Logging

Este projeto é uma API RESTful para gerenciamento de tarefas, construída com Flask, que inclui um gateway e um sistema de logging. Ele permite listar, adicionar, editar e remover tarefas, além de gerenciar usuários e eventos. O sistema utiliza múltiplos serviços e Docker Compose para facilitar a configuração e execução.

## Começando

Estas instruções fornecerão uma cópia do projeto rodando em sua máquina local para desenvolvimento e teste.

### Pré-requisitos

Para executar este projeto, você precisará do seguinte:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Executando a aplicação

Para iniciar o ambiente utilizando Docker Compose, execute:

```bash
docker compose up
```

Após executar, os serviços estarão acessíveis nas seguintes URLs:

- Login Service: http://localhost:5000/
- Image Service: http://localhost:5001/
- Event Service: http://localhost:5002/
- Gateway Service: http://localhost:5003/

## Serviços Disponíveis

### Serviço de Login (Login Service)
Este serviço gerencia a autenticação de usuários e utiliza Flask com autenticação básica HTTP.

### Serviço de Imagem (Image Service)
Serviço responsável por gerenciar operações relacionadas a imagens.

### Serviço de Eventos (Event Service)
Este serviço gerencia a criação, leitura, atualização e exclusão (CRUD) de eventos. Ele é um exemplo de novo serviço adicionado ao sistema.

### Gateway Service
O gateway atua como um ponto de entrada para o sistema, encaminhando as solicitações para os serviços apropriados.


## Desenvolvimento
Este projeto foi desenvolvido com foco na modularidade e escalabilidade, utilizando uma arquitetura de microserviços. Cada serviço é independente e pode ser escalado ou modificado sem impactar os outros serviços. O uso de Docker e Docker Compose facilita o desenvolvimento, teste e implantação do sistema.

