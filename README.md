# Sistematização de Integração e Entrega Contínuas (CI/CD)

Este projeto implementa uma esteira automatizada de CI/CD para uma aplicação Python de **Conversor de Temperatura** (Celsius, Fahrenheit e Kelvin), utilizando **GitHub Actions**, **Docker (Build Multi-Stage)** e publicação no **GitHub Container Registry (GHCR)**.

---

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.11
- **Testes & Cobertura:** `pytest` e `pytest-cov`
- **Containerização:** Docker (Build Multi-Stage)
- **CI/CD:** GitHub Actions
- **Registro de Contêineres:** GHCR (GitHub Container Registry)

---

## ⚙️ Esteira de CI/CD (GitHub Actions)

A esteira automatizada está configurada no arquivo `.github/workflows/esteira.yml` e executa as seguintes etapas:

1. **Testes Automatizados & Cobertura Mínima (>= 70%):**
   - Roda a suíte de testes unitários.
   - Valida se a cobertura de código atinge a meta exigida.

2. **Build e Push do Docker para o GHCR:**
   - Realiza o build *multi-stage* utilizando a imagem `python:3.11-slim`.
   - Formata a tag para minúsculas conforme as exigências do GHCR.
   - Publica automaticamente a imagem no registro de pacotes do GitHub no merge com a branch `main`.

---

## 📦 Como Executar o Container via GHCR

Caso possua o Docker instalado, você pode rodar a imagem oficial publicada na nuvem diretamente pelo terminal:

```bash
# 1. Baixar a imagem do GitHub Container Registry
docker pull ghcr.io/lucca-rodrigues23/sistematizacao-de-integracao-e-entrega-continuas:latest

# 2. Executar a aplicação de forma interativa
docker run -it ghcr.io/lucca-rodrigues23/sistematizacao-de-integracao-e-entrega-continuas:latest
