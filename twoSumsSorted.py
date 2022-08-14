class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = 0
        r = len(nums) - 1
        print(l, r)
        while l != r:
            print(l, r)
            if nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                return [l, r]


print(Solution().twoSum([2, 11, 7, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
