class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        max_freq = 0
        res = 0

        for key,value in c.items():
            max_freq = max(max_freq, value)

        for value in c.values():
            if value == max_freq:
                res += value
        return res
