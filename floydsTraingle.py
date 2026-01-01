"""Floyd's Triangle Pattern

1
2 3
4 5 6
7 8 9 10

"""

n = int(input("Enter value of Floyd's triangle pattern: "))
value = 1
for i in range(1, n + 1):
    for _ in range(i):
        print(value, end=" ")
        value += 1
    print()
