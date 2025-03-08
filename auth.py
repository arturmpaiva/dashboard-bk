# auth.py
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Escopo para acessar as planilhas do Google Sheets (leitura apenas)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Caminho para o arquivo de credenciais do Google (OAuth 2.0)
CREDENTIALS_FILE = 'C:/Users/artur/Downloads/client_secret.json'  # Substitua pelo caminho correto

def authenticate_google_sheets():
    creds = None
    # O arquivo token.json armazena o token de acesso do usuário
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Se não houver credenciais válidas disponíveis, permita que o usuário faça login.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Se o token expirou, use o token de atualização
        else:
            # O fluxo de autenticação OAuth 2.0
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)  # O fluxo de autenticação ocorre aqui

        # Salve as credenciais no arquivo token.json para que não seja necessário autenticar novamente
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

# Função para acessar a planilha usando a API
def access_google_sheet(spreadsheet_id, range_name):
    creds = authenticate_google_sheets()
    service = build('sheets', 'v4', credentials=creds)  # Usando a API correta
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    return values
