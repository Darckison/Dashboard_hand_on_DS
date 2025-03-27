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



##############################################################################################################################
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


##############################################################################################################################S

# Caminho da logo (use um caminho local ou URL)
logo_url = "meu_dashboard\Brasão_UFRR_negativo.png"

html_code = f"""
    <style>
        /* Container flex para alinhar logo e texto */
        .header-container {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            overflow: hidden;
            width: 100%;
        }}

        /* Animação de letreiro */
        @keyframes marquee {{
            from {{ transform: translateX(100%); }}
            to {{ transform: translateX(-100%); }}
        }}

        .scrolling-text {{
            white-space: nowrap;
            display: inline-block;
            font-size: 24px;
            font-weight: bold;
            color: #00FF00;
            padding: 10px 20px;
            border-radius: 10px; /* Bordas arredondadas */
            animation: marquee 7S Linear infinite;
            background-color: transparent;Escuro */
        }}
    </style>
        
        <!-- Letreiro Animado -->
        <div class="scrolling-text">
             DADOS DE TUBERCULOSE  DADOS DE TUBERCULOSE DADOS TUBERCULOSE
        </div>
    </div>
"""

# Renderizar no Streamlit
st.components.v1.html(html_code, height=100)
#######################################################################################





################## Carregando o dataset ######################################
dados_tuberculose = pd.read_csv('meu_dashboard\pages\dados_tuberculose_HANDS_DS.csv')

# Removendo duplicatas
dados_tuberculose = dados_tuberculose.drop_duplicates()

#####################################################################################################################

# Estilos CSS para remover margens e preencher toda a tela
st.markdown("""
    <style>
        /* Remove as margens e paddings da página */
        .main .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100%;
        }
        
        /* Remove o menu superior (opcional) */
        header {visibility: hidden;}

        /* Ajusta o fundo para tela cheia */
        body {
            overflow-x: hidden;
        }
    </style>
""", unsafe_allow_html=True) 


#####################################################################################################################


# Ajustando as datas no dataframe
dados_tuberculose['DT_NOTIFIC'] = pd.to_datetime(dados_tuberculose['DT_NOTIFIC'])
dados_tuberculose['DT_DIAG'] = pd.to_datetime(dados_tuberculose['DT_DIAG'])

# Calculando a idade dos pacientes no momento da notificação
dados_tuberculose['NU_IDADE_N'] = 2024 - dados_tuberculose['ANO_NASC']  # Considerando o ano de 2024 para o cálculo

# Estatísticas descritivas
valor_remover = ['Caso Novo']
dados_tuberculose = dados_tuberculose[~dados_tuberculose['tipos_tratamento'].isin(valor_remover)]


dados_tuberculose['CS_SEXO'] = dados_tuberculose['CS_SEXO'].replace({'M': 'Masculino', 'F': 'Feminino'})
idade_media = dados_tuberculose['NU_IDADE_N'].mean().round(2)
genero_frequente = dados_tuberculose['CS_SEXO'].mode()[0]
tratamento_frequente = dados_tuberculose['tipos_tratamento'].mode()[0]
numero_municipios = dados_tuberculose['municipio'].nunique()







#A LOGO E TÍTULO

# Caminho da logo (local)
logo_path = "meu_dashboard\pages\Brasão_UFRR_.png"

# Criar colunas para alinhar lado a lado
col1, col2 = st.columns([1, 4])  # Ajuste as proporções conforme necessário

with col1:
    st.image(logo_path, width=150)  # Ajuste o tamanho da logo

with col2:
    st.markdown("<h1 style='color: #FFFFFF;'margin: 0; padding-top: 20px;'>CASOS DE TUBERCULOSE RR DASHBOARD</h1>", unsafe_allow_html=True)


#st.subheader("ALUNO: DARCKISON ", divider=True)
st.markdown(
    """
    <div style="display: flex; gap: 8px;">
        <h3 style="color: FFFFFF; margin: 0;">DISCENTE:</h3>
        <h3 style="color: #00FFFF; margin: 0;">Darckison Almeida</h3>
    </div>
    """,
    unsafe_allow_html=True
)
# Layout da página

# Usando st.markdown para aplicar cor ao subtítulo
st.markdown("<h3 style='color: FFFFFF;'>Estatísticas Descritivas</h3><hr style='border: 1px solid #00FFFF;'>", unsafe_allow_html=True)

# Organizando as estatísticas descritivas em colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Idade Média dos Pacientes", f"{idade_media} anos")
    st.metric("Gênero Mais Frequente", genero_frequente)

with col2:
    st.metric("Tratamento Mais Frequente", tratamento_frequente)
    st.metric("Número de Municípios", numero_municipios)

# Gráficos de Análises Visuais
st.markdown("<h3 style='color: FFFFFF;'>Análise visual</h3><hr style='border: 1px solid #00FFFF;'>", unsafe_allow_html=True)
