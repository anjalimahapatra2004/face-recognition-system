# Face Recognition System

A Face Recognition Authentication System built using **FastAPI**, **OpenCV**, **face_recognition**, and **PostgreSQL**.

This project allows users to:

- Register using face recognition
- Store face encodings in PostgreSQL
- Login using face matching
- Use webcam directly from browser

---

# Features

- Face Registration
- Face Login Authentication
- PostgreSQL Database Integration
- FastAPI Backend
- HTML/CSS/JavaScript Frontend
- Webcam Integration
- Face Encoding Storage

---

# Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- OpenCV
- face_recognition

## Frontend
- HTML
- CSS
- JavaScript

---

# Project Structure

```bash
face-recognition-system/
│
├── app/
│   ├── controllers/
│   │   └── auth_controller.py
│   │
│   ├── database/
│   │   ├── base.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   └── user_model.py
│   │
│   ├── routes/
│   │   └── auth_routes.py
│   │
│   ├── services/
│   │   └── face_service.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── register.css
│   │   │   └── login.css
│   │   │
│   │   └── js/
│   │       ├── register.js
│   │       └── login.js
│   │
│   ├── templates/
│   │   ├── register.html
│   │   └── login.html
│   │
│   └── main.py
│
├── requirements.txt
└── README.md



Installation Guide


1. Clone Repository
git clone https://github.com/anjalimahapatra2004/face-recognition-system.git

cd face-recognition-system

2. Create Virtual Environment

Windows

python -m venv venv

Activate virtual environment:

venv\Scripts\activate


3. Install Dependencies
pip install -r requirements.txt


PostgreSQL Setup
4. Install PostgreSQL

Download PostgreSQL:

https://www.postgresql.org/download/

During installation:

Username: postgres
Password: your password
Port: 5432
5. Create Database

Open PostgreSQL Query Tool and run:

CREATE DATABASE face_db;
6. Configure Database Connection

Open:

app/database/connection.py

Update:

DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/face_db"

Run the Project

7. Start FastAPI Server
uvicorn app.main:app --reload

Server runs at:

http://127.0.0.1:8000


Pages
Register Face
http://127.0.0.1:8000/register


Login Face
http://127.0.0.1:8000/login


Database Table

The users table stores:

id
name
email
face_encoding


PostgreSQL Useful Queries
Show Tables
\dt
View Users
SELECT * FROM users;
Delete All Users
DELETE FROM users;
Drop Table
DROP TABLE users;


API Endpoints


Register Face
POST /register-face


Login Face
POST /login-face


How Face Recognition Works
Webcam captures image
Image sent to FastAPI backend
face_recognition library detects face
Face encoding generated
Encoding stored in PostgreSQL

During login:

New encoding generated
Compared with stored encodings
If matched → Login Success


