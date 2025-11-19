class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lenn = len(nums) + 1

        for i in range(lenn):
            if i not in nums:
                return i
