# Usando a imagem oficial do Python
FROM python:3.10-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Instalar pacotes necessários para compilar o mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential pkg-config

# Copiando o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação
COPY . .

# Definindo a variável de ambiente FLASK_APP
ENV FLASK_APP=app.py

# Expondo a porta que a aplicação vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]

