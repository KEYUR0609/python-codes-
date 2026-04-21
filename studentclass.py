class Student:
    def _init_(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll:", self.roll, "| Name:", self.name, "| Marks:", self.marks)

    def update_marks(self, new_marks):
        self.marks = new_marks
        print("Marks Updated Successfully\n")


# ---- List to store students ----
students = []

# ---- Add Student ----
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))
    
    s = Student(roll, name, marks
