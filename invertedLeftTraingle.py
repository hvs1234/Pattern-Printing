"""Inverted Left Aligned Triangle Pattern

* * * * * * * *
* * * * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*

"""

n = int(input("Enter value of inverted left aligned triangle pattern: "))
for i in range(n, 0, -1):
    print("* " * i)
