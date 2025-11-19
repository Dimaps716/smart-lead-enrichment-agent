from pydantic import BaseModel, EmailStr, Field, HttpUrl
from typing import Optional, List
from datetime import datetime


class SocialProfile(BaseModel):
    platform: str
    url: HttpUrl
    username: Optional[str] = None


class LeadInput(BaseModel):
    """Datos mínimos requeridos para iniciar el enriquecimiento"""
    email: EmailStr
    company_domain: Optional[str] = None


class EnrichedData(BaseModel):
    """Datos inferidos/extraídos por el Agente"""
    full_name: Optional[str] = None
    job_title: Optional[str] = None
    linkedin_url: Optional[str] = None
    company_name: Optional[str] = None
    industry: Optional[str] = None
    estimated_revenue: Optional[str] = None
    confidence_score: float = Field(..., ge=0, le=1, description="Confianza del modelo en los datos")
    source_urls: List[str] = []


class LeadResponse(BaseModel):
    """Respuesta final estructurada"""
    id: str = Field(..., description="ID único de la solicitud")
    input_data: LeadInput
    enriched_data: EnrichedData
    processed_at: datetime = Field(default_factory=datetime.now)
    status: str = "completed"

