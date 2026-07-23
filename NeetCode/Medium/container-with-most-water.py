class Solution:
    def maxArea(self, heights):
        leftPointer = 0
        rightPointer = len(heights) - 1
        maxArea = 0

        while (leftPointer < rightPointer):
            width = rightPointer - leftPointer
            height = min(heights[leftPointer], heights[rightPointer])

            currentArea = width * height
            maxArea = max(maxArea, currentArea)

            if (heights[leftPointer] < heights[rightPointer]):
                leftPointer += 1
            else:
                rightPointer -= 1
        
        return maxArea
