class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                base=j-i
                if area<=min(heights[i],heights[j])*base:
                    area=min(heights[i],heights[j])*base
        return area