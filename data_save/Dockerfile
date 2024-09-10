# Usar uma imagem base Python
FROM python:3.9-slim

# Definir o diret�rio de trabalho no container
WORKDIR /app

# Copiar os arquivos necess�rios
COPY . /app

# Instalar as depend�ncias
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta usada pela API Flask
EXPOSE 5002

# Comando para rodar a aplica��o
CMD ["python", "run_database.py"]
