class Solution(object):
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def dfs(i, current, total):
            if total == target:
                result.append(current[:])
                return
            elif i >= len(candidates) or total > target:
                return
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i+1, current, total)
        dfs(0, [], 0)
        return result

a = Solution()
print(a.combinationSum([2,3,6,7],7))
print(a.combinationSum([2,3,5],8))
print(a.combinationSum([2],1))