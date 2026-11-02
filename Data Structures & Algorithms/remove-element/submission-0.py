class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we are given array nums and int val
        # we want to remove all occurences of val in nums (mutate)
        # and return the number of elements in nums that are not val

        k = 0 # let k be the no.of elements in nums that is not val
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
                nums[k-1] = nums[i]
        return k