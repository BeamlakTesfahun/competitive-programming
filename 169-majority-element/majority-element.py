class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = int(len(nums) / 2)
        
        c = collections.Counter(nums)
        
        for key,value in c.items():
            if value > times:
                return key

