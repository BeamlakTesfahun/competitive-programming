class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = int(len(nums)/3)

        dic = {}
        result = []

        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        
        for key,value in dic.items():
            if value > times:
                result.append(key)
        return result


        