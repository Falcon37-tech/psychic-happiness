Today's Problem is-

Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false.

Examples:

Input: V = 4, E = 3, edges[][] = [[3, 0], [1, 0], [2, 0]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
Input: V = 6, E = 6, edges[][] = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]

Output: true
Explanation: The output true denotes that the order is valid. Few valid Topological orders for the graph are:
[4, 5, 0, 1, 2, 3]
[5, 2, 4, 0, 1, 3]
Constraints:
2  ≤  V  ≤  5 x 10^3
1  ≤  E = edges.size()  ≤  min[10^5, (V * (V - 1)) / 2]

Solution
Code-
from collections import deque, defaultdict
class Solution:
    
    def topoSort(self, V, edges):
        adj = defaultdict(list)
        indegree = [0]*V
        for u,v in edges:
            adj[u].append(v)
            indegree[v] += 1
            
        queue = deque([i for i in range(V) if indegree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return topo_order if len(topo_order) == V else []
        
    @staticmethod
    def check(V, res, edges):
        pos = [0]*V
        for i in range(V):
            pos[res[i]] = i
            
        for u , v in edges:
            if pos[u] > pos[v]:
                return False
        return True
    
