class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        diff = 0
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                diff += 1
        return diff