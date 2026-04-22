# 🎓 Student Management System API (FastAPI + MySQL)

A RESTful backend application built using **FastAPI** and **MySQL** that allows managing student records with full CRUD functionality.

---

## 🚀 Features

* ➕ Add new student
* 📄 Retrieve all students
* 🔍 Get student by roll number
* ✏️ Update student details
* ❌ Delete student

---

## 🛠 Tech Stack

* **Python**
* **FastAPI**
* **MySQL**
* **Uvicorn**
* **python-dotenv**

---

## 📁 Project Structure

```id="newstruct"
student-management-api-fastapi/
│
├── app/
│   ├── __init__.py        # Marks app as a Python package
│   ├── config.py          # Loads environment variables
│   ├── database.py        # Database connection setup
│   ├── models.py          # Data models (Student class)
│   └── services.py        # Business logic (CRUD operations)
│
├── api.py                 # FastAPI routes (endpoints)
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files (env, venv, etc.)
└── .env                   # Environment variables (not pushed)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```id="clonecmd"
git clone https://github.com/syedmadniashraf/student-management-api-fastapi.git
cd student-management-api-fastapi
```

---

### 2. Create virtual environment

```id="venvcmd"
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```id="installcmd"
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the root directory:

```id="envcmd"
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=student_management_system
```

---

### 5. Run the server

```id="runcmd"
uvicorn api:app --reload
```

---

### 6. Access API Docs

```id="docscmd"
http://127.0.0.1:8000/docs
```

---

## 🧪 API Endpoints

| Method | Endpoint         | Description         |
| ------ | ---------------- | ------------------- |
| POST   | /students        | Add student         |
| GET    | /students        | Get all students    |
| GET    | /students/{roll} | Get student by roll |
| PUT    | /students/{roll} | Update student      |
| DELETE | /students/{roll} | Delete student      |

---

## ⚠️ Notes

* Roll number should be unique
* Input validation implemented
* Environment variables used for security

---

## 💡 Future Improvements

* JWT Authentication
* Bulk insert API
* SQLAlchemy ORM
* Deployment (Render / Railway)

---

## 👨‍💻 Author

**Syed Madni**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
