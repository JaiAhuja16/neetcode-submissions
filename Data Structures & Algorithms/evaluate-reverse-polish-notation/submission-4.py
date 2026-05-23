class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i == "+":
                st.append(st.pop() + st.pop())
            elif i == "-":
                a = st.pop()
                b = st.pop()
                st.append(b - a)
            elif i == "*":
                st.append(st.pop() * st.pop())
            elif i == "/":
                a = st.pop()
                b = st.pop()
                st.append(int(b / a))
            else:
                st.append(int(i))
            # print(st)
        return st[-1]