# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s):
        # definitions:
        indices = {}      # hashmap storing indices of letters
        tail = -1         # end of the range
        longest = 0       # stores current max length of substring 
        
        for head in range(len(s)):          # iterate over all the letters
            if s[head] in indices:          # if letter is already stored, move the tail to the new position
                tail = max(tail, indices[s[head]]) 
            indices[s[head]] = head         # always store current letter position into hasmap
            longest = max(longest, head-tail) # update longest or retain its current value
        
        return longest            
        
print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
