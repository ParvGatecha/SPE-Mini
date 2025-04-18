# Use Python base image
FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn pytest

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
