# Given a list of strings, find the list of characters that appear in all strings.

def common_characters(strs):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    charmap = {char: 0 for char in alphabet }
    for word in strs:
        for char in word:
            charmap[char] += 1

    return [key for key in charmap.keys() if charmap[key] == 3]
    
print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']
