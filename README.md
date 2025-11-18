# 🏫 Flask Student API

Flask Student API is a Python-based web application built with Flask and SQLite for managing student records. It provides full CRUD functionality (Create, Read, Update, Delete) through a user-friendly web interface.

### 📂 Project Structure
'''
Flask_student_api/
│
├── app.py # 🖥️ Main Flask application with routing and CRUD logic
├── Student.db # 🗄️ SQLite database storing student records
├── requirements.txt # 📦 Project dependencies
├── Procfile # 🚀 Deployment configuration for platforms like Heroku
├── .gitignore # ❌ Files to ignore in Git
└── templates/ # 🌐 HTML templates for frontend UI
├── Home.html
├── Form.html
├── getData.html
├── Delete_data.html
├── UPDATE.html
└── NOTFOUNT.html
'''
### ✨ Features

➕ Add Student Records – Input student details via a web form.

📄 View Records – Fetch and display all student records dynamically.

✏️ Update Records – Edit student details with validation.

🗑️ Delete Records – Remove student entries safely with existence check.

⚠️ Error Handling – Displays “Not Found” page if a student record doesn’t exist.

### 🛠️ Technologies Used

Backend: Python 🐍, Flask ⚡

Database: SQLite 🗄️

Frontend: HTML templates (Jinja2) 🌐

Deployment Ready: Procfile 🚀


