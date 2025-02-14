class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0

        #"MCMXCIV"

        for i in range(len(s)):
            if i == len(s) - 1:
                res += dic[s[i]]   
    

            if i != len(s) - 1 and dic[s[i+1]] <= dic[s[i]]:
                res += dic[s[i]]
             

            elif i != len(s) - 1 and dic[s[i+1]] > dic[s[i]]:
                res -= dic[s[i]]

            
        return res  

        