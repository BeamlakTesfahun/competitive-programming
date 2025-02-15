class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        res = 0

        for key,value in c1.items():
            if key in c2 and value == 1:
                if c2[key] == 1:
                    res += 1
        return res



        