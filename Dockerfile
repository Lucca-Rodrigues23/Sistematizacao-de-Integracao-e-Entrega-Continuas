# Stage 1: Build / Dependências
FROM python:3.11-slim AS builder

WORKDIR /app

COPY . .

# Stage 2: Imagem final leve
FROM python:3.11-slim AS runner

WORKDIR /app

COPY --from=builder /app /app

ENV PORT=8000
EXPOSE 8000

CMD ["python", "conversor_temperatura.py"]
