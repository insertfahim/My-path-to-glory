class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for position,temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                prev_idx,prev_temp = stack.pop()
                days_needed = position-prev_idx
                answer[prev_idx]=days_needed
            stack.append((position,temp))
        return answer