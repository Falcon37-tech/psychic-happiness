Today's Problem is -

Given a matrix mat[][] of dimension n * m where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cell have fresh oranges
2 : Cell have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten. A rotten orange at index (i, j) can rot other fresh orange at indexes (i-1, j), (i+1, j), (i, j-1), (i, j+1) (up, down, left and right) in a unit time.

Note: Your task is to return the minimum time to rot all the fresh oranges. If not possible returns -1.

Examples:

Input: mat[][] = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]
Output: 1
Explanation: Oranges at positions (0,2), (1,2), (2,0) will rot oranges at (0,1), (1,1), (2,2) and (2,1) in unit time.
Input: mat[][] = [[2, 2, 0, 1]]
Output: -1
Explanation: Oranges at (0,0) and (0,1) can't rot orange at (0,3).
Input: mat[][] = [[2, 2, 2], [0, 2, 0]]
Output: 0
Explanation: There is no fresh orange. 
Constraints:
1 ≤ mat.size() ≤ 500
1 ≤ mat[0].size() ≤ 500
mat[i][j] = {0, 1, 2} 

Solution
Code-
from collections import deque
class Solution:
	def orangesRotting(self, mat):
		n = len(mat)
		m = len(mat[0])
		
		queue = deque()
		time = 0
		freshcount = 0
		for i in range(n):
		    for j in range(m):
		        if mat[i][j] == 2:
		            queue.append((i, j, 0))
		        elif mat[i][j] == 1:
		            freshcount += 1
	    directions = [(-1, 0), (1,0), (0,-1), (0,1)]
	    rotted = 0
	    
	    while queue:
	        x, y, currtime = queue.popleft()
	        time = max(time, currtime)
	        
	        for dx, dy in directions:
	            nx, ny = x+dx, y+dy
	            
	            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 1:
	                mat[nx][ny] = 2
	                rotted += 1
	                
	                queue.append((nx,ny,currtime + 1))
	                
	    if rotted != freshcount:
	        return -1
	    return time
