def add_numbers(a, b=10):
    """
    Adds two numbers.

    parameters:
    a (int or float): The first number.
    b (int or float, or default=10): the secound number.

    Returns=a+b (int or float).
    """
    return a + b

print(add_numbers(5, 3))
print(add_numbers(5))


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci of 5 = {fibonacci(5)}")
print(f"Fibonacci of 8 = {fibonacci(8)}")

def binary_search(arr, target, low, high):
    """
    Performs recursive binary search on a sorted list.
    
    Returns:
    int: Index of target if found, else -1.
    """
    
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


numbers = [2, 5, 8, 12, 16, 23, 38, 56]

print(binary_search(numbers, 23, 0, len(numbers) - 1))

print(binary_search(numbers, 100, 0, len(numbers) - 1))