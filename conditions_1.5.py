def is_leap_nested(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_leap_inline(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# בדיקת הפונקציות
years_to_test = [2024, 1900, 2000, 2023]

for y in years_to_test:
    print(f"{y}: Nested -> {is_leap_nested(y)} | Inline -> {is_leap_inline(y)}")
