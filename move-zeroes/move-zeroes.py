class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j, N_Z = 0, 0, 0
        while i < n and j < n:
            if nums[i] == 0:
                N_Z += 1
            else:
                nums[j] = nums[i]
                j += 1
            i += 1

        while N_Z > 0:
            nums[j] = 0
            j += 1
            N_Z -= 1