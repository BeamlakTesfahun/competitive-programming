class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        c = collections.Counter(nums)
        

        for value in c.values():
            if value > 1:
                return True
        return False

        