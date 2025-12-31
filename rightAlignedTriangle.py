"""Right Aligned Triangle Pattern

      *
    * *
  * * *
* * * *

"""

n = int(input("Enter value of right aligned triangle pattern: "))
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)
