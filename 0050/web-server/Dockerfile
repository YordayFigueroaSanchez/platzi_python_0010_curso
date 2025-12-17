FROM python:3.10

WORKDIR /app

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Copiar archivos de dependencias
COPY requirements.txt /app/requirements.txt

# Instalar dependencias con uv
RUN uv pip install --system --no-cache -r requirements.txt

# Copiar el resto de la aplicación
COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]