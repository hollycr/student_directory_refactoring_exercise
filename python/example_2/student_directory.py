import csv
import sys

students = []

def print_menu():
    print("1. Input the students")
    print("2. Show the students")
    print("3. Save the list to a csv file")
    print("4. Load the list from a csv file")
    print("9. Exit")

def interactive_menu():
    while True:
        print_menu()
        process(input().strip())

def process(selection):
    if selection == "1":
        data_entry_loop()
        feedback_message("data entered")
    elif selection == "2":
        if students:
            show_students()
            feedback_message("data printed")
        else:
            print("There are currently no students in the system to display.")
    elif selection == "3":
        save_students()
        feedback_message("data saved")
    elif selection == "4":
        load_students()
        feedback_message("data loaded")
    elif selection == "9":
        sys.exit()  # this will cause the program to terminate
    else:
        print("I don't know what you mean. Try again!")

def feedback_message(operation):
    print("\v" + operation.upper() + " SUCCESSFULLY!\v")

def save_students():
    filename = input("Please enter the filename (inc. extension) in which you'd like to save the data: ")
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for student in students:
            writer.writerow([student["firstname"], student["surname"], student["birthplace"], student["cohort"]])

def load_students():
    filename = input("Please enter the filename (inc. extension) that you'd like to load: ")
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            push_to_array(firstname=row[0], surname=row[1], birthplace=row[2], cohort=row[3])

def initial_load_students():
    filename = sys.argv[1] if len(sys.argv) > 1 else "students.csv"
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                push_to_array(firstname=row[0], surname=row[1], birthplace=row[2], cohort=row[3])
        print(f"Loaded {len(students)} from {filename}")
    except FileNotFoundError:
        print(f"No file was given on startup so loaded \"students.csv\" by default.")

def prompt(output):
    if not output:
        enter = input("Hit enter to exit or \"-\" to enter (a)nother student.\n")
        if enter:
            return user_data_entry()
        return {}
    return user_data_entry()

def user_data_entry():
    print("Please enter the first name, last name, birthplace and cohort of each student.")
    details = {
        "firstname": "--",
        "surname": "--",
        "birthplace": "--",
        "cohort": "unknown"
    }
    
    firstname = input("Enter first name: ")
    if firstname == "":
        return None
    details["firstname"] = firstname

    surname = input("Enter surname: ")
    if surname == "":
        return None
    details["surname"] = surname

    birthplace = input("Enter birthplace: ")
    if birthplace == "":
        return None
    details["birthplace"] = birthplace

    cohort = input("Enter cohort: ")
    if cohort == "":
        return None
    details["cohort"] = cohort

    return details

def push_to_array(**args):
    defaults = {
        "firstname": "--",
        "surname": "--",
        "birthplace": "--",
        "cohort": "unknown"
    }
    defaults.update(args)
    students.append(defaults)

def data_entry_loop():
    details = prompt(students)
    if details:
        push_to_array(**details)
        print(f"Now we have {len(students)} student." if len(students) == 1 else f"Now we have {len(students)} students.")
        while True:
            details = prompt(students)
            if details:
                push_to_array(**details)
                print(f"Now we have {len(students)} student." if len(students) == 1 else f"Now we have {len(students)} students.")
            else:
                break

def show_students():
    print_header()
    print_students_list()
    print_footer()

def print_header():
    print("\nThe students of Villains Academy")
    print("-------------")

def print_students_list():
    for index, student in enumerate(students):
        print(f"{index + 1}. {student['firstname']} ({student['cohort']} cohort)")

def print_footer():
    print(f"Overall, we have {len(students)} great students.")

initial_load_students()

interactive_menu()
