# Long definition
def palindrome_check_long(s):
    binary = []
    for letter, letter_rev in zip(s, reversed(s)):
        if letter == letter_rev:
            binary.append(1)
        else:
            binary.append(0)
    return (0 not in binary)
    
# Using list comprehension
def palindrome_check(s):
    return all(letter == letter_rev for letter, letter_rev in zip(s, reversed(s)))
    
# Check
s = 'abcda'
palindrome_check_long(s)
palindrome_check(s)
