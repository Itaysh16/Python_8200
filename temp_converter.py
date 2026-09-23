# 1. קבלת קלט מהמשתמש כמחרוזת
celsius_str = input("הכנס טמפרטורה במעלות צלזיוס: ")

try:
    # 2. המרת המחרוזת למספר עשרוני
    celsius = float(celsius_str)
    
    # 3. חישוב הטמפרטורה בפרנהייט
    fahrenheit = celsius * 1.8 + 32
    
    # 4. עיגול התוצאה לשתי ספרות עשרוניות
    fahrenheit_rounded = round(fahrenheit, 2)
    
    # 5. הדפסת התוצאה
    print(f"{celsius}°C שווים ל-{fahrenheit_rounded}°F")

except ValueError:
    # קוד שירוץ אם המשתמש הקליד טקסט שלא ניתן להמיר למספר
    print("שגיאה: הקלט שהוזן אינו מספר תקין.")


# 1. לקבל מהמשתמש מחיר של מוצר בש"ח
price_str = input("Enter the product's price in shekalim: ")

try:
    price = float(price_str)
    total_price = price * 1.18
    total_price_rounded = round(total_price, 2)
    print(f"The price with VAT is: {total_price_rounded}")
    print(type(total_price_rounded))

except ValueError:
    print("The input isn't correct")