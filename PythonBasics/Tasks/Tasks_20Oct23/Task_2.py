"""
Sum of Digits: Create a function that calculates the sum of the digits of a positive integer.
n = 12345
sum = 15
n = 123
sum = 6
"""

def calculate(number):
    print("Actual number is:", number)
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum



number = 123456
print(calculate(number))
