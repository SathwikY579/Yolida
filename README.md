# Streamlit Document Query Application

## Overview

This project is a Streamlit-based application that enables users to upload and query documents in various formats. The application securely stores the documents and user data, maintains a record of user interactions, and provides an option to download chat history.

### Features

- **Document Querying:** Supports `.pdf`, `.docx`, and `.txt` file formats. Users can search for specific information within the documents.
- **Secure Database:** Documents and user data are securely stored in an SQLite database with encryption.
- **User History:** Tracks user queries and responses, maintaining a private history for each user.
- **Downloadable Chat History:** Users can download their chat history as a text file.
- **User Interface:** A clean and intuitive interface built with Streamlit, allowing easy navigation and interaction.

## Project Structure

streamlit_document_query/
│
├── app.py # Main application file
├── database.py # Database setup and interaction
├── document_processor.py # Document processing functions
├── security.py # Security-related functions
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

git clone <repo-url>
cd streamlit_document_query
2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage dependencies:


# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
3. Install Dependencies
Install the required Python packages:

pip install -r requirements.txt
4. Run the Application
Use Streamlit to run the application
streamlit run app.py
This will start the application in your default web browser.

Application Features
1. Document Upload and Query
Upload Documents: Users can upload .pdf, .docx, or .txt files. The application extracts and stores the text content for querying.
Query Documents: Users can input queries to search the uploaded documents. The application will return the relevant sections of the documents that match the query.
2. User Interaction History
The application tracks and stores all user queries and responses in a secure manner.
Users can view their query history and download it as a text file.
3. Security Measures
Encryption: Sensitive data, including document content and user information, is encrypted before being stored in the database.
User Privacy: Each user's history is private and can only be accessed by them.
4. User Interface
Clean and Intuitive: The Streamlit interface is designed to be user-friendly, with easy navigation for uploading documents, performing searches, and managing history.
Database Schema
The application uses SQLite for data storage. The database schema includes three main tables:

Document: Stores the uploaded documents' filenames and encrypted content.
User: Stores user information, including encrypted passwords.
QueryHistory: Tracks user queries and the corresponding responses.
Example Schema
sql
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE query_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    query TEXT NOT NULL,
    response TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
Adding New Documents
To add new documents:

Navigate to the "Upload Document" section of the application.
Select the file you wish to upload (.pdf, .docx, or .txt).
The document's content will be extracted and securely stored in the database.
Security
The application uses the cryptography library to encrypt sensitive data before storing it in the database. Ensure that the encryption key is securely stored and managed, as it is crucial for data decryption.

Deployment
You can deploy the Streamlit application on platforms such as Streamlit Cloud, Heroku, or AWS. Below is an example of deploying on Streamlit Cloud:

1. Deploy on Streamlit Cloud
Push your repository to GitHub.
Go to Streamlit Cloud.
Sign in with your GitHub account and link the repository.
Configure the deployment settings and deploy the application.
2. Deploy on Heroku (Optional)
Install the Heroku CLI.
Log in to Heroku:
heroku login
Create a new Heroku application:
heroku create app-name
Push your application to Heroku:
git push heroku main
Open the application:
heroku open
Usage
Once the application is deployed, users can:

Upload and query documents.
View and download their interaction history.
Perform queries across multiple documents.
Contributions
Contributions are welcome! If you'd like to improve this application, please fork the repository and submit a pull request.
