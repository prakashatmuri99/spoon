
# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def display_students():
    if not students:
        print("No students found.")
        return

    print("\n--- Student Details ---")

    for student in students:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])
        print("-----------------------")


def search_student():
    name = input("Enter name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student found!")
            print(student)
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
