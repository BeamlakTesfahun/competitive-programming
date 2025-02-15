class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        c3 = Counter(nums3)

        res = []

        for key,value in c1.items():
            if key in c2 or key in c3:
                res.append(key)
        for key,value in c2.items():
            if key in c3 and key not in res:
                res.append(key)

        return res






        