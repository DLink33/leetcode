from trees.UnionFind import UnionFind

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        uf: UnionFind = UnionFind()
        for i in range(len(isConnected)):
            uf.find(i)
        print(uf)

def main():
    sol = Solution()
    isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    sol.findCircleNum(isConnected=isConnected)

if __name__ == '__main__':
    main()
        
