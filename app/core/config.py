from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Configuración centralizada de la aplicación.
    Valida las variables de entorno al inicio.
    """
    PROJECT_NAME: str = "Smart Lead Enrichment Agent"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Claves de API (Requeridas)
    OPENAI_API_KEY: str
    
    # Configuración del Scraper
    HEADLESS_MODE: bool = True
    MAX_CONCURRENT_TASKS: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )


# Instancia global de configuración
settings = Settings()

