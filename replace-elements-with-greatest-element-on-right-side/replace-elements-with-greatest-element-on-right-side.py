class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        n = len(arr)
        for i in range(n - 1 , -1 , -1):
            cur_val = arr[i]
            arr[i] = max_val
            max_val = max(max_val,cur_val)
        return arr