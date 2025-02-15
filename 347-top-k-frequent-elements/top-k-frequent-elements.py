class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []

        # 1: 3
        # 2: 2
        # 3 : 1

        sorted_c = sorted(c.items(), key=lambda x:x[1], reverse=True)
        print(sorted_c)

       


            
        return [item[0] for item in sorted_c[:k]]
        