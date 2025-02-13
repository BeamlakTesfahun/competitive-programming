class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = int(len(nums)/3)
        res = []

        n = Counter(nums)

        for key,val in n.items():
            if val > target:
                res.append(key)
        return res

        
        