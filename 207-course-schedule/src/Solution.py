from graphs.Graph import Graph, GraphNode
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        for a, b in prerequisites:
            if a == b:
                return False
        graph: Graph[int] = self.generateGraph(numCourses, prerequisites)
        in_deg_map: dict[int, int] = self.generateInDegMapping(graph)
        queue: deque[int] = deque()
        for node_id, indeg in in_deg_map.items():
            if indeg == 0:
                queue.append(node_id)
        completed: int = 0

        while queue:
            curr_node_id = queue.popleft()
            completed += 1 
            currNbrs: list[GraphNode[int]] = graph.neighbors(curr_node_id)
            for nbr in currNbrs:
                in_deg_map[nbr.id] -= 1
                if in_deg_map[nbr.id] == 0:
                    queue.append(nbr.id)
        return completed == numCourses

    @staticmethod
    def generateGraph(numCourses: int, prereqs: list[list[int]]) -> Graph[int]:
        graph: Graph[int] = Graph(directed=True)
        for n in range(0, numCourses):
            graph.add_node(n)
        for prereq in prereqs:
            graph.add_edge(v=prereq[1], u=prereq[0])
        return graph
    
    @staticmethod
    def generateInDegMapping(graph:Graph[int]) -> dict[int, int]:
        rslt: dict[int, int] = {node_id:0 for node_id in graph.nodes.keys()}
        for node in graph.nodes.values():
            adjList: list[GraphNode[int]] = node.adjList
            for nbr in adjList:
                rslt[nbr.id] += 1
        return rslt


def main():
    sol:Solution = Solution()
    prerequisites: list[list[int]] = [[1,0]] #,[0,1]]
    numCourses:int = 2
    graph: Graph = sol.generateGraph(numCourses, prerequisites)
    inDegMap = sol.generateInDegMapping(graph)
    print(inDegMap)
    

if __name__ == '__main__':
    main()
  
