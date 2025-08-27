Today's Problem is-

Given a connected undirected graph represented by adjacency list, adjList[][] with n nodes, having a distinct label from 0 to n-1, where each adj[i] represents the list of vertices connected to vertex i.

Create a clone of the graph, where each node in the graph contains an integer val and an array (neighbors) of nodes, containing nodes that are adjacent to the current node.

class Node {
    val: integer
    neighbors: List[Node]
}
Your task is to complete the function cloneGraph( ) which takes a starting node of the graph as input and returns the copy of the given node as a reference to the cloned graph.

Note: If you return a correct copy of the given graph, then the driver code will print true; and if an incorrect copy is generated or when you return the original node, the driver code will print false.

Examples :

Input: n = 4, adjList[][] = [[1, 2], [0, 2], [0, 1, 3], [2]]
Output: true
Explanation: 

As the cloned graph is identical to the original one the driver code will print true.
Input: n = 3, adjList[][] = [[1, 2], [0], [0]]
Output: true
Explanation: 

As the cloned graph is identical to the original one the driver code will print true.
Constraints:
1 ≤ n ≤ 10^4
0 ≤ no. of edges ≤ 10^5
0 ≤ adjList[i][j] < n

Solution
Code-
#User function Template for python3

'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''

class Solution():
    def cloneGraph(self, node):
        if not node:
            return None
            
        visited = {}
            
        def dfs(curr):
            if curr in visited:
                return visited[curr]
                
            clone = Node(curr.val)
            visited[curr] = clone
                
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))
                
            return clone
            
        return dfs(node)
