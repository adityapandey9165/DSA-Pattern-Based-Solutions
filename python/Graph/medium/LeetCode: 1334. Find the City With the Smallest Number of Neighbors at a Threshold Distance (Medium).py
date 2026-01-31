"""
LeetCode: 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance (Medium)
Problem Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
Author: Aditya Pandey
Date: 2026-01-31

--------------------------------------------------
Problem:
You are given:
- n cities numbered from 0 to n-1
- edges where edges[i] = [from, to, weight]
- distanceThreshold

For each city, find how many other cities are reachable
with distance ≤ distanceThreshold.

Return the city with:
- the smallest number of reachable cities
- if tie → return the city with the greatest index

--------------------------------------------------
Pattern:
Graph + Dijkstra (Single Source Shortest Path)

--------------------------------------------------
Approach:
1. Build an adjacency list for the graph.
2. For each city `i`:
   - Run Dijkstra's algorithm to compute shortest distances
     from city `i` to all other cities.
   - Count how many cities are reachable with:
         0 < distance ≤ distanceThreshold
3. Track the city with the minimum reachable count.
4. In case of tie, choose the city with the larger index
   (handled by using `<=` in comparison).

--------------------------------------------------
Why Dijkstra Works:
- Graph is weighted
- Need shortest paths
- Repeating Dijkstra from every node ensures correctness

--------------------------------------------------
Time Complexity:
- Dijkstra per city: O(E log V)
- Total: O(V * E log V)

Space Complexity:
- O(V + E) for adjacency list and distance array

--------------------------------------------------
Things People Commonly Miss:
1. Do NOT count the city itself (distance = 0).
2. Use `<=` while updating result to handle tie-breaking
   toward larger index.
3. Skip outdated heap entries using:
       if d > dist[node]: continue
4. This is NOT BFS — weights require Dijkstra.
--------------------------------------------------
"""

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Dijkstra from a single source
        def dijkstra(src: int) -> List[int]:
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)]

            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue

                for nei, w in adj[node]:
                    nd = d + w
                    if nd < dist[nei]:
                        dist[nei] = nd
                        heapq.heappush(pq, (nd, nei))

            return dist

        min_reachable = float('inf')
        city = -1

        # Run Dijkstra from each city
        for i in range(n):
            dist = dijkstra(i)
            reachable = sum(1 for d in dist if 0 < d <= distanceThreshold)

            # <= ensures we pick the larger index in case of tie
            if reachable <= min_reachable:
                min_reachable = reachable
                city = i

        return city


# -----------------------
# Local Testing
# -----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheCity(
        4,
        [[0,1,3],[1,2,1],[1,3,4],[2,3,1]],
        4
    ))
    # Expected: 3
