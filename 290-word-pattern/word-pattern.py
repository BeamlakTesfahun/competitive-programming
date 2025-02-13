class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        charToWord = {}
        wordToChar = {}

        splitted = s.split(" ")
        print(splitted)

        if len(pattern) != len(splitted):
            return False


        for c, w in zip(pattern, splitted):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True
        