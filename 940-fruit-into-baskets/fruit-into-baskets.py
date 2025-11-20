class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        dic = {}

        left = 0
        maxx = 0

        for right in range(len(fruits)):
            dic[fruits[right]] = dic.get(fruits[right], 0) + 1

            while dic and len(dic) > 2:
                dic[fruits[left]] -= 1
                if dic[fruits[left]] == 0:
                    del dic[fruits[left]]
                left += 1

            maxx = max(maxx, right - left + 1)
        return maxx






        