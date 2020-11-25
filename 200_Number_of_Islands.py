class DFSsolution: # Time: O(M*N), Space(M*N)
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

from collections import deque
class BFSsolution: #Time: O(M*N), Space: O(min(M,N))
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        count = 0
        self.queue = deque()
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == '1':
                    self.queue.append((i,j))
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        while self.queue:
            r, c = self.queue.popleft()
            if self.isValid(grid, r, c) and grid[r][c] == '1' :
                grid[r][c] = '0'
                self.queue.append((r - 1, c))
                self.queue.append((r + 1, c))
                self.queue.append((r, c - 1))
                self.queue.append((r, c + 1))
        return

    def isValid(self, grid, row, col):
        if row >= 0 and row < self.m and col >= 0 and col < self.n:
            return True
        return False


class UnionFindSolution: # Time: O(M*N), Space(M*N)
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        rows = len(grid); cols = len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(rows) for j in range(cols))
        parent = list(range(rows*cols))
        rank = [0] * rows*cols

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> None: #optimized by union by rank
            xroot = find(x)
            yroot = find(y)
            if xroot == yroot: return
            if rank[xroot] < rank[yroot]:
                xroot, yroot = yroot, xroot
            parent[yroot] = xroot
            rank[xroot] = max(rank[xroot], rank[yroot]+1) #using height as rank
            self.count -= 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0':
                    continue
                index = i*cols + j
                if j < cols-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < rows-1 and grid[i+1][j] == '1':
                    union(index, index+cols)
        return self.count
