
import streamlit as st
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


################## Carregando o dataset ######################################
dados_tuberculose = pd.read_csv('meu_dashboard\pages\dados_tuberculose_HANDS_DS.csv')


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

# Removendo duplicatas
dados_tuberculose = dados_tuberculose.drop_duplicates()



# Criar colunas para alinhar o gráfico e o texto lado a lado
col1, col2 = st.columns([2, 1])  # Ajuste os tamanhos conforme necessário

with col1:
    # Contagem de gênero
    gender_counts = dados_tuberculose['CS_SEXO'].value_counts()
    labels = ['Masculino', 'Feminino']
    values = gender_counts.tolist()

    # Criando o gráfico de pizza (roda) com Plotly
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.3,
        hoverinfo='label+percent',
        marker=dict(colors=['#0000FF', '#E0FFFF'])
    )])

    # Personalizando a aparência do gráfico
    fig.update_layout(
    title="Distribuição por Gênero",  # Corrigido o título
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',  # Corrigido a vírgula no final
    plot_bgcolor='rgba(0,0,0,0)',  # Corrigido o erro do ponto
    width=600,  # Largura maior
    height=600,  # Altura maior
    #margin=dict(l=20, r=20, t=20, b=20)  # Corrigida a indentação e espaços
)

    # Exibir o gráfico
    st.plotly_chart(fig)

with col2:
    st.markdown("""
        <div style="margin-top: 70px;">
        <h3> Distribuição de Gênero por número de pessoas </h3>
        <ul>
            <li> Este gráfico representa a distribuição de casos de tuberculose por gênero.</li>
            <li>🟦 <b>Masculino</b>: Representado em azul.</li>
            <li>⬜<b>Feminino</b>: Representado em azul-claro.</li>
            <li> A análise ajuda a identificar padrões e impactos da tuberculose entre gêneros.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)
