import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

class Config:
    """Configurações da aplicação"""
    
    # API Keys
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    
    # Model Settings - NOMES CORRETOS
    GEMINI_MODELS = {
        "gemini-2.0-flash": "Gemini 2.0 Flash",
        "gemini-1.5-pro": "Gemini 1.5 Pro", 
        "gemini-pro": "Gemini Pro"
    }
    
    GROQ_MODELS = {
        "llama2-70b-4096": "Llama 2 70B",
        "mixtral-8x7b-32768": "Mixtral 8x7B"
    }
    
    # App Settings
    MAX_RESPONSE_LENGTH = 1500
    TEMPERATURE = 0.1
    
    @classmethod
    def validate_api_keys(cls):
        """Valida se as API keys estão configuradas"""
        if not cls.GOOGLE_API_KEY:
            return False, "GOOGLE_API_KEY não encontrada no arquivo .env"
        return True, "API keys configuradas corretamente"