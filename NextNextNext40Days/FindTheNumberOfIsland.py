Today's Problem is-

Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid[][] = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]
Output: 4
Explanation:
The image below shows all the 4 islands in the grid.
 
Input: grid[][] = [['W', 'L', 'L', 'L', 'W', 'W', 'W'], ['W', 'W', 'L', 'L', 'W', 'L', 'W']]
Output: 2
Expanation:
The image below shows 2 islands in the grid.
 
Constraints:
1 ≤ n, m ≤ 500
grid[i][j] = {'L', 'W'}

Solution
Code-
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        n,m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        
        directions = [(-1,0),(1,0), (0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        def dfs(i,j):
            visited[i][j] = True
            for dx, dy in directions:
                ni, nj = i +dx, j + dy
                if 0<= ni<n and 0 <=nj <m:
                    if not visited[ni][nj] and grid[ni][nj] == 'L':
                        dfs(ni, nj)
                        
        island_count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L' and not visited[i][j]:
                    island_count += 1
                    dfs(i,j)
        return island_count
