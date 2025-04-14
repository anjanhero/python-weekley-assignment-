""" This below program will calculate the perimeter of rectangle whose length is
    9 and breadth is 6.
"""

perimeter = 2 * (9 + 6)
print("Perimeter:", perimeter)

""" This program prints Python is great, it’s wild! """


print("Python is great, its wild!")


""" The program prints 2 to the 10th power """


power = 2 ** 10
print("2 to the 10th power:", power)


""" The below program prints the difference of 7 factorial and 5 factorial. """

import math

factorial_difference = math.factorial(7) - math.factorial(5)
print("7! - 5!:", factorial_difference)


""" The below program prints my forename multiplied by 5 """

forename = "chaudhary"
print("Forename * 5:", forename * 5)

"""This program prints my name left justified 15 spaces """

print("Anjan".ljust(15))

""" This program will print the value of PI to 5 decimal places """

import math
pi_value = round(math.pi, 5)
print("PI to 5 decimal places:", pi_value)

""" The below program prints the value of 200 modulus 12  """

modulus_result = 200 % 12
print("200 % 12:", modulus_result)

""" WAP to print 7.2 as an integer value """

a = int(7.2)
print("Integer value of 7.2:", a)

""" Write the program to print the Unicode encoding for your name """

unicode_values = [ord(char) for char in "Anjan"]
print("Unicode encoding for your name:", unicode_values)
