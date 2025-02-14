class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        res = []
        
        sorted_people = sorted(people, key=lambda x:x[1], reverse=True)

        for i in range(len(sorted_people)):
            res.append(sorted_people[i][0])
        return res
        