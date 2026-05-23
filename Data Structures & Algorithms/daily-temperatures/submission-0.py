class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        i = 0
        n = len(temperatures)
        op = [0] * n
        for i in range(n):
            if st:
                if temperatures[i] > temperatures[st[-1]]:
                    while st and temperatures[i] > temperatures[st[-1]]:
                        ind = st.pop()
                        op[ind] = i - ind
                    st.append(i)
            st.append(i)
        return op