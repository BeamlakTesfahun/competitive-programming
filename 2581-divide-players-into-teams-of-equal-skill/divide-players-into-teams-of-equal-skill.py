class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        teams = len(skill)/2

        sums = sum(skill) / teams
        chem = 0

        skill.sort()

        left = 0
        right = len(skill) - 1

        while left < right:
            if skill[left] + skill[right] != sums:
                return -1

            chem += (skill[left] * skill[right])
            left += 1
            right -= 1

        return chem
