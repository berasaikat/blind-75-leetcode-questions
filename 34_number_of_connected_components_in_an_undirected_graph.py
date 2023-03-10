class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1]*n
        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2]>rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
    
a = Solution()
print(a.countComponents(5,[[0, 1], [1, 2], [3, 4]]))
print(a.countComponents(5,[[0, 1], [1, 2], [2, 3], [3, 4]]))

'''
Leet Code 547. Number of Provinces (Very similar to Number of Connected Components in an Undirected Graph)
class Solution(object):
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        edges = []
        n = len(isConnected)
        for i in range(n):
            for j in range(i):
                if isConnected[i][j] == 1:
                    edges.append([i, j])
        par = [i for i in range(n)]
        rank = [1]*n
        def find(node):
            res = node
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2]>rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
    
a = Solution()
print(a.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(a.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
'''