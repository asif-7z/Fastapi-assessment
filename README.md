# Fastapi-assessment
Overview
This FastAPI application allows users to upload a CSV file containing user data and then displays the data on the frontend. The user can specify the columns for the name and age fields during the upload. The data is stored in a SQLite database, and the frontend is rendered using Jinja2 templates.

Getting Started
1.Clone the repository:
```
git clone https://github.com/asif9048/Fastapi-assessment
cd Fastapi-assessment
```
2.Install dependencies:
```
pip install fastapi[all] jinja2
```
3.Run the FastAPI application:
```
uvicorn main:app --reload
```
4.Open your browser and go to http://127.0.0.1:8000/ to access the application.

## Usage:
### Uploading CSV File
- Navigate to the root URL http://127.0.0.1:8000/ in your browser.

- Use the file upload form to select a CSV file.

- Specify the column indices for the name and age fields.

- Click the "Submit" button to upload the CSV file and store the data in the database.

### Viewing Uploaded Data
- After uploading the CSV file, the application will display the user data on the frontend.

- Visit http://127.0.0.1:8000/ to see the displayed user data.
### Project Structure
- main.py: Contains the FastAPI application code.
- templates/: Directory containing Jinja2 templates.
- database.sqlite3: SQLite database file to store user data.
### Dependencies
- FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- Jinja2: Jinja2 is a fast, expressive, succinct, extensible, and widely used template engine.
### Note
- Ensure that you have SQLite installed or make any necessary adjustments to the database connection details based on your requirements.
- This application is a simple example and may require additional enhancements for production use, such as authentication, validation, and error handling.
