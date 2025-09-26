import streamlit as st
import asyncio
import sys
import os

# Configurar path
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

from frontend.layouts.main import create_main_layout
from frontend.components.sidebar import create_sidebar
from frontend.styles.themes import apply_custom_theme
from backend.services.llm_service import LLMService
from backend.services.document_service import DocumentService

def main():
    # Configuração da página com tema moderno
    st.set_page_config(
        page_title="🤖 Financial AI Assistant",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Aplicar tema customizado
    apply_custom_theme()
    
    # Inicializar serviços
    if 'llm_service' not in st.session_state:
        st.session_state.llm_service = LLMService()
    
    if 'document_service' not in st.session_state:
        st.session_state.document_service = DocumentService()
    
    # Criar layout
    create_sidebar()
    create_main_layout()

if __name__ == "__main__":
    main()