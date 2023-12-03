from fastapi import FastAPI, File, UploadFile,Request,Form
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.post("/")
async def upload_csv(request: Request,file: UploadFile = File(...), name_column:int =  Form(...),age_column:int=Form(...)):
    # Read the CSV file
    contents = await file.read()
    lines = contents.decode("utf-8").splitlines()

    # Create a SQLite database connection
    conn = sqlite3.connect("database.sqlite3")
    c = conn.cursor()

    # Create the Users table if it doesn't exist
    c.execute("CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")

    # Insert the data from the CSV file into the database
    for line in lines:
        columns = line.split(",")
        name = columns[name_column]
        age = columns[age_column]
        c.execute("INSERT INTO Users (name, age) VALUES (?, ?)", (name, age))

    # Commit the changes
    conn.commit()

    # Close the database connection
    conn.close()

    # Render the Jinja template
    return templates.TemplateResponse("index.html", {'request':request,"name": name, "age": age})

#return data in frontend
@app.get("/")
async def index(request:Request):
    # Get all the users from the database
    conn = sqlite3.connect("database.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM Users")
    users = c.fetchall()

    # Render the Jinja template
    return templates.TemplateResponse("index.html", {'request':request,"users": users})

