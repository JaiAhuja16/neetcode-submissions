class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        L = self.d[key]
        l, r, ans = 0, len(L) - 1, ""
        while l <= r:
            mid = l + (r - l) // 2
            ts, val = L[mid]
            if ts == timestamp:
                return val
            elif ts < timestamp:
                ans = val
                l = mid + 1
            else:
                r = mid - 1
        return ans