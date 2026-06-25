###### Day 6 — Decorators, Generators, Context Managers ######
#### Part 1 - Generators ####

'''# any() function 
students = [{"name": "Ali"}, {"name":"Sara"}]
result_any = any(s["name"] == "Sara" for s in students)
print(result_any)

# List comprehensions - build the WHOLE list first
result_list = [s["name"] == "Sara" for s in students] # fully computed
print(result_list)
# [False, True]

# Generator expression - produces values on at a time, lazily
result_gen = (s["name"] == "Sara" for s in students) # generator - nothing computed yet
print(result_gen)
# <generator object <genexpr> at 0x000001CE60DE8380>'''

# The problem generators solve - The wastes of massive memory
'''def get_square(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result 
squares = get_square(100000000)
for sq in squares:
    print(sq)
    if sq >= 20:
        break
print(squares)'''

#The generator solution
'''def get_square(n):
    for i in range(n):
        yield i * i 

squares = get_square(100)

for sq in squares:
    print(sq)
    if sq >= 20:
        print(sq)
        break'''

# Seeing it step by step
'''def count_up_to(n):
    i = 1 
    while i<=n:
        print(f"About to yield {i}")
        yield i 
        i += 1 
gen = count_up_to(3)
print(next(gen))'''






#### Part 2 - Decorators ####
# The problem decorators solve 
# Imagine you want to time how long several functions take to run
'''import time 
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper 
# slow_function = timer(slow_function)
# slow_function()

@timer
def slow_function():
    time.sleep(1)
    print("Done")
slow_function()'''

#second example
'''import time
def logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} returned {result}, took seconds: {end - start:.15f}")
        return result 
    return wrapper

@logger
def add(a, b):
    time.sleep(1)
    print("Done")
add(3, 5)'''

#### Part 3 - Context Manager #### 

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename 
        self.mode = mode 

    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file 
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing {self.filename}")
        self.file.close() 
        
filename = "notes.txt"
with FileManager(filename, "w") as f:
    f.write("Hello from custom context manager")
    print("wrote into a file '{filename}'")

with FileManager("notes.txt", "r") as f:
    content = f.read()
    print(content)

from contextlib import contextmanager 

@contextmanager
def file_manager(filename, mode):
    print(f"Opening {filename}")
    f = open(filename, mode)
    yield f 
    print(f"Closing {filename}")
    f.close()

with file_manager("notes.txt", "w") as f:
    f.write("Hello again")

with file_manager("notes.txt", "r") as f:
    content = f.read()
    print(content)