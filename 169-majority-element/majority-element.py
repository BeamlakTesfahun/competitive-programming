class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = int(len(nums) / 2)
        n = Counter(nums)
        print(n)

        for key,value in n.items():
            if value > target:
                return key

        