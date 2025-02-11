class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        dic = {}
        result = []

        for i in range(len(nums)):
            if sorted_num[i] in dic:
                continue

            dic[sorted_num[i]] = i
        for i in nums:
            result.append(dic[i])
        return result

        