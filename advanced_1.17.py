# Exercise 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doubled_numbers = lambda numbers: [x * 2 for x in numbers]
print(f"Doubled numbers: {doubled_numbers(numbers)}")
# another way to do it is to use the map function
doubled_numbers_map = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers (using map): {doubled_numbers_map}")

divided_numbers = list(filter(lambda x: x % 4 == 0, doubled_numbers_map))
print(f"Divided numbers: {divided_numbers}")

# Exercise 2 part 1
with open("test_log.txt","w", encoding="utf-8") as f:
    f.write("SYSTEM: Booting up sequence started.\n")
    f.write("INFO: All systems operational.\n")
    f.write("ERROR: Connection timeout detected on port 8080.\n")
    f.write("WARNING: Memory usage is reaching 85%.\n")
    f.write("ERROR: Failed to write data to database.\n")
    f.write("SYSTEM: Shutting down safely.\n")

def filter_log(filename, keyword):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if keyword in line:
                yield line

check = filter_log("test_log.txt", "ERROR")
for line in check:
    print(line.strip())

# Exercise 2 part 2
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        result = func(*args, **kwargs)
        end_time = time.perf_counter()  # Stop the timer
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def time_sleep(seconds):
    time.sleep(seconds)

time_sleep(1)

# Exercise 2 part 3
import urllib.request
import threading

urls = ["https://httpbin.org/delay/1"] * 10
@timer
def sequential_download(urls):
    for url in urls:
        urllib.request.urlopen(url).read()
@timer
def multi_threaded_download(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=urllib.request.urlopen, args=(url,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()




