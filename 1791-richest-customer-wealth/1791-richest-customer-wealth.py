class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = 0
        max = 0
        for i in accounts:
            if sum > max:
                max = sum
            sum = 0
            for j in i:
                sum = j + sum

        if sum > max:
            max = sum
        return max

            