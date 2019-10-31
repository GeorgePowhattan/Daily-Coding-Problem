# Convert Roman Numerals to Decimal

hashmap = dict(
I     =1,
V     =5, 
X     =10,
L     =50,
C     =100,
D     =500,
M     =1000)

n = 'MCMX'

def romanToInt(string):
    res = 0
    i = 0
    while i < len(string):    # check if the number after is greater than the current one - subtracting
        if i+1 < len(string):
            if hashmap[string[i+1]] > hashmap[string[i]]:
                res = res + hashmap[string[i+1]] - hashmap[string[i]]
                i += 2
            else:
                res += hashmap[string[i]]
                i += 1
        else:
            res += hashmap[string[i]]
            i += 1
    return res

# Iterating the Roman number backwards is arguably easier:
def romanToInt2(string):
    res = 0
    previous = 0
    for letter in reversed(string):
        current = hashmap[letter]
        if current < previous:
            res -= current
        else:
            res += current
        previous = current
    return res      

print(romanToInt(n))
print(romanToInt2(n))