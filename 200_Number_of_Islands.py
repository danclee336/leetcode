class DFSsolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if self.isValid(grid, i, j) and grid[i][j] == '1' :
            grid[i][j] = '0'
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)
        return

    def isValid(self, grid, row, col):
        if row >= 0 and row < self.m and col >= 0 and col < self.n:
            return True
        return False
