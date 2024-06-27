def search_name_student(students: list):
    key_to_search = input("Search by name or last name? ")
    letter_to_search = input("what is the first letters? ")
    if key_to_search == "name":
        student_found = [
            student
            for student in students
            if student["name"].lower().startswith(letter_to_search)
        ]
        if student_found:
            return print(
                f"the students are start with {letter_to_search}: {student_found}"
            )
        else:
            print(f"No students found starting with '{letter_to_search}'")
    elif key_to_search == "last name":
        student_found_last_name = [
            student
            for student in students
            if student["last_name"].lower().startswith(letter_to_search)
        ]
        if student_found_last_name:
            return print(
                f"the last name of students are start with {letter_to_search}: {student_found_last_name}"
            )
        else:
            print(f"No students found starting with '{letter_to_search}'")


def search_age_student(students):
    age_to_search = int(input("What age to look for? "))
    layer_age = input("Do you want to find big small or same age, enter <>= ")
    for student in students:
        if layer_age == "<":
            if student["age"] < age_to_search:
                print(f"the student are smaller than age {age_to_search}: {student}")
        elif layer_age == ">":
            if student["age"] > age_to_search:
                print(f"the student are bigger than age {age_to_search}: {student}")
        elif layer_age == "=":
            if student["age"] == age_to_search:
                print(f"the student are equal in age {age_to_search}: {student}")
