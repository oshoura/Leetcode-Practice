class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hash:
                return (hash[difference], i)
            else:
                hash[n] = i
