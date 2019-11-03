#### Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(string):
    res = ''
    length = 0
    max_length = 0
    for letter in string:
        if letter not in res:
            res += letter
            length = len(res)
            max_length = max(length, max_length)
        else:
            max_length = max(length, max_length)
            res = letter
    return max_length

s = 'abrkaabcdefghijjxxx'
t = 'jklafjerbzop'

print(lengthOfLongestSubstring(t))
