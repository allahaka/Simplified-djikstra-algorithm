import math
import typing


class Edge:
    def __init__(self, from_node: str, to_node: str, weight: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


class Graph:
    def __init__(self, nodes: typing.List[str], edges: typing.List[Edge]) -> None:
        self.nodes = nodes
        self.edges = edges


class Djikstra:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.visited = []
        self.distances = {}
        self.create_distances(self.graph.nodes)

    def create_distances(self, nodes: typing.List[str]):
        for node in nodes:
            self.distances.update({node: {"previous_node": None, "distance": math.inf}})

    def clear_djikstra_table(self):
        self.visited = []
        self.distances = {}
        self.create_distances(self.graph.nodes)

    def distance_from_node_to(self, from_node: str, to_node: str) -> str:
        self.distances.get(from_node)["distance"] = 0
        while True:
            temp_lowest_weight = math.inf
            temp_node = None
            for node in self.graph.nodes:
                if node not in self.visited:
                    if self.distances.get(node)["distance"] < temp_lowest_weight:
                        temp_lowest_weight = self.distances.get(node)["distance"]
                        temp_node = node
            if temp_node is None:
                break
            for edge in self.graph.edges:
                if edge.from_node == temp_node:
                    temp_dst = self.distances[temp_node]["distance"] + edge.weight
                    if self.distances[edge.to_node]["distance"] > temp_dst:
                        self.distances[edge.to_node]["distance"] = temp_dst
                        self.distances[edge.to_node]["previous_node"] = temp_node
            self.visited.append(temp_node)
        return f"Shortest distance from {from_node} to {to_node} " \
               f"is {self.distances.get(to_node).get('distance')}"


def ask_for_nodes() -> typing.List[str]:
    nodes = input("Provide names of nodes seperated with ;\n")
    nodes = nodes.replace(" ", '')
    list_nodes = nodes.split(';')
    nodes = []
    for node in list_nodes:
        nodes.append(node)
    return nodes


def ask_for_edges() -> typing.List[Edge]:
    print("Provide edges one by one in format: Name_node_from:Name_node_to:Weight   weight is an int")
    print("To finish input empty node")
    edges = []
    while True:
        edge = input()
        if edge == "":
            break
        edge = edge.split(':')
        edges.append(Edge(edge[0], edge[1], int(edge[2])))
    return edges


def which_nodes() -> typing.Tuple[str, str]:
    node_from = input("Provide name of node you want to get distance from:\n")
    node_to = input("Provide name of node you want to get distance to:\n")
    return node_from, node_to


def is_true(inp: typing.Any) -> bool:
    return inp.lower() in ["yes", "y", "1", "t", "tak", True, 1]


def main(djikstra: Djikstra = None) -> None:
    if not djikstra:
        nodes = ask_for_nodes()
        edges = ask_for_edges()
        graph = Graph(nodes, edges)
        djikstra = Djikstra(graph)
    node_from, node_to = which_nodes()
    result = djikstra.distance_from_node_to(node_from, node_to)
    print(result)
    repeat = input("Do you want to calculate another distance?")
    if is_true(repeat):
        same_graph = input("Do you want to use same graph?")
        if is_true(same_graph):
            djikstra.clear_djikstra_table()
            main(djikstra)
        else:
            main()
    else:
        quit(0)


if __name__ == "__main__":
    main()
