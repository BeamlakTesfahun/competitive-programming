class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)

        c2 = Counter(nums2)

        # Counter({2: 2, 3: 1})
        # Counter({1: 1, 2: 1})

        sums = 0
        res = []
        for key, value in c1.items():
            if key in c2:
                sums += value
        res.append(sums)
        sums = 0

        for key, value in c2.items():
            if key in c1:
                sums += value
        res.append(sums)
        return res
                





        