class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            max_wealth = max(max_wealth, sum(account))

        return max_wealth



        '''sum = 0
        max = 0
        for i in accounts:
            if sum > max:
                max = sum
            sum = 0
            for j in i:
                sum = j + sum

        if sum > max:
            max = sum
        return max'''

            