# Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.

'''Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']'''

def compress(chars):
    output = []
    previous = None
    counter = 1
    for letter in chars:
        current = letter
        if current == previous:
            counter += 1
        elif current != previous and counter > 1:
            output.append(str(counter))
            counter = 1
            output.append(current)
        else:
            output.append(current)
        previous = current
    if counter > 1:
        output.append(str(counter))
    return output

lst = ['a', 'a', 'b', 'c', 'c', 'c']

print(compress(lst))