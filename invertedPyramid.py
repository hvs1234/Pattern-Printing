"""Inverted Pyramid Pattern

* * * * * * * *
   * * * * *
     * * *
        *

"""

n = int(input("Enter value of inverted pyramid pattern: "))
for i in range(n):
    print("  " * i + "* " * (2 * (n - i) - 1))
