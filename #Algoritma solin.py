#Algoritma solin
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph

    def solin_algorithm(self, start, end):
        # Initialize distances and predecessors
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        predecessors = {node: None for node in self.graph}
        
        # Set of unvisited nodes
        unvisited = set(self.graph.keys())

        while unvisited:
            # Get the node with the smallest distance
            current_node = min(unvisited, key=lambda node: distances[node])
            unvisited.remove(current_node)

            # If we reached the end node
            if current_node == end:
                break

            # Update distances for neighbors
            for neighbor, weight in self.graph[current_node]:
                if neighbor in unvisited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = current_node

        return distances[end], predecessors

    def get_path(self, start, end):
        total_cost, predecessors = self.solin_algorithm(start, end)
        path = []
        current_node = end
        while current_node is not None:
            path.append(current_node)
            current_node = predecessors[current_node]
        path.reverse()
        return path, total_cost


def main():
    g = Graph()
    
    # Add edges based on your provided data
    g.add_edge('A', 'B', 75)
    g.add_edge('B', 'C', 80)
    g.add_edge('C', 'D', 130)
    g.add_edge('B', 'E', 90)
    g.add_edge('E', 'F', 80)
    g.add_edge('F', 'G', 120)
    g.add_edge('G', 'H', 80)
    g.add_edge('G', 'M', 100)
    g.add_edge('M', 'N', 150)
    g.add_edge('C', 'I', 130)
    g.add_edge('I', 'J', 120)
    g.add_edge('J', 'K', 140)
    g.add_edge('I', 'L', 125)
    g.add_edge('L', 'O', 110)
    g.add_edge('O', 'P', 130)

    start_node = 'A'
    end_node = 'P'
    
    path, total_cost = g.get_path(start_node, end_node)
    
    print(f'Total cost from {start_node} to {end_node}: {total_cost}')
    print(f'Path: {" -> ".join(path)}')

main()
