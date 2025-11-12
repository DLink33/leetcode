from trees.UnionFind import UnionFind

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return len(uf)


def main():
    # Smoke Test
    sol:Solution = Solution()
    isConnected: list[list[int]] = [[1,1,0],[1,1,0],[0,0,1]]
    rslt: int = sol.findCircleNum(isConnected)
    print(rslt)


if __name__ == '__main__':
    main()
        
