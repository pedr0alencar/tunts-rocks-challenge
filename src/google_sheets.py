from google.oauth2.service_account import Credentials
import gspread
import logging
import sys


# Defining the correct scopes
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

# Loading credentials from the service account
SERVICE_ACCOUNT_FILE = '../credentials/tunts-rocks-pedro-alencar-928cdef6d732.json'
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Authenticating and creating the API client
client = gspread.authorize(creds)


def get_worksheet(spreadsheet_id, sheet_name):
    # Open the spreadsheet using its ID
    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)
    return worksheet


def read_student_data(worksheet):
    # Read the data, excluding the header
    student_data = worksheet.get_all_values()[3:]  # assumes the first row is the header
    if not student_data:
        logging.warning('No data was read from the spreadsheet.')
        sys.exit(1)
    else:
        logging.info('Spreadsheet data successfully read.')
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

    # Update the cells in batch
    try:
        worksheet.batch_update(update_cells)
        logging.info('Data inserted into the spreadsheet.')
    except Exception as e:
        logging.error(f'Failed to update cells in batch: {e}')
        sys.exit(1)


