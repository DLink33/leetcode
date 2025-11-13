class UnionFind:
    def __init__(self, numNodes:int):
        self.parent = list(range(numNodes+1))
        self.rank = [-1] * (numNodes +1)

    def find(self, x:int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x:int, y:int) -> bool:

        # Compress and get the parents of each input
        root_of_x:int = self.find(x)
        root_of_y:int = self.find(y)

        # They are already on the same team; no need to union()
        if root_of_y == root_of_x:
            return False 
        
        # add the parent with the smaller rank to that of the larger rank
        if self.rank[root_of_x] < self.rank[root_of_y]:
            self.parent[root_of_x] = root_of_y

        elif self.rank[root_of_x] > self.rank[root_of_y]:
            self.parent[root_of_y] = root_of_x

        else:
            self.parent[root_of_y] = root_of_x
            self.rank[root_of_x] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        dsu: UnionFind = UnionFind(len(edges))

        for edge in edges:
            if not dsu.union(edge[0],edge[1]):
                return edge
            
        return []


def main():
    # Smoke Test
    nodes: list[list[int]] = [[1,2],[1,3],[2,3]]
    sol: Solution = Solution()
    rslt: list[int] = sol.findRedundantConnection(nodes)
    print(rslt)


if __name__ == '__main__':
    main()
  
