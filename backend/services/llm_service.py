import os
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.llms.groq import Groq
from core.config.settings import Config

class LLMService:
    """Serviço para gerenciamento de modelos de IA"""
    
    def __init__(self):
        # Verificar se a API key está configurada
        if not Config.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY não encontrada. Configure no arquivo .env")
        
        # Modelos CORRETOS do Gemini
        self.available_models = {
            "🤖 Gemini 2.0 Flash": GoogleGenAI(
                model="gemini-2.0-flash",
                api_key=Config.GOOGLE_API_KEY
            ),
            "🤖 Gemini 1.5 Pro": GoogleGenAI(
                model="gemini-1.5-pro",
                api_key=Config.GOOGLE_API_KEY
            ),
            "🚀 Groq Llama": Groq(
                model="llama2-70b-4096",
                api_key=Config.GROQ_API_KEY
            ) if Config.GROQ_API_KEY else None
        }
        
        # Remover modelos não disponíveis
        self.available_models = {k: v for k, v in self.available_models.items() if v is not None}
        
        if not self.available_models:
            raise ValueError("Nenhum modelo disponível. Configure as API keys no arquivo .env")
        
        self.current_model = list(self.available_models.keys())[0]
    
    def get_available_models(self):
        """Retorna lista de modelos disponíveis"""
        return list(self.available_models.keys())
    
    def set_current_model(self, model_name):
        """Define o modelo atual"""
        if model_name in self.available_models:
            self.current_model = model_name
        else:
            raise ValueError(f"Modelo não disponível: {model_name}")
    
    def generate_response(self, prompt, max_length=1500):
        """Gera resposta usando o modelo atual"""
        try:
            model = self.available_models[self.current_model]
            response = model.complete(prompt)
            return response.text[:max_length]
        except Exception as e:
            return f"❌ Erro ao gerar resposta: {str(e)}"