class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)

        print(c)

        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        return -1



        # dic = {}

        # for i,n in enumerate(s):
        #     if n in dic:
        #         dic.pop(n)
        #     else:
        #         dic[n] = i
        # # print(dic)

        # if not dic:
        #     return -1
        # for key, value in dic.items():
        #     return value
