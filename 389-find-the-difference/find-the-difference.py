class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)

        for key,value in c2.items():
            if key not in c1:
                return key
            elif key in c1 and value != c1[key]:
                return key

        
        