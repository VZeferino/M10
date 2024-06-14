# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo de dependências e instalar as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação
COPY . .

# Informar a porta que será exposta pelo container
EXPOSE 8000

