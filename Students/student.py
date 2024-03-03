import json

# This class represents a single student
class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade


    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"

 

# This class represents a student managment system
class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = self.load_students()


    # This method loads students from a JSON file
    def load_students(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON. File might be corrupt.")
            return []


    # This method saves students to a JSON file
    def save_students(self):
        with open(self.filename, 'w') as file:
            json.dump(self.students, file, indent=4)

    
    # Add a new student to the list
    def add_student(self, student):
        # Check if roll number and grade are positive numbers
        if student.roll_number < 0 or student.grade < 0:
            print('Roll number and grade must be positive numbers!')
            return
        
        # Check if the roll number already exists
        for existing_student in self.students:
            if existing_student['roll_number'] == student.roll_number:
                print(f"Student with roll number {student.roll_number} already exists.")
                return 

        # Append new student to the list and save to file
        self.students.append({'name': student.name, 'roll_number': student.roll_number, 'grade': student.grade})
        self.save_students()
        print(f"Student {student.name} added successfully.")


    # Display information of all students
    def see_all_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Grade: {student['grade']}")


    # Find a student by roll number
    def find_student(self, number):
        for student in self.students:
            if student['roll_number'] == number:
                return f"Name: {student['name']}, Roll Number: {student['roll_number']}, Grade: {student['grade']}"
                    
        return f"This student is not in the list!"
        

    # Change the grade of a student
    def change_grade(self, number, new_grade):
        # Loop through students to find the one with the given roll number
        for student in self.students:
            if student['roll_number'] == number:
                student['grade'] = new_grade
                self.save_students()
                print("Grade updated successfully")
                return
        print("Student not found")