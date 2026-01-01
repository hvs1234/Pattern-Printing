"""Repeated Alphabet

A
B B
C C C
D D D D

"""

n = int(input("Enter value of repeated alphabet pattern: "))
for i in range(1, n + 1):
    print((chr(64 + i) + " ") * i)
