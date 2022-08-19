class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        result = nums1 + nums2
        result.sort()
        
        listLen = len(result)
        if listLen % 2 == 0:
            return (result[int((listLen-1)/2)] + result[int((listLen-1)/2) + 1])/2
        else:
            return (result[int((listLen-1)/2)])