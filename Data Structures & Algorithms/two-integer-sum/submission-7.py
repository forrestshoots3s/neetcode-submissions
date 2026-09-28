class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i, num in enumerate(nums):
            gap = target - num
            if gap in record:
                return [record[gap], i]
            record[num] = i