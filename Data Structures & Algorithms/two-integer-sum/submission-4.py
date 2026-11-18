class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = array of integers
        # target 

        map = {}

        for i in range(len(nums)):
            want = target - nums[i]
            if want in map and map[want] != i:
                return [min(i, map[want]), max(i, map[want])]
            map[nums[i]] = i