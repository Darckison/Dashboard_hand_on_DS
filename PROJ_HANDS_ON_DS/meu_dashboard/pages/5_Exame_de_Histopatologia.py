import streamlit as st
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
###############################################################################################################################  
# Configurando a página para ocupar toda a largura da tela
st.set_page_config(page_title="Dashboard de Tuberculose", layout="wide")


#############################################################################################################

# 🔹 CSS para Imagem de Fundo e Opacidade Ajustável
st.markdown(
    """
    <style>
        /* Faz o fundo ocupar toda a tela */
        [data-testid="stAppViewContainer"] {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh; /* Garante que ocupa toda a tela */
            background: url("https://remsoft.com.br/wp-content/uploads/2024/05/2019-05-22-post-tecnologia-e-saude-blog.png") no-repeat center center fixed;
            background-size: cover;
        }

        /* Overlay para ajustar a opacidade */
        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8); /* Ajuste para controlar a opacidade */
            z-index: -1;
        }

        /* Ajusta o container principal para ocupar toda a tela */
        .main .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100vw !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


################## Carregando o dataset ######################################
dados_tuberculose = pd.read_csv('meu_dashboard\pages\dados_tuberculose_HANDS_DS.csv')



############################################################################################################################################

# Título do Dashboard
# Layout da página
st.markdown(
    "<h3 style='color: #00FFFF;'>OUTROS DADOS RELACIONADOS AO CASO DE TUBERCULOSE</h3>", 
    unsafe_allow_html=True
)
# Dados para o gráfico de roda
# Contagem das condições médicas
col1, col2 = st.columns(2)

with col1:
    # 🔹 Remover valores indesejados ("Não Realizado", "Em Andamento", etc.)
    dados_tuberculose = dados_tuberculose[
        (dados_tuberculose["Histopatologia"].notna()) & 
        (dados_tuberculose["Histopatologia"] != "Não realizado") 
    ]

# 🔹 Contagem dos exames de histopatologia
    histopatologia_counts = dados_tuberculose['Histopatologia'].value_counts()
    histopatologia_types = histopatologia_counts.index.tolist()
    counts = histopatologia_counts.values.tolist()

# Cores personalizadas (ajuste conforme necessário)
    colors = ['#00FFFF', '#00FF00', '#D0FA58', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#00FF00']

# Criando o gráfico
    fig = go.Figure(data=[go.Bar(
        x=histopatologia_types,
        y=counts,
        marker_color=colors[:len(histopatologia_types)]
        )])

# Personalizando layout
    fig.update_layout(
        title='Exames de Histopatologia',
        xaxis_title='Condição Médica',
        yaxis_title='Contagem',
        width=800,
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        plot_bgcolor='rgba(0,0,0,0)'  # Fundo do gráfico transparente
        )

# Exibir no Streamlit
    st.plotly_chart(fig, use_container_width=True)


with col2:
    st.markdown("### 🧪 Exames de Histopatologia")
    st.write("""
    - **Este gráfico exibe a distribuição dos resultados dos exames de histopatologia**.
    - A histopatologia é um exame fundamental para confirmar o diagnóstico de tuberculose.
    - Pacientes com resultados positivos geralmente apresentam **evidências de infecção ativa**.
    - A análise dos exames ajuda na **tomada de decisões clínicas e tratamento adequado**.
    """)
