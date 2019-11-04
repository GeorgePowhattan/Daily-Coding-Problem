# Consecutive Ones in Binary

'''Return the longest run of 1s for a given integer n's binary representation.

Example:
Input: 242 
Output: 4

242 in binary is 0b11110010, so the longest run of 1 is 4.'''


def consecutive_ones(num):
    
    lst = []
    
    # The first part is a decimal -> binary converter written recursively
    def conversion_binary(num):
   
        if (num // 2) == 0:
            lst.append(num % 2)
            return [number for number in reversed(lst)]   # the binary number is ouput in the form of a list

        lst.append(num % 2)
        num = num // 2
        return conversion_binary(num)
    
    lst = conversion_binary(num)
    
    # The second part counts consecutive ones in a list from conversion_binary 
    max_ones = 0
    cur_ones = 0
    
    for digit in lst:
        if digit == 1:
            cur_ones += 1
            max_ones = max(max_ones, cur_ones)
        else:
            cur_ones = 0
    
    return max_ones


print(consecutive_ones(242))