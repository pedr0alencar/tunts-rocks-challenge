from google.oauth2.service_account import Credentials
import gspread
import logging
import sys


# Definindo os escopos corretos
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Carregando as credenciais da conta de serviço
SERVICE_ACCOUNT_FILE = (r'C:\Users\User\PycharmProjects\desafio-tunts-rocks\credentials\tunts-rocks-pedro-alencar'
                        r'-928cdef6d732.json')
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Autenticando e criando o cliente da API
client = gspread.authorize(creds)


def get_worksheet(spreadsheet_id, sheet_name):
    # Use o ID para abrir a planilha
    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)
    return worksheet


def read_student_data(worksheet):
    # Lê os dados, excluindo o cabeçalho
    student_data = worksheet.get_all_values()[3:]  # assume que a primeira linha é cabeçalho
    if not student_data:
        logging.warning('Nenhum dado foi lido da planilha.')
        sys.exit(1)
    else:
        logging.info('Dados da planilha lidos com sucesso.')
    return student_data


def update_student_situations(worksheet, student_results):
    update_cells = []
    for index, student in enumerate(student_results, start=4):
        situation_cell = f'G{index}'
        naf_cell = f'H{index}'
        update_cells.append({
            'range': situation_cell,
            'values': [[student[2]]],
        })
        update_cells.append({
            'range': naf_cell,
            'values': [[student[3]]],
        })

    # Imprime os valores que serão escritos para depuração


    # Atualiza as células em batch
    try:
        worksheet.batch_update(update_cells)
        logging.info('Dados inseridos na planilha.')
    except Exception as e:
        logging.error(f'Failed to update cells in batch: {e}')
        sys.exit(1)
        #print(f'Failed to update cells in batch: {e}')

