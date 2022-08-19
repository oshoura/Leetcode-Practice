class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index = 0
        min = -101
        for n in nums:
            if n > min:
                nums[index] = n
                index += 1
                min = n        
        return index
                
