class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        max_count = 0
        prev = None
        for x in s:
            if x == prev:
                count += 1
            else:
                prev = x
                count = 1
            max_count = max(max_count, count)

        return max_count