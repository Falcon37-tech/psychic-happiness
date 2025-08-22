Today's Problem is -

Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u,v] represents the edge between the vertices u and v. Determine whether a specific edge between two vertices (c, d) is a bridge.

Note:

An edge is called a bridge if removing it increases the number of connected components of the graph.
if there’s only one path between c and d (which is the edge itself), then that edge is a bridge.
Examples :

Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 3]], c = 1, d = 2

Output: true
Explanation: From the graph, we can clearly see that blocking the edge 1-2 will result in disconnection of the graph.
Hence, it is a Bridge.
Input: V = 5, edges[][] = [[0, 1], [0, 3], [1, 2], [2, 0], [3, 4]], c = 0, d = 2
 
Output: false
Explanation:
 
Blocking the edge between nodes 0 and 2 won't affect the connectivity of the graph.
So, it's not a Bridge Edge. All the Bridge Edges in the graph are marked with a green line in the above image.
Constraints:
1 ≤ V, E ≤ 10^5
0 ≤ c, d ≤ V-1



Solution
Code-
from collections import defaultdict
class Solution:
    def isBridge(self, V, edges, c, d):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        if d in adj[c]:
            adj[c].remove(d)
            
        if c in adj[d]:
            adj[d].remove(c)
            
        visited = [False]*V
        
        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        dfs(c)
        
        return not visited[d]
