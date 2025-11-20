class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        counts = Counter(nums)
        res = []

        t = len(nums) // 3

        for key, val in counts.items():
            if val > t:
                res.append(key)
        return res


