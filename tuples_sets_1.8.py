list1 = ["alice", "bob", "charlie", "dave", "eve"]
list2 = ["charlie", "eve", "frank", "grace", "bob"]

set1 = set(list1)
set2 = set(list2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)


large_list = list(range(1000000))
large_set = set(large_list)
import time

# 1. שומרים את נקודת ההתחלה
start = time.perf_counter()

# 2. הרצת הקוד שרוצים למדוד (למשל: חיפוש ברשימה)
result = 999999 in large_list

# 3. שומרים את נקודת הסיום
end = time.perf_counter()

# 4. מחשבים את ההפרש
elapsed_time1 = end - start
print(f"Time taken: {elapsed_time1:.6f} seconds")


import time

# 1. שומרים את נקודת ההתחלה
start = time.perf_counter()

# 2. הרצת הקוד שרוצים למדוד (למשל: חיפוש ברשימה)
result = 999999 in large_set

# 3. שומרים את נקודת הסיום
end = time.perf_counter()

# 4. מחשבים את ההפרש
elapsed_time2 = end - start
print(f"Time taken: {elapsed_time2:.6f} seconds")

print(f"The time difference is: {elapsed_time1 - elapsed_time2:.6f} seconds")