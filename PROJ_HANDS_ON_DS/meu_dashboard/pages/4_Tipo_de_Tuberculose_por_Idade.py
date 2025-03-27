import streamlit as st
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np



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

################## Carregando o dataset ##########################################################################################
dados_tuberculose = pd.read_csv('meu_dashboard\pages\dados_tuberculose_HANDS_DS.csv')

# Removendo duplicatas
dados_tuberculose = dados_tuberculose.drop_duplicates()
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





###############################################################################################################

# Gráfico de Boxplot de Idade por Forma
col1, col2 = st.columns(2)

with col1:
 
    bins = [0, 14, 24, 34, 44, 54, 64, 100]  # Faixas etárias
    labels = ['0-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65+']
    dados_tuberculose['faixa_etaria'] = pd.cut(dados_tuberculose['NU_IDADE_N'], bins=bins, labels=labels, right=True)

     # Agrupar os dados por faixa etária e forma de tuberculose
    dados_agrupados = dados_tuberculose.groupby(['faixa_etaria', 'tipos_de_tuberculose']).size().reset_index(name='NUMERO_CASOS')

    cor_map = {
        'Pulmonar': '#7FFFD4',  # Verde Claro
        'Extrapulmonar': '#FFD700',  # Verde Escuro
        'Pulmonar+Extrapulmonar': '#7CFC00',
            }


     # Criar o gráfico de barras
    fig3 = px.bar(dados_agrupados,
         x='faixa_etaria',
         y='NUMERO_CASOS',
         color='tipos_de_tuberculose',
         barmode='stack',  # Empilhar as barras para cada faixa etária
         title='Distribuição da Idade por Forma de Tuberculose',
         labels={'faixa_etaria': 'Faixa Etária', 'NUMERO_CASOS': 'Número de Casos', 'tipos_de_tuberculose': 'Tipo de Tuberculose'},
         color_discrete_map=cor_map
        
    )
    
    fig3.update_layout(
    xaxis_title='Faixa Etária',
    yaxis_title='Número de Casos',
    width=800,
    height=500,
    showlegend=True,  # Exibir legenda
    paper_bgcolor='rgba(0,0,0,0)',  # Remove fundo externo
    plot_bgcolor='rgba(0,0,0,0)',   # Remove fundo interno
    font=dict(color="white")  # Deixa o texto branco para melhor visibilidade
    )
    
    st.plotly_chart(fig3)


# DESCRIÇÃO DO GRÁFICO
with col2:
    st.markdown("""
        <div style="margin-top: 70px;">
        <h3> Distribuição da Idade por Forma de Tuberculose</h3>
        <ul>
            <li> Este gráfico representa a distribuição de casos de tuberculose por faixa etária.</li>
            <li>📊 <b>As barras empilhadas indicam os diferentes tipos de tuberculose.</li>
            <li>🔴 <b>Pulmonar + Extrapulmonar</b>: Representado em vermelho.</li>
            <li>🟡 <b>Extrapulmonar</b>: Representado em amarelo.</li>
            <li>🟢 <b>Pulmonar</b>: Representado em verde.</li>    
            <li>🏥 <b>A maior incidência ocorre entre 25 e 34 anos**, sugerindo que esse grupo pode ser mais vulnerável à doença.</li>
            <li>📉<b>Casos diminuem significativamente após os 60 anos**, o que pode indicar menor exposição ou diagnóstico menos frequente.</li>
            <li>🔬 <b>A análise desses dados pode auxiliar na definição de políticas de prevenção e tratamento específicas para cada faixa etária.</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)


####################################################################################################################################
   