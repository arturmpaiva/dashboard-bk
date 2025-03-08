import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from auth import authenticate_google_sheets, access_google_sheet

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

st.title('Dashboard BK Financeiro')

opcao = st.radio('Dashboards', ('BK REVIEWS', 'BK ARTS'))

# Se a opção for "Dashboard 1"
if opcao == 'BK REVIEWS':
    st.markdown('<h3 style="text-align: center;">BK Reviews</h3>', unsafe_allow_html=True)
    dashboard_1_url = "https://app.powerbi.com/reportEmbed?reportId=<SEU_REPORT_ID_1>&groupId=<SEU_GROUP_ID>&autoAuth=true&ctid=<SEU_CID>"
    st.markdown(f'<iframe title="BK REVIEWS" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=2390cc43-7f08-47e1-8cca-f6fd08b625d6&autoAuth=true&ctid=aba8a477-140b-43b8-80d3-f19404ea174c" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

elif opcao == 'BK ARTS':
    st.markdown('<h3 style="text-align: center;">BK Arts</h3>', unsafe_allow_html=True)
    dashboard_2_url = "https://app.powerbi.com/reportEmbed?reportId=<SEU_REPORT_ID_2>&groupId=<SEU_GROUP_ID>&autoAuth=true&ctid=<SEU_CID>"
    st.markdown(f'<iframe title="BK ARTS v3" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=ad96f27f-4afd-4964-8687-3bca4c6c185e&autoAuth=true&ctid=aba8a477-140b-43b8-80d3-f19404ea174c" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)


planilhas = {
    "Financeiro Ads": "https://docs.google.com/spreadsheets/d/1WekoU7hKiA8FIQDvn7lAxRf3YCFODhY1NCO2YdLRWLU/edit?gid=0#gid=0",  
    "Financeiro Arts": "https://docs.google.com/spreadsheets/d/1aLMifpOxJBer9h3xUf70Fq9DvpnlokZh/edit?gid=12781143#gid=12781143",
    "Financeiro Reviews": "https://docs.google.com/spreadsheets/d/1JGj2V2jYiu9Ofdg-4JUjg606Ssb7nugliOEZLZ9Jzss/edit?gid=0#gid=0",
    "Fluxo Anual 2025": "https://docs.google.com/spreadsheets/d/1B1Hqh6uKciOnAlT8OAEJcp2Ybo5bXqT2514G-iouPXQ/edit?gid=513733305#gid=513733305",
    "Fechamentos 2025": "https://docs.google.com/spreadsheets/d/16PVILwVOZxrzpT0U9qnRjyu2o1ac3dlHUa6lM_5DqhY/edit?gid=424343636#gid=424343636"
}

for planilha, link in planilhas.items():
    if st.sidebar.button(planilha):
        st.markdown(f'<a href="{link}" target="_blank">Clique aqui para acessar {planilha}</a>', unsafe_allow_html=True)