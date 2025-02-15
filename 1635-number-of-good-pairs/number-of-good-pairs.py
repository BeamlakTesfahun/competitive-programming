class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        # 1 2 3 1 1 3
        
        res = 0

        for left in range(len(nums)):
            for right in range(left+1, len(nums)):
                if nums[left] == nums[right]:
                    res += 1
        return res
            

        