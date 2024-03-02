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