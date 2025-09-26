import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_financial_charts():
    """Cria gráficos financeiros modernos"""
    
    # Dados de exemplo (substituir por dados reais)
    sample_data = pd.DataFrame({
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'Receita': [120000, 150000, 130000, 170000, 160000, 180000],
        'Despesas': [80000, 85000, 90000, 95000, 88000, 92000],
        'Lucro': [40000, 65000, 40000, 75000, 72000, 88000]
    })
    
    # Gráfico de linhas
    fig_line = px.line(
        sample_data, 
        x='Mês', 
        y=['Receita', 'Despesas', 'Lucro'],
        title='📈 Performance Financeira Mensal',
        template='plotly_white'
    )
    
    fig_line.update_layout(
        hovermode='x unified',
        showlegend=True,
        height=400
    )
    
    st.plotly_chart(fig_line, use_container_width=True)
    
    # Gráfico de barras
    col1, col2 = st.columns(2)
    
    with col1:
        fig_bar = px.bar(
            sample_data,
            x='Mês',
            y='Lucro',
            title='💰 Lucro Mensal',
            color='Lucro',
            color_continuous_scale='Viridis'
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        fig_pie = px.pie(
            values=sample_data['Receita'],
            names=sample_data['Mês'],
            title='🍰 Distribuição de Receitas'
        )
        st.plotly_chart(fig_pie, use_container_width=True)