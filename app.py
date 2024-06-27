from selection import menu_selection

students = [
    {"name": "michal", "last_name": "avramowitz", "age": 23},
    {"name": "moti", "last_name": "avramowitz", "age": 25},
]


def menu():
    while True:
        print("1 list of students")
        print("2 add a new student")
        print("3 delete a student")
        print("4 edit a student")
        print("5 search a student by name")
        print("6 search a student by age")
        print("7 exit")
        selection = int(input("please enter your selection: "))
        menu_selection(students, selection)
        if selection == 7:
            break


if __name__ == "__main__":
    menu()
