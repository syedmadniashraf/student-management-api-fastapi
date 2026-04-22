from app.database import get_connection

# Validate input before DB operations
def validate_student(name, roll, grade):
    if not name.strip():
        raise ValueError("Name cannot be empty")
    if not roll.strip():
        raise ValueError("Roll number cannot be empty")
    if grade not in ["A", "B", "C", "D", "F"]:
        raise ValueError("Invalid grade")


class StudentService:

    @staticmethod
    def add_student(student):
        validate_student(student.name, student.roll_number, student.grade)

        query = """
        INSERT INTO students (name, roll_number, course, grade)
        VALUES (%s, %s, %s, %s)
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (student.name, student.roll_number, student.course, student.grade))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_students():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def get_student(roll_number):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE roll_number=%s", (roll_number,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def update_student(roll, name, course, grade):
        validate_student(name, roll, grade)

        query = """
        UPDATE students
        SET name=%s, course=%s, grade=%s
        WHERE roll_number=%s
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query, (name, course, grade, roll))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_student(roll):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE roll_number=%s", (roll,))
        conn.commit()
        cursor.close()
        conn.close()