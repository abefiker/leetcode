class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        square_number = []
        for num in nums:
            square_number.append(pow(num,2))
        return sorted(square_number)    