class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(1, len(nums)):
            if nums[right] > nums[left]:
                nums[left+1] = nums[right]
                left += 1
        return left + 1
        