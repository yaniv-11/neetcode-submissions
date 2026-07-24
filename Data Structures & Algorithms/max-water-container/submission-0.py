class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        count=0
        while l<r:
            cur=(r-l)*min(heights[l],heights[r])
            count=max(cur,count)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return count