class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # memo = {}
        # def f(index):
        #     if index >= n:
        #         return 1
        #     if index in memo:
        #         return memo[index]
        #     if s[index] == '0':
        #         return 0
        #     memo[index] = f(index + 1) + (f(index + 2) if index < n - 1 and 10 <= int(s[index] + s[index + 1]) <= 26 else 0)
        #     return memo[index]
        # return f(0)

        last = 1
        second_last = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                curr = 0
            else:
                curr = second_last
                if i < n - 1 and 10 <= int(s[i] + s[i + 1]) <= 26:
                    curr += last
            last = second_last
            second_last = curr
        return curr