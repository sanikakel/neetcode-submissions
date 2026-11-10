# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)

    def mergeSortHelper(self, pairs, s, e):
        if (e - s) + 1 <= 1:
            return pairs

        m = (s + e) // 2

        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m+1, e)
        self.merge(pairs, s, m, e)

        return pairs


    def merge(self, arr, s, m, e):
        left = arr[s: m+1]
        right = arr[m+1: e+1]

        i, j = 0, 0
        p = s

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[p] = left[i]
                i += 1
            else:
                arr[p] = right[j]
                j += 1
            p += 1

        while i < len(left):
            pairs[p] = left[i]
            i += 1
            p += 1

        while j < len(right):
            pairs[p] = right[j]
            j += 1
            p += 1

        return pairs