class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:


        dic_p = Counter(p)
        dic_s = Counter(s[:len(p)])

        result = []
        left = 0


        if dic_s == dic_p:
            result.append(0)


        for right in range(len(p), len(s)):
            dic_s[s[left]] -= 1
            dic_s[s[right]] += 1

            left += 1

            if dic_s == dic_p:
                result.append(left)
        return result


        