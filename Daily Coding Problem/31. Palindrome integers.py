# Palindrome integers

'''Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a palindrome.'''

def is_palindrome(num):
    res = []
    div = 10
    while div < num*10:
        res.append(int((num % div) // (div/10)))
        div *= 10
    return all([True if num == num_rev else False for num, num_rev in zip(res, reversed(res))])

n1 = 121
n2 = 5432112345
n3 = 123

questions = [n1,n2,n3]

for number in questions:
    print(is_palindrome(number))
