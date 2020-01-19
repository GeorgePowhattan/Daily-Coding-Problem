# Given a list of strings, find the list of characters that appear in all strings.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # create alphabet hashtable
    charmap = {char: 0 for char in alphabet }
    # loop through set of characters in each word
    for word in strs:
        for char in set(word):
            charmap[char] += 1

    return [key for key in charmap.keys() if charmap[key] == len(strs)]
    
print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']
