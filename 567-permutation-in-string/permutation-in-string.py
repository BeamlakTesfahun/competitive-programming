class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # find 

        dic_s1 = Counter(s1)

        dic_s2 = Counter(s2[:len(s1)])

        if dic_s1 == dic_s2:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            dic_s2[s2[left]] -= 1
            dic_s2[s2[right]] += 1

            left += 1

            if dic_s1 == dic_s2:
                return True

        return False



        

        