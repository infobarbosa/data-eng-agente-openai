# Use uma imagem base do Python
FROM python:3.9-slim

# Define diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia apenas o arquivo de requisitos primeiro (para fazer cache das dependências)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo do projeto para dentro do contêiner
COPY app.py .

# Exposição da porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar o aplicativo no contêiner
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
