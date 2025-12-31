"""Full pyramid

    *
   * *
  * * *
 * * * *
* * * * *

"""

n = int(input("Enter value of full pyramid pattern: "))
for i in range(n):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))
