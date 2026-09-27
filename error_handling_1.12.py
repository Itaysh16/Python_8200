try:
    num = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number. Please enter an integer.")
else:
    print(f"You entered the number: {num}")
finally:
    print("Execution completed.")

"""
My mission is to add error handling to the following code that I took from
temp_converter_1.1.py:
"""
try:
    
    # 1. קבלת קלט מהמשתמש כמחרוז והמרתו למספר עשרוני
    celsius_str =float(input("הכנס טמפרטורה במעלות צלזיוס: "))


    # 3. חישוב הטמפרטורה בפרנהייט
    fahrenheit = celsius_str * 1.8 + 32
    
    # 4. עיגול התוצאה לשתי ספרות עשרוניות
    fahrenheit_rounded = round(fahrenheit, 2)
    
    # 5. הדפסת התוצאה
    print(f"{celsius_str}°C שווים ל-{fahrenheit_rounded}°F")

    with open("temps.txt", "r") as f:
            data = f.read()
            
    ratio = celsius_str / 0

except ValueError:
    # קוד שירוץ אם המשתמש הקליד טקסט שלא ניתן להמיר למספר
    print("שגיאה: הקלט שהוזן אינו מספר תקין.")

except FileNotFoundError:
    print("Error: The file 'temps.txt' was not found.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")

