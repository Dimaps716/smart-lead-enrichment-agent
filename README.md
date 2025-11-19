# 🕵️‍♂️ Smart Lead Enrichment Agent

> **FastAPI + Playwright + OpenAI**

Microservicio de enriquecimiento de datos B2B. Transforma un simple correo electrónico en un perfil profesional completo buscando en tiempo real en la web y estructurando la información con Inteligencia Artificial.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-Scraping-45ba4b?style=for-the-badge&logo=playwright&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-412991?style=for-the-badge&logo=openai&logoColor=white)

## 🚀 Arquitectura

El sistema sigue una arquitectura limpia de capas:

1.  **API Layer (FastAPI):** Expone endpoints RESTful documentados automáticamente.
2.  **Service Layer:**
    *   `ScraperService`: Agente autónomo de Playwright que navega y extrae DOM crudo.
    *   `LLMService`: Cliente asíncrono de OpenAI para extracción de entidades (NER).
3.  **Domain Layer (Pydantic):** Validación estricta de datos de entrada y salida.

## 🛠 Instalación

```bash
# 1. Clonar repositorio
git clone https://github.com/Dimaps716/smart-lead-enrichment-agent.git

# 2. Instalar dependencias
pip install -r requirements.txt
# O si usas poetry:
poetry install

# 3. Variables de entorno
cp .env.example .env
# Editar OPENAI_API_KEY=sk-...
```

## ⚡ Uso

```bash
uvicorn app.main:app --reload
```

### Endpoint: `POST /api/v1/enrich`

**Input:**
```json
{
  "email": "contacto@empresa.com"
}
```

**Output:**
```json
{
  "id": "550e8400-e29b...",
  "enriched_data": {
    "full_name": "Juan Pérez",
    "job_title": "CTO",
    "company": "Empresa Tech",
    "confidence_score": 0.98
  }
}
```

---
Hecho con ❤️ por [Dima](https://github.com/Dimaps716)

