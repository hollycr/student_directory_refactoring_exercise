import csv
import sys

class Student():
    def __init__(self, firstname, surname, birthplace, cohort):
        self.firstname = firstname
        self.surname = surname
        self.birthplace = birthplace
        self.cohort = cohort
    
    @classmethod
    def from_user_input(cls):
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
        
        return cls(firstname, surname, birthplace, cohort)

class StudentBody():
    def __init__(self):
        self.list = []
    
    def current_num(self):
        return len(self.list)
    
    def add_students(self):
        while True:
            enter = input("Hit enter to exit or \"-\" to enter (a)nother student.\n")
            if enter:
                new_student = Student.from_user_input()
                if new_student:
                    self.list.append(new_student)
                    print(f"Now we have {student_body.current_num()} student." if student_body.current_num() == 1 else f"Now we have {student_body.current_num()} students.")
            else:
                break    
    
    def show_students(self):
        print("\nThe students of Villains Academy")
        print("-------------")
        for index, student in enumerate(student_body.list):
            print(f"{index + 1}. {student.firstname} ({student.cohort} cohort)")
        print(f"Overall, we have {student_body.current_num()} great students.")

    def save_students(self):
        filename = input("Please enter the filename (inc. extension) in which you'd like to save the data: ")
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for student in self.list:
                writer.writerow([student.firstname, student.surname, student.birthplace, student.cohort])

    def load_students(self):
        filename = input("Please enter the filename (inc. extension) that you'd like to load: ")
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                student = Student(firstname=row[0], surname=row[1], birthplace=row[2], cohort=row[3])
                self.list.append(student)

student_body = StudentBody()

def interactive_menu():
    while True:
        print("1. Input the students")
        print("2. Show the students")
        print("3. Save the list to a csv file")
        print("4. Load the list from a csv file")
        print("9. Exit")
        selection = input().strip()
        if selection == "1":
            student_body.add_students()
            feedback_message("data entered")
        elif selection == "2":
            if student_body.current_num() > 0:
                student_body.show_students()
                feedback_message("data printed")
            else:
                print("There are currently no students in the system to display.")
        elif selection == "3":
            student_body.save_students()
            feedback_message("data saved")
        elif selection == "4":
            student_body.load_students()
            feedback_message("data loaded")
        elif selection == "9":
            sys.exit()  # this will cause the program to terminate
        else:
            print("I don't know what you mean. Try again!")

def feedback_message(operation):
    print("\v" + operation.upper() + " SUCCESSFULLY!\v")

interactive_menu() # first thing to happen