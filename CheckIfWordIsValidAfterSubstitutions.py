# Time complexity o(N)
# space complrxity O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "c" and stack[-2:] == ["a", "b"]:
                stack.pop()
                stack.pop()
            else:
                stack.append(c)
        return not stack

