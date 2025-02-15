class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        # dic = {}
    
        for i in alpha:
            if i not in sentence:
                return False
        return True

        # for i in sentence:
        #     dic[i] = dic.get(i,0) + 1

        # print(dic)

        # for key,value in dic.items():
        #     if value > 1:
        #         return False
        # return True
        
        