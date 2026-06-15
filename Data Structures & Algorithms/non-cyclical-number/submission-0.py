class Solution:
    def isHappy(self, n: int) -> bool:
        def func(n):
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            return s

        slow, fast = n, func(n)
        while slow != fast:
            slow = func(slow)
            fast = func(func(fast))
        return slow == 1