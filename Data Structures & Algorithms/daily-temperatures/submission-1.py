class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        op = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                ind = st.pop()
                op[ind] = i - ind
            st.append(i)
        return op