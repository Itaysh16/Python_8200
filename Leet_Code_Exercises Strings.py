#Exercise 1: Longest Common Prefix
print("Exercise 1: Longest Common Prefix")
def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
        
    for i, char in enumerate(strs[0]):
        for other_word in strs[1:]:
            # אם חורגים מאורך המילה האחרת, או שהאותיות לא תואמות - עוצרים
            if i >= len(other_word) or other_word[i] != char:
                return strs[0][:i]
                
    return strs[0]


# --- אזור ההרצה וההדפסות ---

# דוגמה 1: רשימה עם קידומת משותפת
words_list_1 = ["flower", "flow", "flight"]
result_1 = longestCommonPrefix(words_list_1)

print("--- First Test: ---")
print(f"Words list: {words_list_1}")
print(f"Result: '{result_1}'\n")


# דוגמה 2: רשימה שאין ביניהן שום דבר משותף בהתחלה
words_list_2 = ["dog", "racecar", "car"]
result_2 = longestCommonPrefix(words_list_2)

print("--- Second Test: ---")
print(f"Words list: {words_list_2}")
print(f"Result: '{result_2}' (Empty string expected)\n")


#Exercise 2: Find the Index of the First Occurrence in a String
print("Exercise 2: Find the Index of the First Occurrence in a String")
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# --- אזור ההרצה וההדפסות ---
haystack_1 = "Tanki Online"
needle_1 = "ki On"

result_3 = strStr(haystack_1, needle_1)

print("--- Third Test: ---")
print(f"Words list: {haystack_1}")
print(f"Needle: {needle_1}")
print(f"Result: {result_3}")

haystack_2 = "Tanki Online"
needle_2 = "ki Onl"
result_4 = strStr(haystack_2, needle_2)

print("--- Fourth Test: ---")
print(f"Words list: {haystack_2}")
print(f"Needle: {needle_2}")
print(f"Result: {result_4}\n")


#Exercise 3: Lenth of Last Word
print("Exercise 3: Length of Last Word")
def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])

# --- אזור ההרצה וההדפסות ---
s_1 = "Tanki Online is a great game"
result_5 = lengthOfLastWord(s_1)

print("--- Fifth Test: ---")
print(f"String: {s_1}")
print(f"Result: {result_5}\n")