class Student:
    def __init__(self, grade):
        self.grade = grade
        print("This is a Student class.")
student1 = Student("A")
print(f"Student grade: {student1.grade}")