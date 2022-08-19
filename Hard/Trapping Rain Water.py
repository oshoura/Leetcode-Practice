class Solution:
    def trap(self, height: List[int]) -> int:
        #max heights from left to right
        leftToRightMax = {}
        maxHeight = 0
        for i in range(len(height)):
            if height[i] > maxHeight:
                maxHeight = height[i]
            leftToRightMax[i] = maxHeight
        #max heights from right to left
        rightToLeftMax = {}
        maxHeight = 0
        for i in range(len(height))[::-1]:
            if height[i] > maxHeight:
                maxHeight = height[i]
            rightToLeftMax[i] = maxHeight
            #calculated filled in heights
        filledHeights = [min(rightToLeftMax[i],leftToRightMax[i]) for i in range(len(height))]
        water = 0
        for i in range(len(height)):
            water += (filledHeights[i] - height[i])
        return water
        