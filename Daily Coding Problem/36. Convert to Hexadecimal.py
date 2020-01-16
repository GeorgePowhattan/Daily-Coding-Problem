# Given a non-negative integer n, convert the integer to hexadecimal and return the result as a string. Hexadecimal is a base 16 representation of a number, where the digits are 0123456789ABCDEF. Do not use any builtin base conversion functions like hex.

# Iterative solution 

def find_rank(n):
    counter = 0
    while n > 16:
        n = n / 16 
        counter += 1
    return counter

def to_hex(n):
    # define hexadecimal:
    hex_figures = '123456789ABCDEFG'
    hex_conversion_table = { i: fig for i, fig in enumerate(hex_figures, start=1) }
    # define result string
    res = ''
    # find the largest 16-exponent of the number
    rank = find_rank(n)
    for i in reversed(range(rank+1)):
        div = 16**(i)
        res += hex_conversion_table[n // div]
        n = n % div
    return res
    
n = 5000

print(find_rank(n))
# '7B'
