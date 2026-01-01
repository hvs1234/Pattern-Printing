"""Number Pattern

1
1 2
1 2 3
1 2 3 4

"""

n = int(input("Enter value of number pattern: "))
for i in range(1, n + 1):
    print(*range(1, i + 1))
