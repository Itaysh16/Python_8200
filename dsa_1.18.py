#Exercise 1
from heapq import merge


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    


# Exercise 2 chapter 1 part 1
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if self.items:
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Exercise 2 chapter 1 part 2
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def do_somthing(self):
        self.append(1)

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def search(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def delete(self, value):
        if not self.head:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.value == value:
                curr.next = curr.next.next
                return
            curr = curr.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next  # 1. שמירת ההמשך
            curr.next = prev       # 2. הפיכת החץ
            prev = curr            # 3. קידום prev
            curr = next_node       # 4. קידום curr
        self.head = prev

    def display(self):
        """פונקציית עזר להדפסת הרשימה בצורה ויזואלית"""
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.value))
            curr = curr.next
        print(" -> ".join(elements) if elements else "Empty List")


# Exercise 2 chapter 2 part 1
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Exercise 2 chapter 2 part 2
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    def merge(left, right):
        merged = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # הוספת איברים שנותרו
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    return merge(left_half, right_half)

# --- בדיקה של הרשימה המקושרת ---
if __name__ == "__main__":
    
    stack = Stack()
    
    # 1. הוספת איברים
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # 2. הצצה באיבר העליון
    print(f"Top element (peek): {stack.peek()}")  # אמור להדפיס 30
    
    # 3. הוצאת איבר
    popped = stack.pop()
    print(f"Popped element: {popped}")            # אמור להדפיס 30
    
    # 4. בדיקת גודל ומצב
    print(f"Current size: {stack.size()}")        # אמור להדפיס 2
    print(f"Is empty? {stack.is_empty()}")        # אמור להדפיס False


    sll = SinglyLinkedList()
    print("Evyatar shlomi")
    sll.do_somthing()  # הוספת איבר ראשון (1)\
    sll.display()  # אמור להדפיס: 1 
    # 1. הוספת איברים
    sll.append(10)
    sll.append(20)
    sll.append(30)
    print("Initial List:")
    sll.display()  # אמור להדפיס: 10 -> 20 -> 30

    # 2. חיפוש
    print("Search 20:", sll.search(20))  # True
    print("Search 99:", sll.search(99))  # False

    # 3. הפיכת הרשימה
    sll.reverse()
    print("Reversed List:")
    sll.display()  # אמור להדפיס: 30 -> 20 -> 10

    # 4. מחיקה
    sll.delete(20)
    print("After deleting 20:")
    sll.display()  # אמור להדפיס: 30 -> 10


sorted_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(binary_search(sorted_arr, 23))  # צפוי להחזיר: 5 (אינדקס)
print(binary_search(sorted_arr, 100)) # צפוי להחזיר: -1


unsorted_arr = [38, 27, 43, 3, 9, 82, 10]

print(merge_sort(unsorted_arr))  # צפוי להחזיר: [3, 9, 10, 27, 38, 43, 82]


