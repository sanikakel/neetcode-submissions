class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0 for i in range(max(nums)+1)]

        for i in nums:
            counts[i] += 1
        
        j = 0
        for n in range(len(counts)):
            for _ in range(counts[n]):
                nums[j] = n
                j += 1
        return nums