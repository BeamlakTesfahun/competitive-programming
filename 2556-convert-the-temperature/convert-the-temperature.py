class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        f = celsius * 1.80 + 32.00
        k = celsius + 273.15

        return [k, f]
        