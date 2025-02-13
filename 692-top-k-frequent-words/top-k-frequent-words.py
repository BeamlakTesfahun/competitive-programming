class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []

        c = Counter(words)

        sorted_c = sorted(c.items(), key=lambda x: (-x[1], x[0]))

        return [sorted_c[i][0] for i in range(k)]

        # Counter({'i': 2, 'love': 2, 'leetcode': 1, 'coding': 1})
        # sorted_c = sorted(c.items(), key=lambda x:x[1], reverse=True)

        # print(sorted_c)

       
        # return [sorted_c[i][0] for i in range(len(sorted_c[:k]))]


        