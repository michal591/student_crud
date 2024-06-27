"""
    if selection == 1:
        return list_students(students)
    elif selection == 2:
        return add_student(students)
    elif selection == 3:
        return delete_student(students)
    elif selection == 4:
        return edit_student(students)
    elif selection == 5:
        return search_name_student(students)
    elif selection == 6:
        return search_number_student(students)
"""


def list_students(students):
    for student in students:
        print(student)


def add_student(students: list):
    new_name = input("enter a new name of student ")
    new_last_name = input("enter a new last name of student ")
    new_age = input("enter the age of the new student ")
    new_student = {"name": new_name, "last_name": new_last_name, "age": new_age}
    students.append(new_student)
    print("added a new student:", new_student)


def delete_student(students: list):
    list_students(students)
    choise_delete = int(input("which student you want to delete? "))
    students.pop(choise_delete)


def edit_student(students):
    list_students(students)
    student_to_edit = input("Enter the name of the student to edit: ")
    key_to_edit = input("Which key do you want to edit (name, last_name, age)? ")
    new_value = input("What is the new value for this student? ")
    student_found = False
    for student in students:
        if student["name"] == student_to_edit:
            student_found = True
            if key_to_edit in student:
                if key_to_edit == "age":
                    new_value = int(new_value)
                student[key_to_edit] = new_value
                print(f"Student '{student_to_edit}' has been updated to: {student}")
                return
            else:
                print(f"Invalid key! Available keys are: {', '.join(student.keys())}")
                return
    if not student_found:
        print(f"Student '{student_to_edit}' not found. Please enter a valid name.")
