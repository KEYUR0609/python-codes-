def add(a, b):
    print("Addition =", a + b)

def sub(a, b):
    print("Subtraction =", a - b)

def mul(a, b):
    print("Multiplication =", a * b)

def div(a, b):
    if b != 0:
        print("Division =", a / b)
    else:
        print("Division not possible")

# Main Program
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice: "))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if choice == 1:
    add(x, y)
elif choice == 2:
    sub(x, y)
elif choice == 3:
    mul(x, y)
elif choice == 4:
    div(x, y)
else:
    print("Invalid choice")
