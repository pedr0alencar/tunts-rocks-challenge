from google_sheets import get_worksheet, read_student_data, update_student_situations
from student_analysis import calculate_student_situation
import os
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')


def main():
    load_dotenv()

    # Use the spreadsheet ID here
    spreadsheet_id = os.getenv('SPREADSHEET_ID')
    sheet_name = os.getenv('SHEET_NAME')

    # Retrieve the specific worksheet from the spreadsheet
    worksheet = get_worksheet(spreadsheet_id, sheet_name)
    # Read student data from the worksheet
    student_data = read_student_data(worksheet)
    # Calculate the situation for each student based on the data
    student_results = calculate_student_situation(student_data)
    # Update the spreadsheet with the calculated student situations
    update_student_situations(worksheet, student_results)
    logging.info('Spreadsheet successfully updated.')


if __name__ == "__main__":
    main()
