import re

def first_letter(x):
    x = str(x)
    pattern = r"[A-Z]"
    if re.match(pattern, x[0]):
        print(x[0])
    else:
        print("Your name should start with capital letters")

#name = input("Enter your name: ")
       
       
def tel_number(y):
    while len(y) > 12:
        print("Enter a valid number")
    pattern = r'[0-9]'
    if re.match(pattern, y):
        print(y)
    else:
        print("Number is not valid")
        
number = input("Enter your telephone number")

tel_number(number)
        