# Student Management System

students = []  # This list will store student dictionaries

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    student_class = input("Enter Class: ")
    marks = int(input("Enter Marks: "))
    
    student = {
        "roll_no": roll_no,
        "name": name,
        "class": student_class,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully")

def display_students():
    if not students:
        print("No students found.")
        return
    print("All Students:")
    for student in students:
        print(student)

def search_student():
    roll_no = input("Enter Roll No to search: ")
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student Found:", student)
            return
    print("Student not found.")

def update_student():
    roll_no = input("Enter Roll No to update: ")
    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = input("Enter New Name: ")
            student["class"] = input("Enter New Class: ")
            student["marks"] = int(input("Enter New Marks: "))
            print("Student updated successfully")
            return
    print("Student not found.")

def delete_student():
    roll_no = input("Enter Roll No to delete: ")
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully")
            return
    print("Student not found.\n")

# Main Program Loop
while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting... Goodbye")
        break
    else:
        print("Invalid choice. Please try again.")
