'''Version numbers are strings that are used to identify unique states of software products. A version number is in the format a.b.c.d. and so on where a, b, etc. are numeric strings separated by dots. These generally represent a hierarchy from major to minor changes. Given two version numbers version1 and version2, conclude which is the latest version number.

Your code should do the following:
If version1 > version2 return 1.
If version1 < version2 return -1.
Otherwise return 0.
'''

def compareVersion(version1, version2):
    ver1 = [int(number) for number in version1.split('.')]
    ver2 = [int(number) for number in version2.split('.')]
    for number1, number2 in zip(ver1, ver2):
        if number1 > number2:
            return 1
        if number1 < number2:
            return -1
    return 0

version1 = "1.0.33"
version2 = "1.0.27"

print(compareVersion(version1, version2))