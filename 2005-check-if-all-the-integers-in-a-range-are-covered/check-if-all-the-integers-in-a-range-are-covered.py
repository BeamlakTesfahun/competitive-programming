class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [False] * 60

        for i, j in ranges:
            for x in range(i, j+1):
                arr[x] = True
        for x in range(left, right+1):
            if not arr[x]:
                return False
        return True