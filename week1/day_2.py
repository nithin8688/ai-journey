subjects = ["Maths", "Physics", "AI"]
subjects.append("Chemistry")
subjects.insert(0, "English")
print(subjects)
subjects.remove("Maths")
print(subjects)
last = subjects.pop()
print(subjects)
print(last)

print(subjects[0])
print(subjects[-1])

print(subjects[1:2])

nums = [5,3,1,4,2]
nums.sort()
print(nums)

nums2 = [5,3,1,4,2]
sorted_copy = sorted(nums2)
print(sorted_copy)

#### Dictionaries ####
student = {
    "name": "Sara",
    "grade": "A+",
    "subjects": ["Maths", "Physics", "Chemistry"]
}

print(student)
print(student["name"])
print(student.get("age"))
print(student.get("age",19))

student["age"] = 22
print(student)
student["grade"] = "A"
print(student)
del student["age"]

print(student)
for key, value in student.items():
    print(f"{key}: {value}")

#### TUPLE ####
point = (10, 20)
x, y = point
print(point)
print(x,y)

#### SET ####
a = {1,2,3,4}
b = {3,4,5,6}

print(a | b) # union: {all}
print(a & b) # Intersection: common {3, 4}
print(a - b) # Difference {1, 2}
print(b - a)

names = ["Ali", "Sara", "Ali", "Bilal", "Sara"]
namess = set(names)
print(namess)

#### List comprehensions ####
square = []
for n in range(1,6):
    square.append(n*n)
print(square)

squ = [n for n in range(1,11) if n%2==0]
print(squ)

#### Dict Comprehension ####
students = ["Ali", "Sara", "Bilal"]
name_length = {name: len(name) for name in students}
print(name_length)

students = [
    {"name": "Ali",   "marks": 88, "subject": "Math"},
    {"name": "Sara",  "marks": 95, "subject": "Physics"},
    {"name": "Bilal", "marks": 72, "subject": "Math"},
    {"name": "Zara",  "marks": 60, "subject": "AI"},
]
## Above 75
pass_marks = [n["name"] for n in students if n["marks"] >= 75]
print(pass_marks)

##Unique set
unique_subjects = {n["subject"] for n in students}
print(unique_subjects)

#Dict comprehensions
student_name_marks = {s["name"]: s["marks"] for s in students}
print(f"name and marks: {student_name_marks}")

student_name_subject = {s["name"]: s["subject"] for s in students}
print(student_name_subject)

#Highest marks
highest_marks = max(students, key=lambda m:m["marks"])
print(highest_marks)

# 1. A function with a default arg, *args, and **kwargs
# 2. A list comprehension that filters
# 3. A set comprehension
# 4. A dict comprehension
# 5. max() with a key=lambda on a list of dicts