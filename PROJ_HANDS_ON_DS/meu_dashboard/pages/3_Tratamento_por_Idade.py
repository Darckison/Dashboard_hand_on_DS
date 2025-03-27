import streamlit as st
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

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

# Removendo duplicatas
dados_tuberculose = dados_tuberculose.drop_duplicates()
###############################################################

# Ajustando as datas no dataframe
dados_tuberculose['DT_NOTIFIC'] = pd.to_datetime(dados_tuberculose['DT_NOTIFIC'])
dados_tuberculose['DT_DIAG'] = pd.to_datetime(dados_tuberculose['DT_DIAG'])

###############################################################

# Ajustando as datas no dataframe
dados_tuberculose['DT_NOTIFIC'] = pd.to_datetime(dados_tuberculose['DT_NOTIFIC'])
dados_tuberculose['DT_DIAG'] = pd.to_datetime(dados_tuberculose['DT_DIAG'])

##################################################################################################################################
# Calculando a idade dos pacientes no momento da notificação
dados_tuberculose['NU_IDADE_N'] = 2024 - dados_tuberculose['ANO_NASC']  # Considerando o ano de 2024 para o cálculo

# Estatísticas descritivas
dados_tuberculose['CS_SEXO'] = dados_tuberculose['CS_SEXO'].replace({'M': 'Masculino', 'F': 'Feminino'})
idade_media = dados_tuberculose['NU_IDADE_N'].mean().round(2)
genero_frequente = dados_tuberculose['CS_SEXO'].mode()[0]
tratamento_frequente = dados_tuberculose['tipos_tratamento'].mode()[0]
numero_municipios = dados_tuberculose['municipio'].nunique()

# Gráfico de Distribuição de tipos de tratamento
col1, col2 = st.columns(2)

with col1:
    fig2 = px.histogram(dados_tuberculose, x='NU_IDADE_N', color='tipos_tratamento',
                         title='Distribuição de Idade por Tipo de Tratamento',
                         labels={'NU_IDADE_N': 'Idade', 'tipos_tratamento': 'Tipo de Tratamento'},
                         color_discrete_sequence=px.colors.qualitative.Plotly)

    fig2.update_layout(
        xaxis_title='Idade',
        yaxis_title='Contagem',
        width=800,
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',  # Fundo geral transparente
        plot_bgcolor='rgba(0,0,0,0)'    
    )

    st.plotly_chart(fig2)
    
    


# Gráfico de Histograma de Idade por Tratamento
with col2:
   st.markdown("""
        <div style="margin-top: 70px;">
        <h3> Distribuição de Idade por Tipo de Tratamento</h3>
        <ul>
            <li> Este gráfico representa a distribuição de casos de tuberculose por gênero.</li>
            <li>🟦 <b>Caso novo</b>: Representado em azul.</li>
            <li>🟧 <b>Reingresso após abandono</b>: Representado em vermelho.</li>
            <li>🟩 <b>Transferência</b>: Representado em verde.</li>
            <li>🟪 <b>Reicidiva</b>: Representado em roxo.</li>
            <li> A análise ajuda a identificar padrões e impactos da tuberculose entre gêneros.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)