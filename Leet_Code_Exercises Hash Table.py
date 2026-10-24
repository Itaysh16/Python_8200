#Exercise 1: Two Sum
print("Exercise 1: Two Sum")
def two_sum(nums, target):
    numbers = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numbers:
            return [numbers[complement], i]
        numbers[num] = i
    return None

numbers = [2, 7, 11, 15]
target = 9
result = two_sum(numbers, target)
print(result)
print()


print("Exercise 2: Roman to Integer")

#Exercise 2: Roman to Integer
def romanToInt(s: str) -> int:
    # 1. יצירת המילון (מיפוי אותיות לערכים)
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    
    # 2. מעבר על המחרוזת בעזרת אינדקסים
    for i in range(n):
        # בדיקה האם אנחנו לא באיבר האחרון, והערך הנוכחי קטן מהערך שאחריו
        if i < n - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]  # מחסירים את הערך (כמו ב-IV או IX)
        else:
            total += roman_map[s[i]]  # מוסיפים את הערך כרגיל
            
    return total

# דוגמאות לשימוש בפונקציה
print(f"Output: {romanToInt('III')}")    # Output: 3
print(f"Output: {romanToInt('IV')}")     # Output: 4
print(f"Output: {romanToInt('IX')}")     # Output: 9
print(f"Output: {romanToInt('LVIII')}")  # Output: 58
print(f"Output: {romanToInt('MCMXC')}\n")  # Output: 1990

print("Exercise 3: Linked List Cycle Detection")

#Exercise 3: Linked List Cycle Detection
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: ListNode) -> bool:
    visited = set()  # הפנקס שלנו לשמירת הצמתים
    
    while head is not None:
        # אם הצומת כבר בפנקס - יש מעגל אינסופי!
        if head in visited:
            return True
            
        # אם לא, נרשום אותו ונתקדם הלאה
        visited.add(head)
        head = head.next
        
    # אם הגענו לכאן, סימן שהגענו ל-None ואין מעגל
    return False

# בוא נבדוק את זה עם דוגמאות אמיתיות בקוד:
# ==========================================

print("--- check 1: list with cycle ---")
# יוצרים צמתים: 3 -> 2 -> 0 -> -4
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode((-4))

# מחברים אותם יחד בשרשרת
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # <--- הנה המעגל! הצומת האחרון מצביע חזרה לצומת השני (2)

# שולחים לפונקציה ובודקים
result1 = hasCycle(node1)
print(f"Is there a cycle in the first list? {result1}")  # צפוי להדפיס True


print("\n--- check 2: straight list without cycle ---")
# יוצרים צמתים ישרים: 1 -> 2 -> None
a = ListNode(1)
b = ListNode(2)
a.next = b
# b.next נשאר נקי (None)

# שולחים לפונקציה ובודקים
result2 = hasCycle(a)
print(f"Is there a cycle in the second list? {result2}\n")  # צפוי להדפיס False

print("Exercise 4: Intersection of Two Linked Lists")

#Exercise 4: Intersection of Two Linked Lists
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    # 1. פותחים פנקס ריק
    visited = set()
    
    # 2. עוברים על רשימה A ושומרים כל צומת בפנקס
    while headA is not None:
        visited.add(headA)
        headA = headA.next
        
    # 3. עוברים על רשימה B ובודקים מי מהם כבר נמצא בפנקס
    while headB is not None:
        if headB in visited:
            return headB  # מצאנו את המפגש!
        headB = headB.next
        
    # 4. אם לא נפגשו בכלל
    return None

# ==========================================
# יוצרים את המסילות ומספרים אותן בפועל:
# ==========================================

# 1. קודם כל ניצור את החלק המשותף שבו המסילות מתמזגות:
# צומת 8 -> צומת 4 -> צומת 5
shared_node_3 = ListNode(5)
shared_node_2 = ListNode(4)
shared_node_2.next = shared_node_3

intersection_node = ListNode(8) # <--- זה הצומת המדויק שבו הן נפגשות!
intersection_node.next = shared_node_2


# 2. ניצור את רשימה A (לפני המפגש יש את המספרים: 4 -> 1)
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = intersection_node  # מכאן היא מתחברת לחלק המשותף!
# רשימה A המלאה נראית כך: 4 -> 1 -> 8 -> 4 -> 5


# 3. ניצור את רשימה B (לפני המפגש יש את המספרים: 5 -> 6 -> 1)
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersection_node  # מכאן היא מתחברת לאותו צומת בדיוק!
# רשימה B המלאה נראית כך: 5 -> 6 -> 1 -> 8 -> 4 -> 5


# ==========================================
# נשלח את שתי הרשימות לפונקציה ונבדוק מה התוצאה:
# ==========================================
result = getIntersectionNode(headA, headB)

if result is not None:
    print(f"We found an intersection node with value: {result.val}")
else:
    print("There is no intersection node between the two lists.")

print()


print("Exercise 5: Majority Element")
#Exercise 5: Majority Element
def majorityElement(nums: list[int]) -> int:
    counts = {}
    
    # שלב 1: עוברים על הרשימה וסופרים כל מספר במילון
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
    # שלב 2: עוברים על המילון ובודקים למי יש רוב (יותר מאורך הרשימה חלקי 2)
    for num, count in counts.items():
        if count > len(nums) // 2:
            return num

# דוגמאות לשימוש בפונקציה
print(f"Output 1: {majorityElement([3, 2, 3])}")          # Output: 3
print(f"Output 2: {majorityElement([2, 2, 1, 1, 1, 2, 2])}")  # Output: 2
print(f"Output 3: {majorityElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9])}")  # Output: none (no majority element)
print(f"Output 4: {majorityElement([5,5,5,5,6,7,9])}\n")  # Output: 5

print("Exercise 6: Happy Number")
#Exercise 6: Happy Number
def isHappy(n: int) -> bool:
    visited = set()  # הפנקס שלנו
    
    # כל עוד לא הגענו ל-1, וגם לא נתקלנו במספר שכבר היה בפנקס:
    while n != 1 and n not in visited:
        visited.add(n)  # רושמים שביקרנו במספר הנוכחי בפנקס
        
        # מחשבים את ה-"next" (סכום ריבועי הספרות של n)
        # לדוגמה, עבור 19 זה יהפוך ל- 1**2 + 9**2 = 82
        n = sum(int(digit) ** 2 for digit in str(n))
        
    # אם הלולאה נעצרה כי n == 1, נחזיר True (מאושר!). אחרת False (מעגל אינסופי).
    return n == 1

# דוגמאות לשימוש בפונקציה
print(f"Output 1: {isHappy(19)}")  # Output: True (19 הוא מספר מאושר)
print(f"Output 2: {isHappy(2)}")   # Output: False (2 יוצר מעגל אינסופי)
print(f"Output 3: {isHappy(7)}\n")   # Output: True (7 הוא מספר מאושר)


#Exercise 7: Contains Duplicate
print("Exercise 7: Contains Duplicate")
def containsDuplicate(nums: list[int]) -> bool:
    # 1. פותחים פנקס ריק (set) לשמירת המספרים שעברנו עליהם
    seen = set()
    
    # 2. עוברים על כל מספר ברשימה בלולאה
    for num in nums:
        # 3. אם המספר כבר קיים בפנקס - מצאנו כפילות!
        if num in seen:
            print("The loop found a duplicate number:", num)  # הדפסה לצורך בדיקה
            return True  # מחזירים אמת שיש כפילות
            
        # 4. אם זו הפעם הראשונה שאנחנו רואים אותו, נרשום אותו בפנקס
        seen.add(num)
        
    # 5. אם עברנו על כל הרשימה והמספרים לא חזרו על עצמם
    return False

# בדיקה 1: רשימה עם כפילויות [1, 2, 3, 1]
numbers_list_1 = [1, 2, 3, 1]
result1 = containsDuplicate(numbers_list_1)
print(f"Is there a duplicate in list 1? {result1}")

# בדיקה 2: רשימה בלי כפילויות [1, 2, 3, 4]
numbers_list_2 = [1, 2, 3, 4]
result2 = containsDuplicate(numbers_list_2)
print(f"Is there a duplicate in list 2? {result2}\n")


