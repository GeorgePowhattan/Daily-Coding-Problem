# Plus One

'''Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer. The most significant digit is at the front of the array and each element in the array contains only one digit. Furthermore, the integer does not have leading zeros, except in the case of the number '0'.

Example:
Input: [2,3,4]
Output: [2,3,5]
'''

def plusOne(digits):
    
    number = 0
    
    # construct a number
    for i, digit in zip(range(len(digits)),reversed(list(digits))):
    
        number += digit * 10**i
        plusone = number + 1
    
    # deconstruct the number to a list
    return [digit for digit in str(plusone)]

num = [2, 9, 9]

print(plusOne(num))