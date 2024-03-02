from student import Student, StudentManager


def main():

    manager = StudentManager('students.json')


    # Helper function to choose an action.
    def choose_function():
        try: 
            n = int(input("Hello! This is a student management page!\n"
                          "Choose an option:\n"
                          "1. See all students\n"
                          "2. Add a new student\n"
                          "3. Change student's grade\n"
                          "4. Find a student\n"
                          "If you want to exit, press CTRL + C\n"))
            if n not in [1, 2, 3, 4]:
                raise ValueError()
            return n
        except ValueError:
            print("Please enter a valid choice (1, 2, 3, or 4)")
            return choose_function()



    while True:
        choice = choose_function()
        try:
            if choice == 1:
                manager.see_all_students()

            elif choice == 2:
                name = input("Please enter the student's name: ").strip().title()
                roll_number = int(input("Please enter the student's roll number: "))
                grade = int(input("Please enter the student's grade: ") )          
                student = Student(name, roll_number, grade)
                manager.add_student(student)

            elif choice == 3:
                student_roll_number = int(input("Please enter the student's roll number: "))
                student_new_grade = int(input("Please enter the student's new grade: "))
                manager.change_grade(student_roll_number, student_new_grade)

            elif choice == 4:
                student_roll_number = int(input("Please enter the student's roll number: "))
                print(manager.find_student(student_roll_number))
            else:
                continue
            request = input('Do you want to exit (yes/no)? ').lower().strip()
            if request in ['yes','y']:
                break
        except ValueError as e:
            print("Invalid input, please ensure you enter numerical values where required.")
        

  
    
    
if __name__ =="__main__":
    main()
