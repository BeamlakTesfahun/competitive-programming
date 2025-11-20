class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        result = []
        dic_s = Counter(s[:len(p)])
        dic_p  = Counter(p)
        print(dic_s)
        print(dic_p)

        if dic_s == dic_p:
            result.append(0)

        left = 0
        for right in range(len(p), len(s)):
            dic_s[s[right]] += 1
            dic_s[s[left]] -= 1

            left += 1
            if dic_s == dic_p:
                result.append(left)


        return result