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

```
student_management_system/
│
├── app/
│   ├── config.py        # Environment config
│   ├── database.py      # DB connection
│   ├── models.py        # Data model
│   └── services.py      # Business logic
│
├── api.py               # FastAPI routes
├── requirements.txt
└── .env (ignored)
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/syedmadniashraf/student-management-api-fastapi.git
cd student-management-api-fastapi
```

---

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create `.env` file:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=student_management_system
```

---

### 5. Run the server

```
uvicorn api:app --reload
```

---

### 6. API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Endpoints

| Method | Endpoint         | Description      |
| ------ | ---------------- | ---------------- |
| POST   | /students        | Add student      |
| GET    | /students        | Get all students |
| GET    | /students/{roll} | Get by roll      |
| PUT    | /students/{roll} | Update           |
| DELETE | /students/{roll} | Delete           |

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
* Deployment (Render/Railway)

---

## 👨‍💻 Author

**Syed Madni**

---

## ⭐ Support

If you like this project, consider giving it a ⭐
