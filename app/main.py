import uuid
from fastapi import FastAPI, HTTPException, Depends
from app.core.config import settings
from app.models.schemas import LeadInput, LeadResponse, EnrichedData
from app.services.llm_service import LLMService
from app.services.enrichment_service import ScraperService, EnrichmentService

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API de enriquecimiento de leads impulsada por IA y Scraping."
)

# Inyección de dependencias simple
def get_enrichment_service():
    llm = LLMService(api_key=settings.OPENAI_API_KEY)
    scraper = ScraperService()
    return EnrichmentService(llm, scraper)

@app.post(
    f"{settings.API_V1_STR}/enrich",
    response_model=LeadResponse,
    status_code=200,
    tags=["Lead Enrichment"]
)
async def enrich_lead_data(
    lead_in: LeadInput,
    service: EnrichmentService = Depends(get_enrichment_service)
):
    """
    Enriquece un lead a partir de su email.
    
    - **Busca** en la web referencias del usuario.
    - **Analiza** los resultados con GPT-4.
    - **Retorna** un perfil estructurado JSON.
    """
    try:
        # Lógica de negocio
        data = await service.enrich_lead(lead_in.email)
        
        enriched_data = EnrichedData(
            full_name=data.get("full_name"),
            job_title=data.get("job_title"),
            company_name=data.get("company_name"),
            confidence_score=data.get("confidence_score", 0.0),
            source_urls=["https://linkedin.com/in/example"]
        )
        
        return LeadResponse(
            id=str(uuid.uuid4()),
            input_data=lead_in,
            enriched_data=enriched_data
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando lead: {str(e)}")

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok", "version": settings.VERSION}

