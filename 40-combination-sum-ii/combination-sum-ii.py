class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = []

        def dfs(i, val, curr: list):
            if val == target:
                res.append(curr[:])
                return

            for j in range(i, n):
                if j > 0 and candidates[j] == candidates[j-1] and j > i:
                    continue
                if candidates[j] + val > target:
                    break
                curr.append(candidates[j])
                dfs(j+1, candidates[j] + val, curr)
                curr.pop()

        dfs(0, 0, [])
        return res