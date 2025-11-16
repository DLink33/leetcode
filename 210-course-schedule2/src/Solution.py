from graphs.Graph import Graph, GraphNode
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        for a, b in prerequisites:
            if a == b:
                return []
        graph: Graph[int] = self.generateGraph(numCourses, prerequisites)
        in_deg_map: dict[int, int] = self.generateInDegMapping(graph)
        queue: deque[int] = deque()
        order: list[int] = []

        for node_id, indeg in in_deg_map.items():
            if indeg == 0:
                queue.append(node_id)
        
        while queue:
            curr_node_id = queue.popleft()
            order.append(curr_node_id)
            currNbrs: list[GraphNode[int]] = graph.neighbors(curr_node_id)
            for nbr in currNbrs:
                in_deg_map[nbr.id] -= 1
                if in_deg_map[nbr.id] == 0:
                    queue.append(nbr.id)
        
        if len(order) != numCourses:
            return []
        return order
        

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
    sol: Solution = Solution()
    # prerequsites: list[list[int]] = [[1,0],[2,0],[3,1],[3,2]]
    # numCourses:int = 4
    # order: list[int] = sol.findOrder(numCourses=numCourses,prerequisites=prerequsites)
    # print(order)

    prerequsites: list[list[int]] = [[1,0],[2,0],[3,1],[3,2],[2,3]]
    numCourses:int = 4
    order: list[int] = sol.findOrder(numCourses=numCourses,prerequisites=prerequsites)
    print(order)



if __name__ == '__main__':
    main()
  
