class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        c = Counter(nums)
        
        res = []
        pair = 0
        no_pair = 0

        for key,value in c.items():
            if value % 2 == 0:
                pair += value/2
            else: 
                pair += value // 2
                no_pair += 1
        return [int(pair), no_pair]


        