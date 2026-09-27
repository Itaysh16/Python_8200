with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Learning python for 8200\n")
    file.write("close the file authomaticly line by line\n")
    file.write("Reading and writing datas are core capabillity\n")

print("The file created and writed successfuly")

with open("output.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())


import csv
import json

# ==========================================
# שלב 1: יצירת קובץ CSV עם אנשי קשר
# ==========================================

contacts_data = [
    ["name", "phone", "city"],
    ["Israel Israeli", "0501234567", "Tel Aviv"],
    ["Noa Kirel", "0529876543", "Jerusalem"],
    ["Yossi Cohen", "0545555555", "Tel Aviv"],
    ["Dana International", "0531111222", "Haifa"],
    ["Ron Arad", "0584443332", "Tel Aviv"]
]

# כותבים את הנתונים לקובץ contacts.csv
with open("contacts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(contacts_data)

print("שלב 1 הושלם: הקובץ contacts.csv נוצר בהצלחה!")

# ==========================================
# שלב 2: סינון אנשי הקשר וכתיבה ל-JSON
# ==========================================

filtered_contacts = []

# 1. פתיחת קובץ ה-CSV וסינון אנשי קשר מתל אביב
with open("contacts.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    # שימוש ב-List Comprehension לסנון מהיר
    filtered_contacts = [row for row in reader if row["city"] == "Tel Aviv"]

# 2. כתיבת הנתונים המסוננים לקובץ JSON
with open("filtered_contacts.json", "w", encoding="utf-8") as f:
    json.dump(filtered_contacts, f, indent=4, ensure_ascii=False)

print("שלב 2 הושלם: אנשי הקשר מתל אביב נשמרו ב-filtered_contacts.json!")

# ==========================================
# שלב 3: קריאת ה-JSON והדפסת טבלה מיושרת
# ==========================================

# 1. טעינת הנתונים מתוך קובץ ה-JSON
with open("filtered_contacts.json", "r", encoding="utf-8") as f:
    loaded_contacts = json.load(f)

# 2. הדפסת כותרת הטבלה מיושרת
print("\n--- אנשי קשר מתל אביב (נקראו מ-JSON) ---")
print(f"{'Name':<22} | {'Phone':<15} | {'City':<15}")
print("-" * 58)

# 3. הדפסת שורות הנתונים
for contact in loaded_contacts:
    print(f"{contact['name']:<22} | {contact['phone']:<15} | {contact['city']:<15}")