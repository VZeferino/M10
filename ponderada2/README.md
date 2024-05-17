# API de Gerenciamento de Tarefas

Uma API RESTful para gerenciamento de tarefas, construída com Flask. Esta API permite listar, adicionar, editar e remover tarefas com autenticação básica HTTP.

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

Após executar, a API estará acessível via http://localhost:5000/.

## App Mobile em Flutter
A aplicação móvel em Flutter permite interagir com a API para adicionar, editar e excluir tarefas. Para rodar a aplicação no Android, conecte seu dispositivo ao computador ou utilize um simulador.

## Demonstração
Um vídeo demonstrativo das funcionalidades da aplicação foi produzido. Para acessar clique [aqui](https://youtu.be/jmXzh1bQZ2o?si=nbF49r2hd2HdNqwV)

## Documentação
A documentação completa da API está disponível via Swagger UI em http://localhost:5000/docs, onde você pode testar todas as operações diretamente.

## Desenvolvimento
Este projeto foi desenvolvido considerando a eficiência e praticidade para gestão de tarefas simples. A escolha entre uma arquitetura de microserviços ou monolítica e entre sincronia ou assincronia deve ser baseada nas necessidades específicas de uso. Eu escolhi a que eu escolhi por ser mais simples :) 

