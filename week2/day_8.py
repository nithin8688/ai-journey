###### Async programming deep dive ######
#### Part 1 - sync vs async, side by side ####

## Sync ##
import time
import asyncio
'''
def make_chai(cup_number):
    print(f"Starting Cup {cup_number}")
    time.sleep(2)
    print(f"Cup {cup_number} ready")

def sync_main():
    start = time.time()
    make_chai(1)
    make_chai(2)
    make_chai(3)
    print(f"Total time: {time.time() - start:.2f}s")
sync_main()

## Async ##
async def make_chai(cup_number):
    print(f"Starting cup {cup_number}")
    await asyncio.sleep(2)
    print(f"Cup is ready {cup_number}")

async def async_main():
    start = time.time()
    await asyncio.gather(
        make_chai(1),
        make_chai(2),
        make_chai(3),
    )
    print(f"Total time: {time.time() - start:.2f}s")
asyncio.run(async_main())'''


#### Part 2 - the keywords, one by one #### 
## async def ##
'''async def greet():
    return "Hello"
# # Wrong - this doesn't run the function 
# result = greet()  # <coroutine object greet at 0x...> - not "Hello"
# print(result)

# #Right 
result = asyncio.run(greet())
print(result) # Hello

## await ## 
async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(1) # pause here, let others run 
    print("Done")
    return {"data": 42}

## asyncio.gather() # To run multiple coroutines concurrently, wait for all to finish
async def main():
    result = await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data(),
    )
    print(result)
## asyncio.run # The entry point. Starts the event loop and runs one top-level coroutine.
asyncio.run(main())'''

#### Part 3 - the event loop (what's actually happening) #### 
'''Event Loop = the chai wala

Coroutines = cups of chai being made

await = "I'm waiting for water to boil — take me off the burner 
         and put someone else on"

asyncio.gather() = "start all these cups at the same time"'''

#### Part 4 - real use case: fetching multiple URLs #### 
import aiohttp

'''async def fetch_url(session, url):
    async with session.get(url) as response:
        data = await response.json()
        print(f"Got response from {url}")
        return data 
async def fetch_all():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
    ]
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[fetch_url(session, url) for url in urls]
        )
    return results 
results = asyncio.run(fetch_all())
for r in results:
    print(r["title"])'''

#### Part 5 - async with context managers #### 
'''async def read_file_async():
    async with aiofiles.open("notes2.txt", "r") as f:
        content = await f.read()
    return content 

async def stream_data():
    async for chunk in some_async_stream:
        process(chunk)'''

async def fetch_student(student_id):
    print(f"Start to fetch student id_{student_id}")
    await asyncio.sleep(1) 
    return {"id": student_id, "name": f"Student_{student_id}", "marks": student_id * 10}

async def fetch_all_students(ids):
    results = await asyncio.gather(
        *[fetch_student(i) for i in ids]
    )
    return results
     
async def main():
    start = time.time()
    students = await fetch_all_students(range(1,6))
    for student in students:
        print(student)
    print(f"Total time: {time.time() - start:.2f}")
    
asyncio.run(main())