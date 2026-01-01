"""Alphabet Pattern

A
A B
A B C
A B C D

"""

n = int(input("Enter value of alphabet pattern: "))
for i in range(1, n + 1):
    print(*[chr(65 + j) for j in range(i)])
