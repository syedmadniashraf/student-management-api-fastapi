from app.models import Student
from app.services import StudentService


def main():
    while True:
        print("\n===== Student Management =====")
        print("1. Add Student")
        print("2. Show All")
        print("3. Get by Roll")
        print("4. Update")
        print("5. Delete")
        print("0. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Name: ")
                roll = input("Roll: ")
                course = input("Course: ")
                grade = input("Grade: ").upper()

                student = Student(name, roll, course, grade)
                StudentService.add_student(student)
                print("✔ Student added successfully")

            elif choice == "2":
                students = StudentService.get_all_students()
                for s in students:
                    print(s)

            elif choice == "3":
                roll = input("Roll: ")
                print(StudentService.get_student(roll))

            elif choice == "4":
                roll = input("Roll: ")
                name = input("New Name: ")
                course = input("Course: ")
                grade = input("Grade: ").upper()

                StudentService.update_student(roll, name, course, grade)
                print("✔ Student updated successfully")

            elif choice == "5":
                roll = input("Roll: ")
                StudentService.delete_student(roll)
                print("✔ Student deleted")

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Unexpected error occurred")


if __name__ == "__main__":
    main()