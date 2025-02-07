class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:  
            return len(nums)
        
        left = 1  
        
        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:  
                nums[left] = nums[right]  
                left += 1
        
        return left  
