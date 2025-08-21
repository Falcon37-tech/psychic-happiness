Today's Problem is-

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v.

Examples:

Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]

Output: true
Explanation: The diagram clearly shows a cycle 0 → 2 → 0
Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]

Output: false
Explanation: no cycle in the graph
Constraints:
1 ≤ V, E ≤ 10^5
u ≠ v



Solution
Code-
class Solution:
    def isCycle(self, V, edges):
        from collections import defaultdict
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            
        visited = [False]*V
        recStack = [False]*V
        
        def dfs(node):
            visited[node] = True
            recStack[node] = True
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif recStack[neighbor]:
                    return True
                    
            recStack[node] = False
            return False
            
        for v in range(V):
            if not visited[v]:
                if dfs(v):
                    return True
        return False
