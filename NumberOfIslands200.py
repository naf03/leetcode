class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # run DFS on every cell
        # mark cell visited
        # if cell is land and not visit , add to the number of islands
        ROW, COL = len(grid), len(grid[0])
        def dfs(r,c,visited):
            if min(r,c) < 0 or r >= ROW or c >=COL or (r,c) in visited or grid[r][c] == "0":
                return 
            visited.add((r,c))
            #up
            dfs(r-1,c,visited)
            #down
            dfs(r+1,c,visited)
            #left
            dfs(r,c-1,visited)
            #right
            dfs(r,c+1,visited)

        visited = set()
        islands = 0
       
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and grid[r][c] != "0":
                    islands += 1
                    dfs(r,c, visited)
        return islands
   