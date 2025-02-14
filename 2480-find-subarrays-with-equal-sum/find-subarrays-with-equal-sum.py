class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:

        res = []

        left = 0

        if len(nums) <= 2:
            return False        
        for right in range(1, len(nums)):
            sums = nums[left] + nums[right]

            if sums in res:
                return True
            res.append(sums)
            left += 1
        return False

        