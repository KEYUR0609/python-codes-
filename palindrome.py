text = input("Enter a string: ")

# Reverse the string
rev = text[::-1]

# Check palindrome
if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
