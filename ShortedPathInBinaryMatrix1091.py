from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        
        queue = deque()
        def bfs(grid):
            if grid[0][0]==1:
                return -1
            length=1
            queue.append((0,0))
            visited.add((0,0))
            while len(queue)>0:
                for i in range(len(queue)):
                    x, y = queue.popleft()
                    if x==ROW-1 and y==COL-1:
                        return length
                    diff = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,1],[1,-1]]
                    for dx, dy in diff:
                        newx, newy = dx+x, dy+y
                        if min(newx, newy) < 0 or newx == ROW or newy == COL or (newx, newy) in visited or grid[newx][newy]==1:
                            continue
                        queue.append((newx, newy))
                        visited.add((newx,newy))
                length+=1
            return -1
        return bfs(grid)




        