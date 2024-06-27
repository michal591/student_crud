from crud.crud import list_students, add_student, delete_student, edit_student
from crud.search import search_name_student, search_age_student


def menu_selection(students, selection):
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
        return search_age_student(students)
