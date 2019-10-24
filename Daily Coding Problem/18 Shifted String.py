# You are given two strings, A and B. Return whether A can be shifted some number of times to get B.
# Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B= acb should return false.


def is_shifted(a, b):
    
    if len(a) != len(b):
        return False
    
    if a[0] in b:
        shift = b.index(a[0])
    else:
        return False
    
    if any(a[index] != b[(index+shift) % len(a)] for index in range(len(a))):
        return False
    
    return True
    
    
a = 'abcdef'
b = 'cdefab'

print(is_shifted(a, b))
