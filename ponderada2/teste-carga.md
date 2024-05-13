# API de Lista de Tarefas - Teste de Carga

Uma API RESTful simples para gerenciamento de tarefas, construída com Flask e Flask-RESTful. Permite criar, listar, atualizar e deletar tarefas. Implementa autenticação básica HTTP para todas as operações e agora vamos testar.

## Começando

Estas instruções irão te ajudar a configurar uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste.

### Pré-requisitos

- Python 3.6 ou superior
- Flask
- Flask-RESTful
- Flask-HTTPAuth
- Flask_Swagger_ui

### Executando a aplicação

Para iniciar o servidor Flask, execute:

```
python3 app.py
```

A aplicação estará acessível em `http://localhost:5000/`.
![image](https://github.com/VZeferino/M10/assets/99190423/47bdbdbd-7257-4616-86f0-dffe906869ed)


### Testes de Carga

Realizamos um teste de carga na funcionalidade de criação de tarefas da nossa aplicação para garantir que o sistema possa lidar com um volume alto de requisições simultâneas. Este teste é crucial para verificar a estabilidade e a escalabilidade do nosso serviço em condições de uso intenso.

#### Detalhes

- Endpoint Testado: /tasks
- Método: POST
- Carga de Teste: 100 requisições
- Dados Enviados: Cada requisição enviou um JSON para criação de uma nova tarefa.
- Autenticação: Cada requisição incluiu cabeçalhos de autenticação com usuário e senha válidos.

O teste foi conduzido utilizando jmeter que permite simular e monitorar a resposta do servidor.

#### Resultados

Os resultados do teste de carga indicam como o sistema se comporta sob estresse. Os dados detalhados do teste estão disponíveis no arquivo summary.csv, incluído no diretório do projeto dentro da pasta static. Este relatório inclui tempos de resposta, taxa de erro das requisições, e outras métricas relevantes.

Para visualizar, você pode clicar [aqui](https://github.com/VZeferino/M10/blob/main/ponderada2/static/summary.csv)
