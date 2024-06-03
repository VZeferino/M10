# Aplicação de Upload de Imagens com Flutter
Uma aplicação móvel em Flutter para upload de imagens com processamento de filtros, utilizando backend em microserviços. Esta aplicação permite que usuários se registrem, façam login, e processem imagens com um filtro preto e branco. Após o processamento, o usuário recebe uma notificação e a imagem processada é exibida na tela.

## Começando
Estas instruções fornecerão uma cópia do projeto rodando em sua máquina local para desenvolvimento e teste.

## Pré-requisitos
Para executar este projeto, você precisará do seguinte:

Docker
Docker Compose
Flutter


Agora, o backend é dividido em dois microserviços:

Login Service: Responsável pela autenticação e registro de usuários.
Image Processing Service: Responsável pelo processamento de imagens.


## Configuração do Backend
Clone o repositório para sua máquina local.
Navegue até o diretório do projeto.
Executando os Microserviços com Docker Compose dentro da pasta backend.

Para iniciar o ambiente utilizando Docker Compose, execute:

```
docker compose up
```

Após executar, os serviços estarão acessíveis via:

Login Service: http://localhost:5000/
Image Processing Service: http://localhost:5001/

## App Mobile em Flutter
A aplicação móvel em Flutter permite interagir com os serviços para registro, login e processamento de imagens.

## Executando o App Flutter
Certifique-se de ter o Flutter instalado em sua máquina.
Conecte seu dispositivo Android ao computador ou utilize um emulador.

No diretório do projeto Flutter, execute:

```
flutter pub get
flutter run
```

### Funcionalidades
Tela de Login: Permite que o usuário faça login com e-mail e senha. Também há uma opção para registro de novos usuários.
Tela Inicial: Após o login, o usuário é levado para a tela inicial onde pode acessar a tela de processamento de imagem.
Tela de Processamento de Imagem: O usuário seleciona uma imagem da galeria, envia para o backend, e a imagem é processada com um filtro preto e branco.
Notificação: Após o processamento da imagem, o usuário recebe uma notificação informando que a imagem foi processada com sucesso e ela é exibida na tela.

## Demonstração
Um vídeo demonstrativo das funcionalidades da aplicação foi produzido. Para acessar [clique aqui](https://drive.google.com/file/d/1UWcIQCX6PvDsi4fTxH3IdSZrM9Wcwjb3/view?usp=sharing)

## Desenvolvimento
Este projeto foi desenvolvido considerando a eficiência e praticidade para gestão de imagens simples. A arquitetura de microserviços foi escolhida para facilitar a escalabilidade, manutenção e também porque o professor Murilo obrigou. Caso contrário eu perderia nota.
