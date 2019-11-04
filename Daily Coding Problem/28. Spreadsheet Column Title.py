#### Spreadsheet Column Title

'''MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc. In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth. Given a positive integer, find its corresponding column name.'''


def convertToTitle(num):
    
    # Spawn hashtable of numbers and alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    hashtable = { number: letter for number, letter in enumerate(alphabet,start=1) }
    hashtable[0] = None
    length = len(alphabet)
    lst = []
    
    # Recursively convert number in decimal to alphabetical MS Office notation ('AZ')
    def recursion(num):
        if (num // length) == 0:
            lst.append(hashtable[num % length])
            return ''.join([letter.upper() for letter in reversed(lst) if letter is not None])

        elif num % length == 0:
            lst.append(hashtable[length])
            num = num // length - 1
            return recursion(num)

        else:    
            lst.append(hashtable[num % length])
            num = num // length
            return recursion(num)
    
    return recursion(num)


a = 51    # AY
b = 52    # AZ
c = 676    # YZ
d = 704    # AAB

columns = [a, b, c, d]

for column in columns:
    print(convertToTitle(column))

