"""Repeated Numbers

1
2 2
3 3 3
4 4 4 4

"""

n = int(input("Enter value of repeated numbers pattern: "))
for i in range(1, n + 1):
    print((str(i) + " ") * i)
