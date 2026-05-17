class Solution:
    def trap(self, height: List[int]) -> int:
        # water traps in     P1--D--P2
        n = len(height)
        st = []
        amt = 0
        depth = 0
        for i in range(n):
            if st:
                while st and height[st[-1]] < height[i]:
                    depth = min(height[st[-1]], height[i])
                    st.pop()
                    if st:
                        amt += (min(height[st[-1]], height[i]) - depth) * (i - st[-1] - 1)
            st.append(i)
        return amt