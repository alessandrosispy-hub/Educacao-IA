import streamlit as st
import os
from core.config.settings import Config

def create_sidebar():
    """Sidebar moderna com upload e configurações"""
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; margin-bottom: 30px;'>
            <h1 style='color: #667eea; margin-bottom: 5px;'>🤖</h1>
            <h3 style='color: #2d3748; margin: 0;'>Financial AI</h3>
            <p style='color: #718096; font-size: 12px;'>Assistente Inteligente</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Verificar API keys
        is_valid, message = Config.validate_api_keys()
        if not is_valid:
            st.error(f"⚠️ {message}")
            st.info("""
            **Configure no arquivo .env:**
            ```
            GOOGLE_API_KEY=sua_chave_aqui
            # GROQ_API_KEY=sua_chave_groq (opcional)
            ```
            """)
            return None, None, None, None, None
        
        # Upload section
        st.markdown("### 📤 Upload de Documentos")
        uploaded_file = st.file_uploader(
            "Arraste ou selecione arquivos",
            type=["pdf", "csv", "xlsx"],
            help="Suporta PDF, CSV e Excel",
            key="file_uploader"
        )
        
        # Configurações de modelo - APENAS MODELOS DISPONÍVEIS
        st.markdown("### ⚙️ Configurações")
        
        # Modelos disponíveis baseados nas API keys configuradas
        available_models = ["🤖 Gemini 2.0 Flash", "🤖 Gemini 1.5 Pro"]
        if Config.GROQ_API_KEY:
            available_models.append("🚀 Groq Llama")
            
        model_choice = st.selectbox(
            "Modelo de IA",
            available_models,
            index=0
        )
        
        # Configurações de resposta
        max_length = st.slider("Tamanho máximo da resposta", 500, 3000, 1500)
        concise_mode = st.checkbox("Modo resumido", value=True)
        auto_translate = st.checkbox("Traduzir automaticamente", value=True)
        
        # Status do sistema
        st.markdown("### 📊 Status do Sistema")
        api_status = "✅ Conectado" if is_valid else "❌ Offline"
        st.metric("API Status", api_status)
        
        # Quick actions
        st.markdown("### ⚡ Ações Rápidas")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Limpar", use_container_width=True):
                st.session_state.clear()
                st.rerun()
        
        return uploaded_file, model_choice, max_length, concise_mode, auto_translate