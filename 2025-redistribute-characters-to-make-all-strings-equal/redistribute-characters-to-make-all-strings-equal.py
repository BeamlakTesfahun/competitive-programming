class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}

        for i in words:
            for j in range(len(i)):
                dic[i[j]] = dic.get(i[j],0) + 1
        print(dic)

        for key, value in dic.items():
            if value % len(words) != 0:
                return False
        return True


    




        