class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = collections.Counter(s)
        c2 = collections.Counter(t)

        if c == c2:
            return True
        return False