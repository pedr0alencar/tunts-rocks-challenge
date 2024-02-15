from google_sheets import get_worksheet, read_student_data, update_student_situations
from student_analysis import calculate_student_situation
import os
from dotenv import load_dotenv
import logging


# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def main():
    load_dotenv()

    # Use o ID da planilha aqui
    spreadsheet_id = os.getenv('SPREADSHEET_ID')
    sheet_name = os.getenv('SHEET_NAME')

    worksheet = get_worksheet(spreadsheet_id, sheet_name)
    student_data = read_student_data(worksheet)
    student_results = calculate_student_situation(student_data)
    update_student_situations(worksheet, student_results)
    logging.info('Planilha atualizada com sucesso.')

    #print("Planilha atualizada com sucesso.")


if __name__ == "__main__":
    main()
