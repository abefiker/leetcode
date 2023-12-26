class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        last_val = n - 1
        j = 0
        while j < last_val:
            if nums[j] % 2 == 0:
                j += 1
            else:
                nums[j], nums[last_val] = nums[last_val], nums[j]
                last_val -= 1
        return nums