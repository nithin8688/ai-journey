'''def greet(name):
    message = f"Good morning, {name}"
    return message
result = greet("Nithin")
# print(result)
'''
'''
def make_chai(cups, sugar=1):
    print(f"Making {cups} cups, {sugar} spoons of sugar")
# make_chai()
make_chai(2)
make_chai(2,3)
'''
'''
def register(name, age, city):
    print(f"{name} | {age} | {city}")
register("nithin", 19, "GRP")
register(name="vinod", city="BLR", age=23)
register("nithin", city="Delhi", age=23)
'''
'''
def total_marks(*subjects):
    print(type(subjects))
    return sum(subjects)
print(total_marks(85,90,99))
print(total_marks(89,34,23,45,56,76))
'''
'''
def log_events(*events):
    for e in events:
        print(f"[LOG] {e}")
log_events("LOG", "File upload", "Email sent")
'''
'''
def create_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
create_profile(name="Nithin", age="23", city="Delhi", role="AI Engineer")'''

'''
def build_ai_model(model_name, version, *layers, **hyperparams):
    print(f"Model: {model_name} v{version}")
    print(f"Layers: {layers}")
    print(f"Config: {hyperparams}")
build_ai_model("ConvNexTiny", 2, 24,32,64,128, lr=0.001, dropout=0.3)'''

'''
score =100
def update():
    score = 999
    print(score) 
update()
print(score)

score = 100 
def update():
    global score
    score = 999 
update()
print(score)'''

'''
def square(n):
    return n * n 
squaree = lambda n : n * n
print(square(5))
print(squaree(6))'''
'''
students = [
    {"name": "Ali", "marks": 88},
    {"name": "Sara", "marks": 95},
    {"name": "Bilal", "marks": 72}
]
ranked = sorted(students, key=lambda s:s["marks"], reverse=True)
for s in ranked:
    print(s["name"], "-", s["marks"])

def student(*marks):
    print(sum(marks))
student(23,34,45,56,67)
'''
def student_report(name, *subjects, grade="Not graded", **details):
    print(f"{'='*10} Student Report {'='*10}")
    print(f"Name       :{name}")
    print(f"Grade      :{grade}")
    print(f"Subjects   :{', '.join(subjects)}")
    print(f"Details:")
    for key, value in details.items():
        print(f" {key}: {value}")
    print(f"{'='*36}")
student_report("Sara", "Math", "Physics", "AI", city= "Delhi", goal="AI Engineer", year= 2)

