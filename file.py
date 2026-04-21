FILENAME = "students.txt"

# ---- Add Student ----
def add_student():
    with open(FILENAME, "a") as f:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        f.write(roll + "," + name + "," + marks + "\n")
    print("Student Added Successfully\n")


# ---- View Students ----
def view_students():
    if not os.path.exists(FILENAME):
        print("No records found\n")
        return
    
    with open(FILENAME, "r") as f:
        print
