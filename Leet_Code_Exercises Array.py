#Exercise 1: Remove Elements
print("Exercise 1: Remove Elements")
def removeElement(nums: list[int], val: int) -> int:
    k = 0  # מונה שמציין את המקום הפנוי הבא בתחילת הרשימה
    
    for num in nums:
        # אם המספר שונה מהערך שצריך למחוק
        if num != val:
            nums[k] = num  # שמים אותו במקום הפנוי הבא
            k += 1         # מקדמים את המונה
            
    return k  # מחזירים כמה מספרים תקינים נשארו

# --- אזור ההרצה וההדפסות ---
# דוגמה: רשימה עם מספרים, כולל הערך שיש למחוק
nums_list_1 = [3, 2, 2, 3, 4, 6, 3, 8, 19, 34, 3, 5, 7, 5]
val_1 = 3
k_1 = removeElement(nums_list_1, val_1)
print(f"Original list: {nums_list_1}")
print(f"Number of elements after removal: {k_1}\n")


#Exercise 2: Search Insert Position
print("Exercise 2: Search Insert Position")
def searchInsert(nums: list[int], target: int) -> int:
    # עוברים על כל האינדקסים והערכים ברשימה בעזרת enumerate
    for i, num in enumerate(nums):
        # אם מצאנו מספר שגדול או שווה ל-target, זה בדיוק האינדקס שלו!
        if num >= target:
            return i
            
    # אם הלולאה סיימה לעבור על הכל וכל המספרים היו קטנים מה-target,
    # סימן שהוא צריך להיכנס בסוף הרשימה
    return len(nums)

# --- אזור ההרצה וההדפסות ---
# דוגמה 1: רשימה ממוינת, מחפשים את המיקום
nums_list_2 = [1, 3, 5, 6]
target_1 = 5
k_2 = searchInsert(nums_list_2, target_1)
print(f"Original list: {nums_list_2}")
print(f"Target: {target_1}")
print(f"Insert position: {k_2}")

# דוגמה 2: רשימה ממוינת, מחפשים את המיקום של מספר שלא קיים ברשימה
nums_list_3 = [1, 3, 5, 6]
target_2 = 2
k_3 = searchInsert(nums_list_3, target_2)
print(f"Original list: {nums_list_3}")
print(f"Target: {target_2}")
print(f"Insert position: {k_3}\n")


#Exercise 3: Plus One
print("Exercise 3: Plus One")
def plusOne(digits: list[int]) -> list[int]:
    # 1. הופכים את רשימת הספרות למחרוזת, מחברים הכל, וממירים למספר שלם
    num = int("".join(map(str, digits)))
    
    # 2. מוסיפים 1
    num += 1
    
    # 3. הופכים את המספר החדש חזרה למחרוזת, וממירים כל תווית לספרה בתוך רשימה
    return [int(char) for char in str(num)]

# --- אזור ההרצה וההדפסות ---
# דוגמה: רשימת ספרות שמייצגת את המספר 123
digits_list_1 = [1, 2, 3]
result_1 = plusOne(digits_list_1)
print(f"Original list: {digits_list_1}")
print(f"Result: {result_1}")

#דוגמא 2: רשימת ספרות שמייצגת את המספר 999
digits_list_2 = [9, 9, 9]
result_2 = plusOne(digits_list_2)
print(f"Original list: {digits_list_2}")
print(f"Result: {result_2}\n")