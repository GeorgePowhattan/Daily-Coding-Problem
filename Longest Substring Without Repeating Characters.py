class Solution:
    def lengthOfLongestSubstring(self, s):
        indices = {}
        # definitions:
        tail = -1
        longest = 0
        
        for head in range(len(s)):
            if s[head] in indices:
                tail = max(tail, indices[s[head]])
            indices[s[head]] = head
            longest = max(longest, head-tail) 
        
        return longest            
        
        Solution().lengthOfLongestSubstring(s)
# 10
