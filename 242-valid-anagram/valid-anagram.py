class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = Counter(s)
        dic_t = Counter(t)

        if dic_s == dic_t:
            return True

        return False        