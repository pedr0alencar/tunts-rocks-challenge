![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/3ee79eb2-f0ff-4b8e-b4b4-37cf63dac95a)

# Tunts.Rocks Challenge - Student Situation Analysis

## Overview
This Python script automates the analysis of student situations in a Google Sheets document based on their grades and attendance. It reads the data, calculates whether the student is approved, disapproved due to absence, disapproved due to grades, or if they need a final exam, and updates the spreadsheet with this information.

## Prerequisites
- Python 3.8 or higher.
- Google account with access to the Google Sheets API.
- Google Cloud project with the Sheets API enabled.
- Service account in Google Cloud with permissions for the Sheets API and a JSON key file.

## Preparing the Spreadsheet
Before running the script, you need to prepare a Google Sheets document that the script will interact with. The script reads and updates the student data on this spreadsheet based on their grades and attendance.

1. **Copy the Provided Spreadsheet**: Access the provided Google Sheets template link. Use the "File" > "Make a copy" option to create a copy of the spreadsheet in your own Google Drive.
The link that we are using: https://docs.google.com/spreadsheets/d/1XvWJcRLj2WAeXO3ULQ_GxGm9---3SZkjMbGcXMJtt70/edit#gid=0

3. **Rename the Spreadsheet**: Rename the copied spreadsheet to "Software Engineering Challenge - [Your Name]".

4. **Adjust Sharing Settings**: Change the spreadsheet's sharing settings to "Anyone with the link can edit" to ensure the script can access and modify the spreadsheet. This step is crucial for the script's ability to update the spreadsheet without authentication errors.

5. **Note the Spreadsheet ID**: The spreadsheet ID can be found in the URL of your Google Sheet. It's the long string of letters and numbers between "/d/" and "/edit". You will need this ID to configure the script to target your copied spreadsheet.

6. **Specify the Sheet Name**: If you have renamed the tab within the spreadsheet or want to target a specific sheet, note the exact name of the sheet. This name is also required for the script configuration.

After preparing your spreadsheet and noting down the necessary details, proceed with the initial setup of the project environment and the Google Cloud Platform configurations as described below.

## Initial Setup
Before running the application, you need to set up your Google Cloud project and configure access to the Google Sheets API. Follow these detailed steps to ensure everything is correctly configured:

1. **Create a Project in Google Cloud Platform (GCP)**:
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Click on the "Project" dropdown near the top-left corner and then click on "New Project".
   - Name your project (e.g., "Tunts Rocks Challenge"), and click "Create".

2. **Enable the Google Sheets API for Your Project**:
   - With your new project selected, navigate to the "APIs & Services" > "Dashboard" section from the left sidebar.
   - Click "ENABLE APIS AND SERVICES" at the top. Search for "Google Sheets API", select it, and click "Enable".

3. **Create a Service Account**:
   - Go to "APIs & Services" > "Credentials", and click on "Create Credentials" at the top. Select "Service account" from the dropdown.
   - Name your service account (e.g., "sheets-access"), grant it a role of "Editor" (this gives it permissions to access and modify your Google Sheets), and click "Done".
   - After creating the service account, click on it in the "Credentials" page. Go to the "Keys" tab, click on "Add Key", and choose "Create new key". Select "JSON" as the key type, and click "Create". This will download the JSON key file to your computer.

4. **Download the JSON Key File**:
   - Store the downloaded JSON key file securely. This file contains sensitive information that allows programmatic access to your Google Cloud resources.
   - You will use this file in your project to authenticate the script with the Google Sheets API.

5. **Setting Up the Environment Variables**:
   - Move the downloaded JSON key file to the `credentials` directory within your project. Ensure the path in your script matches the location of this file.
   - Use the `.env` file to set environment variables such as `SPREADSHEET_ID` and `SHEET_NAME` with the respective values of your Google Sheet ID and the name of the worksheet you intend to manipulate.

By completing these steps, you've set up your Google Cloud project, enabled the necessary API, created a service account for authentication, and prepared your project environment to run the application securely.



## Local Setup
1. **Clone the repository**:
```
git clone https://github.com/pedr0alencar/tunts-rocks-challenge.git
```
3. **Navigate to the project directory**:
```
cd tunts-rocks-challenge
```

## Python Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

1. **Create a virtual environment**:
```
python -m venv venv
```
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
```
pip install -r requirements.txt
```

## Environment Variable Configuration
1. **Save the Google service account JSON key** in the `credentials` directory.
2. **Set up the `.env` file** in the root of the project with the necessary environment variables:
SPREADSHEET_ID=1qB_SdyfU3-MWK0i3rnFdYvhLK4nOvco6u6s090g_Vt8
SHEET_NAME=engineering_software
Obs. This is mine SpreadSheet ID, if you want to find yours, get the url and select the Id between '/d/' and '/edit'
Exemple: ![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/3a35a990-4b4e-4980-99eb-f2be88c7163a)
Replace `1qB_SdyfU3-MWK0i3rnFdYvhLK4nOvco6u6s090g_Vt8` and `engineering_software` with the actual values of your Google Sheets document ID and the sheet name you are working with.

## Running the Application
To start the application, use the following command:
python src/main.py
This will initiate the process of reading, analyzing, and updating the student situations in your Google Sheets document.

## Logs and Info
After running the application, you shuld she this:
![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/bc52555a-fd0d-446d-aa5a-465b9070c6c0)

it means that the data succesfuly updated, the logs are all tested and if something go worng it will show you what isn't working on the application.


## Code Explanation

The application is divided into three main files:

- `google_sheets.py`: Responsible for authenticating and interacting with the Google Sheets API.
- `student_analysis.py`: Contains the logic to calculate each student's situation based on the defined rules.
- `main.py`: Coordinates the process by calling functions from the other modules to perform the reading and updating of the spreadsheet.

## Security Considerations
This project includes sensitive data such as API keys for demonstration purposes. In a real-world scenario, this information should never be exposed publicly. Always ensure that sensitive data is stored securely and not included in version control.

## Conclusion
This project demonstrates how to interact with the Google Sheets API using Python to automate the process of student data analysis. If you encounter any issues or have questions, please reach out to the repository maintainers.

Make it fun, see you soon (-;
```
Speedy Dev off
```


