# time complexity o(N)
# space complexit
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_indecis = {c: i for i, c in enumerate(S)}
        end = start = 0
        ans = []

        for i, c in enumerate(S):
            end = max(end, last_indecis[c])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans