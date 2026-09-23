print(f"{'*':>4}", end=" |")

for i in range(1,11):
    print(f"{i:>4}", end="")
print()
print("-----+", end="")
print("-" * 40)

for row in range(1, 11):
    print(f"{row:>4}", end=" | ")
    for col in range(1, 11):
        print(f"{row*col:>4}", end="")
    print()
# תווי בריחה
print("Line 1\nLine 2\tIndented \\")
print(r"C:\Users\net\new_folder")
