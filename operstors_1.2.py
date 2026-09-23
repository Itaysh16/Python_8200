# ==========================================
# חלק א': פונקציה לבדיקת מספר ראשוני
# ==========================================

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# בדיקת הפונקציה
print("Is 7 prime?", is_prime(7))    # True
print("Is 10 prime?", is_prime(10))  # False
print("Is 1 prime?", is_prime(1))    # False

print("-" * 30)

# ==========================================
# חלק ב': הבדל בין == ל-is
# ==========================================

a = [1, 2]
b = [1, 2]

print("a == b:", a == b)  # True  - כי הערכים בתוך הרשימות זהים
print("a is b:", a is b)  # False - כי אלו שני אובייקטים נפרדים בכתובות זיכרון שונות

# הוכחה: הדפסת כתובות הזיכרון (id) של שני המשתנים
print("Memory address of a:", id(a))
print("Memory address of b:", id(b))

num = 20
numbers = [10,20,30,40]
if num % 2 == 0 and num % 5 == 0 and num in numbers:
    print("valid number")
else:
    print("invalid")