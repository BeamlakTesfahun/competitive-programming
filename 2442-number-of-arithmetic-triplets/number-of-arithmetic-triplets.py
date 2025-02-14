class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dic = {}
        res = 0

        for i in range(len(nums)):
            dic[nums[i]] = i
        print(dic)

        #[0,1,4,6,7,10]
        # 

        for i in range(len(nums)):
            t1 = nums[i] - diff
            t2 = nums[i] - diff*2
            if t1 in dic and t2 in dic:
                if i > dic[t1] and i > dic[t2]:
                    res += 1
        return res

        