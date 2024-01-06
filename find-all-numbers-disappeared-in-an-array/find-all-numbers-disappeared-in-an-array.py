class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Create a set of the input array
        num_set = set(nums)

        # Initialize an empty list to store disappeared numbers
        disappeared_numbers = []

        # Iterate over the range [1, n] and check for missing elements
        for i in range(1, n + 1):
            if i not in num_set:
                disappeared_numbers.append(i)

        # Return the list of disappeared numbers
        return disappeared_numbers