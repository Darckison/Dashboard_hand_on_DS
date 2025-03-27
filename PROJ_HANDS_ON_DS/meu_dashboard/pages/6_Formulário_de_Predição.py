import streamlit as st
import joblib
import numpy as np
import pandas as pd


###################################################]
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

# Verificar se o arquivo do modelo existe antes de carregar
modelo_path = "MODELO_DE_ARVORE_PRED.pkl"

###################################################################
modelo_path = "meu_dashboard\pages\MODELO_DE_ARVORE_PRED.pkl"


try:
    modelo = joblib.load(modelo_path)
except FileNotFoundError:
    st.error("Erro: O arquivo do modelo não foi encontrado. 🚨")
    st.stop()

# Criar interface
st.title("Predição de Tuberculose")

# Entrada de dados do paciente
#idade = st.number_input("Idade", min_value=0, max_value=120, value=30)
sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
municipio= st.selectbox("Municipio", ['Boa Vista', 'Caracarai', 'Mucajaí', 'Alto Alegre', 'Amajarí', 'Bom Fim', 'Cantá', 'Caroebe', 'Iracema', 'Normandia', 'Pacaraima', 'Rorainópolis', 'São João da Baliza', 'São Luiz','Uiramutã'])
ano_diagnostico = st.number_input("Qual o ano vigente?", min_value=50, max_value=2026, value=2000)
teste_hiv = st.selectbox("Teste HIV", ["Positivo", "Negativo"])
DT_DIAG = st.date_input("📅 Informe a data do diagnostico do caso de tuberculose")


# Converter os dados para um formato adequado ao modelo
#sexo_binario = 1 if sexo == "Masculino" else 0
#dados_paciente = np.array([[ sexo_binario, ano_diagnostico, teste_hiv, municipio]])
###################################################################################################################################
#MAPEAMENTO DE COLUNAS


mapping_hiv = {
  1.0:'Positivo',
  2.0: 'Negativo',
 
}


mapping_municipio ={

    0: 'Boa Vista',
    1: 'Caracarai',
    2: 'Mucajaí',
    3: 'Alto Alegre',
    4: 'Amajarí',
    5: 'Bom Fim',
    6: 'Cantá',
    7: 'Caroebe',
    8: 'Iracema',
    9: 'Normandia',
    10: 'Pacaraima',
    11: 'Rorainópolis',
    12: 'São João da Baliza',
    13: 'São Luiz',
    14:'Uiramutã'

}

mapping_sexo = {
    0:'Masculino',
    1:'Feminino',
    
}

feature_names = ['TP_NOT', 'ID_AGRAVO', 'DT_NOTIFIC', 'NU_ANO', 'SG_UF_NOT',
       'ID_MUNICIP', 'DT_DIAG', 'NU_IDADE_N', 'CS_SEXO', 'GESTANTES', 'SG_UF',
       'ID_MN_RESI', 'ID_PAIS', 'TRATAMENTO', 'BACILOSC_E', 'CULTURA_ES',
       'HIV', 'municipio']

################################################################

if sexo == "Masculino" :
     sexo = 0
else:
     sexo = 1

#################################################################

if municipio == 'Boa Vista':
     municipio = 0
elif municipio == 'Caracarai':
     municipio = 1
elif municipio == 'Mucajaí':
     municipio = 2
elif municipio == 'Alto Alegre':
     municipio = 3
elif municipio == 'Amajarí':
     municipio = 4
elif municipio == 'Bom Fim':
     municipio = 5
elif municipio == 'Cantá':
     municipio = 6
elif municipio == 'Caroebe':
     municipio = 7
elif municipio == 'Iracema':
     municipio = 8
elif municipio == 'Normandia':
     municipio = 9
elif municipio == 'Pacaraima':
     municipio = 10
elif municipio == 'Rorainópolis':
     municipio = 11
elif municipio == 'São João da Baliza':
     municipio = 12
elif municipio == 'São Luiz':
     municipio = 13
elif municipio == 'Uiramutã':
     municipio = 14

################################################################

if teste_hiv == "Positivo":
     teste_hiv = 1.0
else:
     teste_hiv = 2.0

##################################################################

DT_DIAG = int(DT_DIAG.strftime("%Y%m%d"))







    
    # Botão para realizar a predição
if st.button("Fazer Predição"):
    
        # Create a new DataFrame with all features
        novo_dado = pd.DataFrame([[ano_diagnostico, 14, DT_DIAG, sexo, teste_hiv , municipio]], columns=[ 'NU_ANO', 'SG_UF_NOT', 'DT_DIAG', 'CS_SEXO','HIV', 'municipio'])

        # Reindex the new DataFrame to match the training data columns
        # Fill missing columns with 0 (or appropriate values)
        novo_dado = novo_dado.reindex(columns=feature_names, fill_value=0)

        # Predição com o modelo treinado
        # Change best_dt_classifier to best_clf
        #previsao = best_dt_classifier.predict(novo_dado)



        # EXIBIR O RESULTADO DA PREDIÇÃO JUNTO A ACURÁCIA
        #print(f'Predição para um modelo exemplo:{"Sim" if previsao [0] == 1 else "Não"}')
        #print(f"Acurácia do melhor modelo: {accuracy}")
        
        predicao = modelo.predict(novo_dado)
        resultado = (
    "De acordo com os dados inseridos, o paciente tem suspeita **POSITIVA** de tuberculose."
    if predicao[0] == 1
    else "De acordo com os dados inseridos, o paciente tem suspeita **NEGATIVA** de tuberculose."
     )

# Exibir o resultado no Streamlit
        st.write(resultado)

