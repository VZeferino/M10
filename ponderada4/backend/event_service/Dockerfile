# Usar uma imagem base oficial do Python
FROM python:3.8-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install -r requirements.txt

# Copiar o conteúdo do diretório atual para /app no contêiner
COPY . .

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
