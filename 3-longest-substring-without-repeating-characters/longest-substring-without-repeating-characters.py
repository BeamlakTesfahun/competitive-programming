class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        sets = set()
        left = 0

        for right in range(len(s)):
            while sets and s[right] in sets:
                sets.remove(s[left])
                left += 1
            sets.add(s[right])
            longest = max(longest, right - left + 1)
        return longest    
        

       