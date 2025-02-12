class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c_nums1 = Counter(nums1)
        c_nums2 = Counter(nums2)

        # print(c_nums1.items())
        # print(c_nums2)
        res = []

        for k1,v1 in c_nums1.items():
            for k2,v2 in c_nums2.items():
                if k1 == k2:
                    s = min(v1,v2)
                    for i in range(s):
                        res.append(k1)
        return res
            


        

        

