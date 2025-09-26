import streamlit as st
from frontend.components.header import create_header  # ✅ CORRIGIDO

def create_main_layout():
    """Layout principal moderno com abas"""
    
    # Header
    st.markdown("""
    <div class='fade-in'>
    """, unsafe_allow_html=True)
    
    create_header()  # ✅ Agora está importado corretamente
    
    # Abas principais
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Dashboard", "🤖 Análise IA", "📊 Dados", "⚙️ Configurações"])
    
    with tab1:
        create_dashboard_tab()
    
    with tab2:
        create_analysis_tab()
    
    with tab3:
        create_data_tab()
    
    with tab4:
        create_settings_tab()

def create_dashboard_tab():
    """Tab de dashboard com métricas"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.metric("Receita Total", "R$ 1.2M", "+12%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.metric("Lucro Líquido", "R$ 350K", "+8%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
        st.metric("Despesas", "R$ 850K", "-5%")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Gráficos - Com fallback
    try:
        from frontend.components import charts
        charts.create_financial_charts()
    except ImportError:
        st.info("📊 Módulo de gráficos não disponível")

def create_analysis_tab():
    """Tab de análise com IA"""
    st.markdown("### 💬 Análise Inteligente")
    
    # Container de chat moderno
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            query = st.text_input(
                "💡 Pergunte sobre seus dados financeiros:",
                placeholder="Ex: Qual foi o lucro no último trimestre?",
                key="analysis_query"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            analyze_btn = st.button("🚀 Analisar", use_container_width=True)
        
        if analyze_btn and query:
            with st.spinner("🤖 Analisando..."):
                # Função simplificada por enquanto
                result = "Análise em desenvolvimento"
                st.success(result)

def create_data_tab():
    """Tab de visualização de dados"""
    if st.session_state.get('dataframe') is not None:
        st.dataframe(
            st.session_state.dataframe,
            use_container_width=True,
            height=400
        )
    else:
        st.info("📁 Faça upload de um arquivo para visualizar os dados")

def create_settings_tab():
    """Tab de configurações avançadas"""
    st.markdown("### ⚙️ Configurações Avançadas")
    
    with st.expander("Configurações de IA"):
        st.slider("Temperatura", 0.0, 1.0, 0.1, key="temperature")
        st.number_input("Máximo de tokens", 100, 4000, 1500, key="max_tokens")
    
    with st.expander("Configurações de Visualização"):
        st.selectbox("Tema", ["Claro", "Escuro", "Automático"], key="theme")
        st.checkbox("Mostrar logs técnicos", key="show_logs")