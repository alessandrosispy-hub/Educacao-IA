import streamlit as st
import time

def create_header():
    """Header moderno com métricas"""
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        st.markdown("""
        <h1 style='color: #2d3748; margin-bottom: 0;'>📊 Financial Dashboard</h1>
        <p style='color: #718096; margin: 0;'>Análise inteligente em tempo real</p>
        """, unsafe_allow_html=True)
    
    with col2:
        st.metric("Documentos", st.session_state.get('doc_count', 0))
    
    with col3:
        st.metric("Consultas", st.session_state.get('query_count', 0))
    
    with col4:
        status = "🟢 Online" if st.session_state.get('llm_service') else "🔴 Offline"
        st.metric("Status", status)

def show_loading_animation(message="Processando..."):
    """Mostra animação de loading moderna"""
    with st.spinner(message):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        progress_bar.empty()