"""Left Aligned Triangle Pattern

*
* *
* * *
* * * *
* * * * *
* * * * * *

"""

n = int(input("Enter value of left aligned triangle pattern: "))
for i in range(1, n + 1):
    print("* " * i)
