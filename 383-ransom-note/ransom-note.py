class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(ransomNote)
        c2 = Counter(magazine)

        # print(c)
        # print(c2)

        # Counter({'a': 2})
        # Counter({'a': 1, 'b': 1})

        for key,value in c.items():
            if key not in c2:
                return False
            elif key in c2:
                if value > c2[key]:
                    return False
        return True
        