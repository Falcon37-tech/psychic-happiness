Today's Problem is -

Given a square matrix mat[][] of size n x n. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space. 

Examples:

Input: mat[][] = [[1, 2, 3],
                [4, 5, 6]
                [7, 8, 9]]
Output: Rotated Matrix:
[3, 6, 9]
[2, 5, 8]
[1, 4, 7]
Input: mat[][] = [[1, 2],
                [3, 4]]
Output: Rotated Matrix:
[2, 4]
[1, 3]
Constraints:
1 ≤ n ≤ 102
0 <= mat[i][j] <= 103

Solution
Code-

class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                
        for j in range(n):
            for i in range(n//2):
                mat[i][j], mat[n-1-i][j] = mat[n-1-i][j], mat[i][j]
        return mat
