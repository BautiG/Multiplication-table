"""
multiplication-table.py
Author: Bauti G
Credit: Liam S.
Assignment:

Write and submit a Python program that prints a multiplication table. The user 
must be able to determine the width and height of the table before it is printed.

The final multiplication table should look like this:

Width of multiplication table: 10
Height of multiplication table: 8

  1   2   3   4   5   6   7   8   9  10
  2   4   6   8  10  12  14  16  18  20
  3   6   9  12  15  18  21  24  27  30
  4   8  12  16  20  24  28  32  36  40
  5  10  15  20  25  30  35  40  45  50
  6  12  18  24  30  36  42  48  54  60
  7  14  21  28  35  42  49  56  63  70
  8  16  24  32  40  48  56  64  72  80
"""
width = input(int("Width of multiplication table: "))
height = input(int("Height of multiplication table: "))

for a in range(height):
    for b in [a*2]:
        for c in [a*3]:
            for d in [a*4]:
                for e in [a*5]:
                    for f in [a*6]:
                        for g in [a*7]:
                            for h in [a*8]:
                                print(a, b, c, d, e, f, g, h)

print("The number is: {0:>3}".format(1))         # Prints "The number is:   1"
print("The number is: {0:>3}".format(12))        # Prints "The number is:  12"
print("The number is: {0:>3}".format(123))       # Prints "The number is: 123"