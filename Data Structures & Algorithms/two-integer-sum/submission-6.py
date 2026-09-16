class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in prevMap:
                return [prevMap[dif], i]
            prevMap[num] = i