import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Untuk graf tidak terarah

    def solin_algorithm(self, start, end):
        # Inisialisasi jarak dan pendahulu
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        predecessors = {node: None for node in self.graph}
        
        # Priority queue untuk menyimpan (jarak, node)
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Jika sudah mencapai node akhir
            if current_node == end:
                break

            # Jika jarak saat ini lebih besar dari jarak yang diketahui
            if current_distance > distances[current_node]:
                continue

            # Perbarui jarak untuk tetangga
            for neighbor, weight in self.graph[current_node]:
                new_distance = current_distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor))

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
    
    # Menambahkan sisi berdasarkan data yang diberikan
    g.add_edge('A', 'B', 75)
    g.add_edge('B', 'C', 80)
    g.add_edge('C', 'D', 130)
    g.add_edge('B', 'E', 90)
    g.add_edge('E', 'F', 80)
    g.add_edge('E', 'H', 130)
    g.add_edge('H', 'G', 80)
    g.add_edge('F', 'G', 120)
    g.add_edge('G', 'M', 100)
    g.add_edge('H', 'M', 110)
    g.add_edge('M', 'N', 150)
    g.add_edge('N', 'O', 200)
    g.add_edge('C', 'I', 120)
    g.add_edge('D', 'J', 80)
    g.add_edge('I', 'J', 120)
    g.add_edge('J', 'K', 140)
    g.add_edge('I', 'L', 130)
    g.add_edge('L', 'O', 115)
    g.add_edge('K', 'O', 130)
    g.add_edge('O', 'P', 130)


    start_node = 'A'
    end_node = 'P'
    
    path, total_cost = g.get_path(start_node, end_node)
    
    print(f'Total cost from {start_node} to {end_node}: {total_cost}')
    print(f'Path: {" -> ".join(path)}')

main()
