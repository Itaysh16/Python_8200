"""
1.
My mission is to convert the following code into a list comprehension.
 squares = []
for i in range(1, 11):
    squares.append(i**2)

"""

squares = [i**2 for i in range(1, 11)]
print(squares)

"""
2.
My mission is to convert the following code into a list comprehension.
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return reversed_words
"""

def reverse_words(sentence):
    return [word[::-1] for word in sentence.split()]

print(reverse_words("hello world python"))

"""
3.
My mission is to convert the following code into a list comprehension.
for i in range(1, 11):
    print (i, end=" ")
"""
squares = [print(i, end=" ") for i in range(1, 11)]
print()

"""
4.
My mission is to convert the following code into a list comprehension.
for i in range(1, 11):
    if i % 2 == 0:
        print (i, end=" ")
"""

squares = [print(i, end=" ") for i in range(1, 11) if i % 2 == 0]
print()

"""
5.
My mission is to convert the following code into a list comprehension.
for i in range(2,11,2):
    print (i, end=" ")
"""
squares = [print(i, end=" ") for i in range(2, 11, 2)]
print()

"""
My test is to write a list comprehension that produces all pairs of i and j where
the sum of i and j is even, for i and j in the range 1 to 10.

"""
even_pairs = [(i, j) for i in range(1, 11) for j in range(1, 11) if (i + j) % 2 == 0]
print(even_pairs)

"""
My test is to write a list comprehension that receives a dictionary and return
it back words
"""

original_dict = {'a': 1, 'b': 2, 'c': 3}
backwords_dict = {v: k for k, v in original_dict.items()}
print(backwords_dict)