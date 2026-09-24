def remove_duplicates(lst):
    special_list = []
    for item in lst:
        if item not in special_list:
            special_list.append(item)
    return special_list
# בדיקה לראות אם זה עובד
numbers = [1, 2, 2, 3, 4, 4, 4, 1, 5]
print(remove_duplicates(numbers))



def transpose(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    transposed = []
    
    # 1. עוברים עמודה-עמודה במטריצה המקורית
    for col in range(num_cols):
        new_row = []
        # 2. לכל עמודה, עוברים על כל השורות ואוספים את האיבר
        for row in range(num_rows):
            new_row.append(matrix[row][col])
        
        # 3. מוסיפים את השורה החדשה למטריצה המשוחלפת
        transposed.append(new_row)
        
    return transposed


# בדיקה:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose(matrix))
# פלט צפוי: [[1, 4], [2, 5], [3, 6]]


a = [1, 2]
b = a
b.append(3)

print(f"a: {a}") # output is: a: [1, 2, 3]
print(f"b: {b}") # output is: b: [1, 2, 3]
# The output of a and b is the same because both are pointing to the same memory so if you append one of them with the number 3 it will be reflected in the other one as well.






