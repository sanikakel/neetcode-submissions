class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxval = -1
        for i in range(len(arr) - 1, -1, -1):
            newval = max(maxval, arr[i])
            arr[i] = maxval
            maxval = newval
        return arr