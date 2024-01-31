class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output, stack,  = [0 for _ in temperatures], []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                i0, _ = stack.pop()
                output[i0] = i - i0
            stack.append((i, t))
        return output

