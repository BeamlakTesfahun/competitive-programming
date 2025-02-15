class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        dic = {}
        for i in paths:
            dic[i[0]] = i[1]
        print(dic)

        # {'London': 'New York', 'New York': 'Lima', 'Lima': 'Sao Paulo'}
        for i in paths:
            for j in i:
                if j not in dic:
                    return j


        