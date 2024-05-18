class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area = 0
        for root,height in enumerate(heights):
            prev_position = root
            while stack and stack[-1][1]>height:
                prev_position,prev_height = stack.pop()
                area = (root-prev_position)*prev_height
                max_area=max(area,max_area)
            stack.append((prev_position,height))
        for root,height in stack:
            max_area = max(max_area,height*(len(heights)-root))
        return max_area