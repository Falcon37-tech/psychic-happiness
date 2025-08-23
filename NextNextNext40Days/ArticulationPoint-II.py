Today's Problem is-

You are given an undirected graph with V vertices and E edges. The graph is represented as a 2D array edges[][], where each element edges[i] = [u, v] indicates an undirected edge between vertices u and v.
Your task is to return all the articulation points (or cut vertices) in the graph.
An articulation point is a vertex whose removal, along with all its connected edges, increases the number of connected components in the graph.

Note: The graph may be disconnected, i.e., it may consist of more than one connected component.
If no such point exists, return {-1}.

Examples :

Input: V = 5, edges[][] = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]

Output: [1, 4]
Explanation: Removing the vertex 1 or 4 will disconnects the graph as-
   
Input: V = 4, edges[][] = [[0, 1], [0, 2]]
Output: [0]
Explanation: Removing the vertex 0 will increase the number of disconnected components to 3.  
Constraints:
1 ≤ V, E ≤ 10^4

Solution
Code-
class Solution:
    
    @staticmethod
    def constructAdj(V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return adj
        
    @staticmethod
    def findPoints(adj, u, visited, disc, low, time, parent, isAP):
        visited[u] = 1
        time[0] += 1
        disc[u] = low[u] = time[0]
        children = 0
        
        for v in adj[u]:
            
            if not visited[v]:
                children += 1
                Solution.findPoints(adj, v, visited, disc, low, time, u, isAP)
                
                low[u] = min(low[u], low[v])
                
                if parent != -1 and low[v] >= disc[u]:
                    isAP[u] = 1
            elif v != parent:
                low[u] = min(low[u], disc[v])
        if parent == -1 and children > 1:
            isAP[u] = 1
            
    def articulationPoints(self, V, edges):
        adj = Solution.constructAdj(V, edges)
        disc = [0] * V
        low = [0] * V
        visited = [0] * V
        isAP = [0] * V
        time = [0]
        
        for u in range(V):
            if not visited[u]:
                Solution.findPoints(adj, u, visited, disc, low, time, -1, isAP)
        result = [u for u in range(V) if isAP[u]]
        return result if result else [-1]
