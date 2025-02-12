class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        print(set_nums1)
        print(set_nums2)

        res = set_nums1.intersection(set_nums2)
        res = list(res)
        return res

        # res = []

        # for i in nums1:
        #     for j in nums2:
        #         if i == j:
        #             res.append(i)
        # return res

        