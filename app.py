import streamlit as st
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from auth import authenticate_google_sheets, access_google_sheet

st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
        .responsive-iframe {
            position: relative;
            width: 100%;
            padding-top: 56.25%; /* Proporção de 16:9 */
            height: 0;
            overflow: hidden;
        }

        .responsive-iframe iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
        /* Forçar o tamanho e a cor da barra lateral */
        [data-testid="stSidebar"] {
            background-color: #191a1f !important;
            width: 20% !important; /* Reduzir largura */
        }

        /* Redimensionar a imagem na barra lateral */
        [data-testid="stImage"] img {
            width: 50px; /* Reduzir tamanho da imagem */
            display: block;
            margin: 0 auto;
        }

        /* Centralizar e ajustar o header */
        .header-container {
            text-align: center;
            font-size: 2em;
            margin-bottom: 20px;
        }

        /* Ajustar as tabs para não sobrepor */
        div[data-testid="stTabs"] > div {
            margin-top: -10px;
        }

        /* Estilizar os botões na barra lateral */
        .sidebar-button {
            display: block;
            text-align: center;
            background-color: white;
            color: black !important;
            padding: 10px 15px;
            margin: 10px auto;
            border-radius: 15px;
            text-decoration: none;
            font-weight: bold;
        }

        .sidebar-button:hover {
            background-color: #f0f0f0;
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

st.sidebar.image("logobk.jpg", caption="", use_container_width=False)

st.title('Dashboard BK Financeiro')

def acionar_webhooks():
    webhook1_url = "https://n8n.fxautomate.top/webhook/dashboard"
    webhook2_url = "https://n8n.fxautomate.top/webhook/faturamento"
    
    payload_1 = {"message": "Acionando primeiro webhook!"}
    payload_2 = {"message": "Acionando segundo webhook!"}
    
    try:
        response_1 = requests.post(webhook1_url, json=payload_1)
        if response_1.status_code == 200:
            st.success("Primeiro Webhook acionado com sucesso!")
        else:
            st.error(f"Erro ao chamar o primeiro Webhook: {response_1.status_code}")
    except Exception as e:
        st.error(f"Erro ao chamar o primeiro Webhook: {str(e)}")
    
    try:
        response_2 = requests.post(webhook2_url, json=payload_2)
        if response_2.status_code == 200:
            st.success("Segundo Webhook acionado com sucesso!")
        else:
            st.error(f"Erro ao chamar o segundo Webhook: {response_2.status_code}")
    except Exception as e:
        st.error(f"Erro ao chamar o segundo Webhook: {str(e)}")
    

tab1, tab2 = st.tabs(["BK REVIEWS", "BK ARTS"])
with tab1:
    st.header("BK REVIEWS")
    if st.button('Atualizar Planilha Reviews'):
        acionar_webhooks()
    
    st.markdown(
    """
    <div class="responsive-iframe">
        <iframe title="BK REVIEWS" width="853" height="540" src="https://app.powerbi.com/view?r=eyJrIjoiZTAwZDBmNjktMWJhMy00YjI2LTliMmMtOGQ3NDcwOGY5MGExIiwidCI6ImFiYThhNDc3LTE0MGItNDNiOC04MGQzLWYxOTQwNGVhMTc0YyJ9" frameborder="0" allowFullScreen="true"></iframe>
    <\div>
    """,
    unsafe_allow_html=True,
)

with tab2:
    st.header("BK ARTS")
    st.markdown(
        """
        <div class="responsive-iframe">
            <iframe title="BK ARTS v3" width="853" height="540" src="https://app.powerbi.com/view?r=eyJrIjoiYjA0ZjEyZTItYzIxOS00MjY4LTljYTEtYTUwMjMxYTAxMmFhIiwidCI6ImFiYThhNDc3LTE0MGItNDNiOC04MGQzLWYxOTQwNGVhMTc0YyJ9" frameborder="0" allowFullScreen="true"></iframe>
        <\div>
        """,
        unsafe_allow_html=True,)


planilhas = {
    "Tráfego Ads": "https://docs.google.com/spreadsheets/d/1WekoU7hKiA8FIQDvn7lAxRf3YCFODhY1NCO2YdLRWLU/edit?gid=0#gid=0",  
    "Financeiro Arts": "https://docs.google.com/spreadsheets/d/1aLMifpOxJBer9h3xUf70Fq9DvpnlokZh/edit?gid=12781143#gid=12781143",
    "Financeiro Reviews": "https://docs.google.com/spreadsheets/d/1JGj2V2jYiu9Ofdg-4JUjg606Ssb7nugliOEZLZ9Jzss/edit?gid=0#gid=0",
    "Fluxo Anual 2025": "https://docs.google.com/spreadsheets/d/1B1Hqh6uKciOnAlT8OAEJcp2Ybo5bXqT2514G-iouPXQ/edit?gid=513733305#gid=513733305",
    "Fechamentos 2025": "https://docs.google.com/spreadsheets/d/16PVILwVOZxrzpT0U9qnRjyu2o1ac3dlHUa6lM_5DqhY/edit?gid=424343636#gid=424343636"
}

for planilha, link in planilhas.items():
    if st.sidebar.button(planilha):
        st.markdown(f'<meta http-equiv="refresh" content="0;url={link}">', unsafe_allow_html=True)