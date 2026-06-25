###### Part 1 - Exception Handling ######
## What happens without it ##
'''def divide(a, b):
    return a/b
print(divide(5,0))'''

#### try/except - the core pattern ####
'''def divide(a, b):
    try:
        return a/b 
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None 
    
print(divide(10,2))
print(divide(5,0))'''

#### Multiple except blocks ####
'''def process_input(value):
    try:
        number = int(value)
        result = 100 / number 
        return result 
    except ValueError:
        return f"'{value}' is not a valid number"
    except ZeroDivisionError:
        return f"'{value}' Cannot divide by zero"

print(process_input("20"))
print(process_input("abc"))
print(process_input("0"))'''

#### else and finally ####
'''def read_age(value):
    try:
        age = int(value)
    except ValueError:
        print("Invalid input - not a number")
    else:
        # runs ONLY if try succeeded - no exception
        print(f"Valid age: {age}")
    finally:
        # runs ALWAYS - whether exception happened or not
        print("Processing complete")
read_age("5")
read_age("abc")'''

#### raise - throw your own exceptions ####
'''def set_balance(amount):
    if amount < 0:
        raise ValueError(f"Balance cannot be negative: {amount}")
    return amount 
try:
    print(set_balance(-500))
except ValueError as e:
    print(f"Caught error: {e}")'''

#### Custom exceptions - professional  pattern ####
'''class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance 
        self.amount = amount 
        super().__init__(f"Cannot withdraw {amount}. Balance is only {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount 

try:
    print(withdraw(500, 1000))
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")'''



###### Part 2 - File Handling ######
#### Reading and Writing files ####
'''# Writing a file
with open("notes.txt", "w") as f:
    f.write("Day 5 notes\n")
    f.write("Exception handling\n")

# Appending the date without erasing the file
with open("notes.txt", "a") as f:
    f.write("notes\n")

#Reading a file
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

#Reading line by line
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())

#### Handling missing files ####
def read_file(filename):
    try:
        with open(filename,"r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"file '{filename}' not found")
        return None

content = read_file("notes.txt")
print(content)'''

###### JSON Handling ######
#### JSON - the language of APIs ####
'''import json 

#Python dict -> JSON string (serialization)
student = {
    "name": "Ali",
    "marks": 88,
    "subjects": ["Maths", "AI", "Physics"],
    "passed": True
}

json_string = json.dumps(student, indent=2)
print(json_string)

# JSON string -> Python dict (deserialization)
json_string = '{"name": "Ali", "marks": 88}'
data = json.loads(json_string)
print(data["name"])
print(type(data))'''


# Write dict to JSON file
'''def save_data(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Error saving: {e}")

# Read JSON file back to dict
def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"file '{filename}' not found - returning empty dict")
        return {}
    except json.JSONDecodeError:
        print(f"{filename} is not valid JSON")
        return {}'''
    
'''students = '[{"name": "Ali", "marks": 88},{"name": "Sara", "marks": 95}]'

save_data("student.json", students)
loaded = load_data("student.json")
print(loaded)

s = json.loads(students)
print(s)'''

import json
#### DAY 5 exercise ####
# 1. add_student(filename, name, marks, subject)
#    - loads existing data from file (empty list if file missing)
#    - appends new student dict
#    - saves back to file
#    - raises ValueError if marks not between 0-100

# 2. get_all_students(filename)
#    - loads and returns all students from file
#    - handles FileNotFoundError and JSONDecodeError

# 3. get_topper(filename)
#    - returns the student with highest marks
#    - handles empty list case

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} return {result}")
        return result 
    return wrapper

def load_students(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

@log_call 
def add_student(filename, name, marks, subject):
    if marks < 0 or marks > 100:
        raise ValueError(f"Marks should not between 1 to 100")
    
    students = load_students(filename)

    new_student = {"name":name, "marks": marks, "subject": subject}
    students.append(new_student)

    with open(filename, "w") as f:
        json.dump(students, f, indent=2)

    print(f"Added {name} to {filename}")

def get_all_students(filename):
    return load_students(filename)

def get_topper(filename):
    return max(load_students(filename), key=lambda s:s["marks"])

def get_passing_students(filename):
    students = load_students(filename)
    for s in students:
        if s["marks"] >= 75:
            yield s

# Test it like this:
# add_student("students.json", "Ali",   88, "Math")
# add_student("students.json", "Sara",  95, "Physics")
# add_student("students.json", "Bilal", 72, "AI")

students = get_all_students("students.json")
for s in students:
    print(s)

topper = get_topper("students.json")
print(f"Topper: {topper['name']} with {topper['marks']}")

# This should raise ValueError:
add_student("students.json", "Zara", 80, "AI")
add_student("students.json", "Zara", 55, "AI")


for student in get_passing_students("students.json"):
    print(f"who is having more than 75: {student}")

# To delete the file data
'''import os
if os.path.exists("students.json"):
    os.remove("students.json")'''