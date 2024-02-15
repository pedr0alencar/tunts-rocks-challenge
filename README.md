![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/3ee79eb2-f0ff-4b8e-b4b4-37cf63dac95a)

# Tunts.Rocks Challenge - Student Situation Analysis

## Overview
This Python script automates the analysis of student situations in a Google Sheets document based on their grades and attendance. It reads the data, calculates whether the student is approved, disapproved due to absence, disapproved due to grades, or if they need a final exam, and updates the spreadsheet with this information.

## Prerequisites
- Python 3.8 or higher.
- Google account with access to the Google Sheets API.
- Google Cloud project with the Sheets API enabled.
- Service account in Google Cloud with permissions for the Sheets API and a JSON key file.

## Initial Setup
1. **Create a project** in the Google Cloud Platform.
2. **Enable the Google Sheets API** for your project.
3. **Create a service account** and grant it the necessary permissions to access the Google Sheets API.
4. **Download a JSON key file** for your service account.

## Local Setup
1. **Clone the repository**:
git clone [Repository_Link]
2. **Navigate to the project directory**:
cd tunts-rocks-challenge

## Python Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

1. **Create a virtual environment**:
python -m venv venv
2. **Activate the virtual environment**:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

## Install Dependencies
Install the necessary dependencies with pip:
pip install -r requirements.txt

## Environment Variable Configuration
1. **Save the Google service account JSON key** in the `credentials` directory.
2. **Set up the `.env` file** in the root of the project with the necessary environment variables:
SPREADSHEET_ID=1qB_SdyfU3-MWK0i3rnFdYvhLK4nOvco6u6s090g_Vt8
SHEET_NAME=engineering_software
Obs. This is mine SpreadSheet ID, if you want to find yours, get the url and select the Id beteween the /d/ and the /edit#
Exemple: ![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/3a35a990-4b4e-4980-99eb-f2be88c7163a)
Replace `1qB_SdyfU3-MWK0i3rnFdYvhLK4nOvco6u6s090g_Vt8` and `engineering_software` with the actual values of your Google Sheets document ID and the sheet name you are working with.

## Running the Application
To start the application, use the following command:
python src/main.py
This will initiate the process of reading, analyzing, and updating the student situations in your Google Sheets document.

## Code Explanation

The application is divided into three main files:

- `google_sheets.py`: Responsible for authenticating and interacting with the Google Sheets API.
- `student_analysis.py`: Contains the logic to calculate each student's situation based on the defined rules.
- `main.py`: Coordinates the process by calling functions from the other modules to perform the reading and updating of the spreadsheet.

## Security Considerations
This project includes sensitive data such as API keys for demonstration purposes. In a real-world scenario, this information should never be exposed publicly. Always ensure that sensitive data is stored securely and not included in version control.

## Conclusion
This project demonstrates how to interact with the Google Sheets API using Python to automate the process of student data analysis. If you encounter any issues or have questions, please reach out to the repository maintainers.


