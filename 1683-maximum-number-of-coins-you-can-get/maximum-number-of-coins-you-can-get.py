class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        print(piles)

        return sum(piles[len(piles)//3: : 2])
        