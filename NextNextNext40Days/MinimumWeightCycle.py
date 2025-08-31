Today's Problem is-

Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by a 2d array edges[][], where edges[i] = [u, v, w] represents the edge between the nodes u and v having w edge weight.
Your task is to find the minimum weight cycle in this graph.

Examples:

Input: V = 5, edges[][] = [[0, 1, 2], [1, 2, 2], [1, 3, 1], [1, 4, 1], [0, 4, 3], [2, 3, 4]]

Output: 6
Explanation: 

Minimum-weighted cycle is  0 → 1 → 4 → 0 with a total weight of 6(2 + 1 + 3)
Input: V = 5, edges[][] = [[0, 1, 3], [1, 2, 2], [0, 4, 1], [1, 4, 2], [1, 3, 1], [3, 4, 2], [2, 3, 3]]

Output: 5
Explanation: 

Minimum-weighted cycle is  1 → 3 → 4 → 1 with a total weight of 5(1 + 2 + 2)
Constraints:
1 ≤ V ≤ 100
1 ≤ E = edges.size() ≤ 10^3 
1 ≤ edges[i][j] ≤ 100



Solution

Code-
class Solution:

    def constructadj(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))
        return adj

    def shortestPath(self, V, adj, src, dest):
        dist = [float('inf')] * V
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:

                if (u == src and v == dest) or (u == dest and v == src):
                    continue

                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist[dest]

    def findMinCycle(self, V, edges):
        adj = self.constructadj(V, edges)
        minCycle = float('inf')

        for edge in edges:
            u, v, w = edge
            dist = self.shortestPath(V, adj, u, v)

            if dist != float('inf'):
                minCycle = min(minCycle, dist + w)

        return minCycle
