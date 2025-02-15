class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 1 2 2 3 8

        sorted_nums = sorted(nums)
        dic = {}
        res = []

        for i in range(len(nums)):
            if sorted_nums[i] in dic:
                continue
            dic[sorted_nums[i]] = i
        print(dic)

        for j in nums:
            res.append(dic[j])
        return res
        
