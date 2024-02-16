![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/3ee79eb2-f0ff-4b8e-b4b4-37cf63dac95a)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


# Tunts.Rocks Challenge - Student Situation Analysis
Technical challenge from Tunts.Rocks - Dev Training Program  

## Summary

- [Link to the candidate's copied spreadsheet](#link-to-the-candidates-copied-spreadsheet)
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [How to Run Locally](#how-to-run-locally)
    - [Dependencies Installation](#dependencies-installation)
    - [Running the Application](#running-the-application)
- [About the Code](#about-the-code)
    - [Logging](#logging)
- [How to Run with Your Own Spreadsheet](#how-to-run-with-your-own-spreadsheet)
    - [Create a Project on Google Cloud Platform (GCP)](#create-a-project-on-google-cloud-platform-gcp)
    - [Enable Google Sheets API for Your Project](#enable-google-sheets-api-for-your-project)
    - [Create a Service Account](#create-a-service-account)
    - [Download the JSON Key File](#download-the-json-key-file)
    - [Setting Up Environment Variables](#setting-up-environment-variables)
- [Security Considerations](#security-considerations)
- [Demonstration](#demonstration)



## Link to the candidate's copied spreadsheet
https://docs.google.com/spreadsheets/d/1qB_SdyfU3-MWK0i3rnFdYvhLK4nOVcoGu60S9Og_Vt8/edit#gid=0 

   

## Overview
This Python script automates the analysis of students' situations in a Google Sheets document based on their grades and attendance. It calculates the average of the three exams (P1, P2, and P3) for each student and determines their situation according to the rules below:

- **Failed due to Grade**: When the average grade (m) is below 5.
- **Final Exam**: When the average grade is between 5 and 7 (5 ≤ m < 7).
- **Approved**: When the average grade is 7 or higher (m ≥ 7).

Additionally, if the student's absences exceed 25% of the total classes, they will be automatically **Failed due to Absence**, regardless of the average. For students in the "Final Exam" situation, the script also calculates the **Necessary Grade for Final Approval (NGFA)**. This grade is calculated so that the final average, considering the NGFA, is at least 5 for approval, following the formula: 5 ≤ (m + ngfa)/2.

The script updates the spreadsheet with this information, automating the process of analyzing the students' situations.

## Prerequisites
- Python 3.8 or higher.
- Google account with access to the Google Sheets API.
- Project on Google Cloud with the Sheets API enabled.
- Service account on Google Cloud with permissions for the Sheets API and a JSON key file.

## How to run locally
For the purpose of evaluating the challenge, the application will consume the API already with the information from the copy of the candidate's spreadsheet. Thus, to execute:

1. Clone the repository with:
```
git clone https://github.com/pedr0alencar/tunts-rocks-challenge.git
```
2. Navigate to the project directory and set up a Python virtual environment to manage dependencies.
```
cd tunts-rocks-challenge
```

### Dependencies Installation
Use `pip install -r requirements.txt` to install the necessary dependencies.


### Running the Application
Use the command `python src/main.py` to start the process of reading, analyzing, and updating the students' situations in your Google Sheets spreadsheet.

## About the code
The application is divided into three main files:

- `google_sheets.py`: Manages authentication and interaction with the Google Sheets API.
- `student_analysis.py`: Contains the logic to calculate each student's situation based on the provided rules.
- `main.py`: Orchestrates the process by calling functions from the other modules.

Additionally, we have:
- `credentials`: Stores the spreadsheet's json key within the Google Cloud project.
- `.env`: Parameterizes the name and the id of the spreadsheet.

### Logging
Logging was used for activity monitoring, if everything goes right, it will show:  

![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/bc52555a-fd0d-446d-aa5a-465b9070c6c0)  
  
Logging of warning and error was also added for the cases:
- No data was read on the spreadsheet.
- Failure to update cells in the table.
- Error processing line.
  
If there is an error reading or inserting data into the spreadsheet, the execution will be terminated.

## How to run with your own spreadsheet:
Create a Project on Google Cloud Platform (GCP):

- Visit the Google Cloud Console.
- Click on the "Project" dropdown near the upper left corner, then click on "New Project".
- Name your project (e.g., "Tunts Rocks Challenge") and click on "Create".

Enable Google Sheets API for Your Project:

- With your new project selected, navigate to "APIs & Services" > "Dashboard" on the left sidebar.
- Click on "ENABLE APIS AND SERVICES" at the top. Search for "Google Sheets API", select it, and click on "Enable".

Create a Service Account:

- Go to "APIs & Services" > "Credentials" and click on "Create Credentials" at the top. Select "Service account" from the dropdown.
- Name your service account (e.g., "sheets-access"), grant it a "Editor" role (this gives it permissions to access and modify your Google Sheets) and click on "Done".
- After creating the service account, click on it in the "Credentials" page. Go to the "Keys" tab, click on "Add Key" and choose "Create new key". Select "JSON" as the key type and click on "Create". This will download the JSON key file to your computer.

Download the JSON Key File:

- Store the downloaded JSON key file securely. This file contains sensitive information that allows programmatic access to your Google Cloud resources.
- You will use this file in your project to authenticate the script with the Google Sheets API.

Setting Up Environment Variables:

- Move the downloaded JSON key file to the `credentials` directory within your project. Ensure the path in your script matches the location of this file.
- Use the `.env` file to set environment variables such as `SPREADSHEET_ID` and `SHEET_NAME`, with the respective values for the ID of your Google Sheet and the name of the tab you intend to manipulate.

## Demonstration
Images of the spreadsheet before and after execution:  
  
![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/3ceb90fc-66bb-4f9b-ad35-45a4ff83742f)
  
![image](https://github.com/pedr0alencar/tunts-rocks-challenge/assets/122798848/a5597c96-6ddb-4e17-8564-9616c080b4a7)


## Security Considerations
This project includes sensitive data, such as API keys, for demonstration purposes. In a real scenario, such information would not be publicly exposed.


---

Make it fun, see you soon (-;
Work hard Play hard!
```
Speedy Dev off
```
