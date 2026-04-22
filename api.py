from fastapi import FastAPI, HTTPException
from app.models import Student
from app.services import StudentService

app = FastAPI(title="Student Management API")


@app.get("/")
def home():
    return {"message": "API is running"}


# Get all students
@app.get("/students")
def get_students():
    return StudentService.get_all_students()


# Get student by roll
@app.get("/students/{roll}")
def get_student(roll: str):
    student = StudentService.get_student(roll)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


# Add student
@app.post("/students")
def add_student(student: dict):
    try:
        s = Student(
            student["name"],
            student["roll_number"],
            student["course"],
            student["grade"].upper()
        )
        StudentService.add_student(s)
        return {"message": "Student added successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Update student
@app.put("/students/{roll}")
def update_student(roll: str, student: dict):
    try:
        StudentService.update_student(
            roll,
            student["name"],
            student["course"],
            student["grade"].upper()
        )
        return {"message": "Student updated"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Delete student
@app.delete("/students/{roll}")
def delete_student(roll: str):
    StudentService.delete_student(roll)
    return {"message": "Student deleted"}