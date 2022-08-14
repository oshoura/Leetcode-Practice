class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        results = []
        # initialize pointers
        a = 0
        # first pointer goes through list
        while a < len(nums) - 2:
            target = nums[a] * -1
            b = a + 1
            c = len(nums) - 1
            # second two pointers perform mini 2Sum II
            while b < c:
                if nums[b] + nums[c] < target:
                    b += 1
                elif nums[b] + nums[c] > target:
                    c -= 1
                else:
                    if [nums[a], nums[b], nums[c]] not in results:
                        results.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
            a += 1
        return results


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
# [-4, -1, -1, 0, 1, 2] -> [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum([0, 0, 0]))
print(Solution().threeSum([-1]))
print(Solution().threeSum([]))
