class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= len(grid):
                return 0
            elif y < 0 or y >= len(grid[0]):
                return 0
            elif grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            area = 0
            area += dfs(x + 1, y)
            area += dfs(x - 1, y)
            area += dfs(x, y + 1)
            area += dfs(x, y - 1)
            return 1 + area
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                area = dfs(x, y)
                res = max(res, area)
        return res

