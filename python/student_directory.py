import csv
import sys

class Student():
    def __init__(self, firstname, surname, birthplace, cohort):
        self.firstname = firstname
        self.surname = surname
        self.birthplace = birthplace
        self.cohort = cohort

class StudentBody():
    def __init__(self):
        self.list = []
    
    def current_num(self):
        return len(self.list)
    
    def add_student(self, student):
        self.list.append(student)   

class Interface():
    def __init__(self):
        pass

    @staticmethod
    def selection_menu():
        print("1. Input the students")
        print("2. Show the students")
        print("3. Save the list to a csv file")
        print("4. Load the list from a csv file")
        print("9. Exit")
        selection = input().strip()
        return selection
    
    @staticmethod
    def feedback_message(operation):
        print("\v" + operation.upper() + " SUCCESSFULLY!\v")

    @staticmethod 
    def get_student_data():
        print("Please enter the first name, last name, birthplace and cohort of each student.")

        firstname = input("Enter first name: ")
        if firstname == "":
            return None

        surname = input("Enter surname: ")
        if surname == "":
            return None

        birthplace = input("Enter birthplace: ")
        if birthplace == "":
            return None

        cohort = input("Enter cohort: ")
        if cohort == "":
            return None
        return Student(firstname, surname, birthplace, cohort)
    
    @staticmethod 
    def add_students_to_body(student_body):
        while True:
            enter = input("Hit enter to exit or \"-\" to enter (a)nother student.\n")
            if enter:
                new_student = Interface.get_student_data()
                if new_student:
                    student_body.add_student(new_student)
                    print(f"Now we have {student_body.current_num()} student." if student_body.current_num() == 1 else f"Now we have {student_body.current_num()} students.")
            else:
                break 
        Interface.feedback_message("data entered")

    @staticmethod
    def show_students(student_body):
        if student_body.current_num() > 0:
            print("\nThe students of Villains Academy")
            print("-------------")
            for index, student in enumerate(student_body.list):
                print(f"{index + 1}. {student.firstname} ({student.cohort} cohort)")
            print(f"Overall, we have {student_body.current_num()} great students.")
            Interface.feedback_message("data printed")
        else:
            print("There are currently no students in the system to display.")

    @staticmethod
    def save_students(student_body):
        filename = input("Please enter the filename (inc. extension) in which you'd like to save the data: ")
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for student in student_body.list:
                writer.writerow([student.firstname, student.surname, student.birthplace, student.cohort])
        Interface.feedback_message("data saved")

    @staticmethod
    def load_students(student_body):
        filename = input("Please enter the filename (inc. extension) that you'd like to load: ")
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(firstname=row[0], surname=row[1], birthplace=row[2], cohort=row[3])
                student_body.add_student(student)
        Interface.feedback_message("data loaded")

    @staticmethod
    def run_programme():
        student_body = StudentBody()
        actions = {
            "1": Interface.add_students_to_body,
            "2": Interface.show_students,
            "3": Interface.save_students,
            "4": Interface.load_students,
            "9": sys.exit, # this will cause the program to terminate
        }
        while True:
            selection = Interface.selection_menu()
            if selection in actions:
                actions[selection](student_body)
            else: 
                print("I don't know what you mean. Try again!")

Interface.run_programme() # first thing to happen

# def run_programme():
#     student_body = StudentBody()
#     while True:
#         selection = Interface.selection_menu()
#         if selection == "1":
#             Interface.add_students_to_body(student_body)
#         elif selection == "2":
#             Interface.show_students(student_body)
#         elif selection == "3":
#             Interface.save_students(student_body)
#         elif selection == "4":
#             Interface.load_students(student_body)
#         elif selection == "9":
#             sys.exit()  # this will cause the program to terminate
#         else:
#             print("I don't know what you mean. Try again!")