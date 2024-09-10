# Usar uma imagem base Python
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos necessários
COPY . /app

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta usada pela API Flask
EXPOSE 5001

# Comando para rodar a aplicação
CMD ["python", "run_cleaner.py"]
