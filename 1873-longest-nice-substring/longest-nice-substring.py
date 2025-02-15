class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = ""
                
        for windowStart in range(len(s)):
            for windowEnd in range(windowStart + 1, len(s) + 1):
                substring = s[windowStart:windowEnd]
                if all(c.lower() in substring and c.upper() in substring for c in set(substring)):
                    if len(substring) > len(longest):
                        longest = substring
                
        return longest
        