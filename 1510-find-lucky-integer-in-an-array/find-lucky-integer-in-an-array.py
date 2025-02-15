class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        max_val = -1

        for key,value in c.items():
            if value == key:
                max_val = max(max_val, key)
        return max_val