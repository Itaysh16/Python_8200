for i in range(1, 11):
    print (i, end=" ")
print()
for i in range(1, 11):
    if i % 2 == 0:
        print (i, end=" ")

print()

for i in range(2,11,2):
    print (i, end=" ")

print()
print()

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print("*" * i)


import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to Guess the Number!")
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("Guess a number (1-100): ")

    # 1. בדיקת יציאה
    if user_input.lower() == "exit":
        print("Thanks for playing! Goodbye.")
        break

    # 2. המרה למספר וקידום הספירה (בתוך הלולאה!)
    guess = int(user_input)
    attempts += 1

    # 3. בדיקת הניחוש
    if guess == secret_number:
        print(
            f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts."
        )
        break  # ניחשת נכון - סיימנו את המשחק!
    elif guess < secret_number:
        print("Too low! Try again.\n")
    else:
        print("Too high! Try again.\n")



# פה תבוא לולאת ה-while True שלך!
