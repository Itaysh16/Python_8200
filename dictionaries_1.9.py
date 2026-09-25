# פונקציית עזר שמקבלת זוג של (מילה, כמות) ומחזירה רק את הכמות (באינדקס 1)
def get_count(item):
    return item[1]


def count_words_dict(text):
    # 1. הפיכת כל הטקסט לאותיות קטנות
    clean_text = text.lower()

    # 2. פירוק הטקסט לרשימה של מילים לפי רווחים
    words = clean_text.split()

    # 3. יצירת מילון ריק לשמירת השכיחויות
    word_counts = {}

    # 4. ספירת כל מילה במילון
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # 5. הוצאת כל זוגות (מילה, כמות) מתוך המילון
    items_list = word_counts.items()

    # 6. מיון הזוגות מהגדול לקטן לפי הכמות
    sorted_items = sorted(items_list, key=get_count, reverse=True)

    # 7. חיתוך של 10 האיברים הראשונים בלבד
    top_10 = sorted_items[:10]

    # 8. הדפסת התוצאות
    print("--- 10 המילים הנפוצות ביותר ---")
    for word, count in top_10:
        print(f"{word}: {count}")

    return top_10

# --- טקסט ניסיוני להרצה ---
sample_text = """
Python is an amazing programming language. Python is easy to learn and Python is powerful.
In 8200, Python is widely used for networking, automation, and data analysis.
Learning Python step by step will make you a better programmer.
"""

# קריאה לפונקציה להרצה
count_words_dict(sample_text)


from collections import Counter 

def count_words_counter(text):
    words = text.lower().split()
    counts = Counter(words)
    top_10 = counts.most_common(10)
    print("--- 10 המילים הנפוצות ביותר (Counter)----")
    for word, count in top_10:
        print(f"{word}: {count}")

# --- טקסט ניסיוני חדש ---
cyber_text = """
Network security is critical for protecting data. A secure network prevents unauthorized access.
Security teams monitor network traffic every day. Good security practice keeps data safe and network reliable.
"""

# קריאה לפונקציה
count_words_counter(cyber_text)
print()
print()

# --- תרגיל ב': ספר טלפונים כמילון מקונן ---

def add_contact(phonebook, name, phone, email, address):
    # הוספה או עדכון של מילון פנימי תחת המפתח של השם
    phonebook[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"✓ Contact '{name}' added successfully.")


def search_contact(phonebook, name):
    # שליפת הפרטים בצורה בטוחה בעזרת .get כדי למנוע קריסה
    contact = phonebook.get(name)
    
    if contact:
        print(f"\n--- Contact Info: {name} ---")
        print(f"Phone:   {contact['phone']}")
        print(f"Email:   {contact['email']}")
        print(f"Address: {contact['address']}")
        return contact
    else:
        print(f"\n✗ Contact '{name}' not found.")
        return None


def delete_contact(phonebook, name):
    # בדיקה אם המפתח קיים לפני המחיקה
    if name in phonebook:
        del phonebook[name]
        print(f"\n✓ Contact '{name}' deleted successfully.")
    else:
        print(f"\n✗ Cannot delete: '{name}' not found.")


# --- דוגמת הרצה ---
my_phonebook = {}

# 1. הוספת אנשי קשר
add_contact(my_phonebook, "Itay", "050-1234567", "itay@gmail.com", "Tel Aviv")
add_contact(my_phonebook, "Noam", "052-9876543", "noam@gmail.com", "Haifa")

# 2. חיפוש איש קשר קיים ושאינו קיים
search_contact(my_phonebook, "Itay")
search_contact(my_phonebook, "David")

# 3. מחיקת איש קשר
delete_contact(my_phonebook, "Noam")

# 4. בדיקה מחדש לאחר מחיקה
search_contact(my_phonebook, "Noam")