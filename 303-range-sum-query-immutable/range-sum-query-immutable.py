class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        value = 0
        for i in nums:
            value += i
            self.prefix.append(value)
        # print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix[right]
        left_sum = self.prefix[left-1] if left > 0 else 0
        return right_sum - left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)