# Shifted string

'''You are given two strings, A and B. Return whether A can be shifted some number of times to get B.

Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.'''

def is_shifted(a, b):
    if len(a) != len(b):
        return('The strings are not the same length! Cannot be shifted.')
    else:
        try:
            shift = b.index(a[0])
            return all([True if a[i] == b[(i + shift) % len(a)] else False for i in range(len(a))])
        except:
            return('The first letter of a not found in b at all')


a = 'aabcde'
b = 'cdeaab'

c = 'aaa'
d = 'bbb'

print(is_shifted(a,b))
print(is_shifted(c,d))