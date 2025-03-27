import streamlit as st
import os

# 🔹 Configuração da página (Deve ser a primeira linha)
st.set_page_config(page_title="Dashboard de Tuberculose", layout="wide")


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


# 🔹 Cabeçalho com Imagem da Logo e Título
logo_path = "meu_dashboard\logo data.jpeg"

col1, col2 = st.columns([1, 5])  # Criar colunas para alinhar logo e título

with col1:
    st.image(logo_path, width=100)  # Ajuste o tamanho da imagem

with col2:
    st.title("📊 Dashboard de Tuberculose")
    st.write("Explore os gráficos e insights sobre os casos de tuberculose.")

st.divider()


col1, =st.columns([5])

with col1:
    st.markdown("<h4 style='color: FFFFFF;'>Os gráficos exibem informações essenciais para acompanhar tendências e padrões da doença, auxiliando no melhor entendimento. A interface foi projetada para ser clara e intuitiva, proporcionando insights valiosos para profissionais de saúde e gestores.</h4><hr style='border: 1px solid #00FFFF;'>", unsafe_allow_html=True)
    

