class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {'}':'{', ')':'(', ']':'['}
        for i in s:
            if st:
                if i in d and st[-1] == d[i]:
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        return not st