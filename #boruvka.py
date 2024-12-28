#boruvka
class Graph:
    def __init__(self):
        self.edges = []  # List untuk menyimpan semua edge

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))  # Menambahkan edge sebagai (weight, start_vertex, end_vertex)

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])  # Mencari root dari node

    def union(self, parent, rank, xroot, yroot):
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1  # Menggabungkan dua subset

    def boruvka_mst(self):
        # Membuat pemetaan dari vertex ke indeks
        vertex_map = {vertex: index for index, vertex in enumerate(set(u for _, u, _ in self.edges) | set(v for _, _, v in self.edges))}
        
        num_vertices = len(vertex_map)  # Jumlah vertex
        parent = []
        rank = []
        
        # Inisialisasi V pohon yang berbeda
        for node in range(num_vertices):
            parent.append(node)
            rank.append(0)

        num_trees = num_vertices  # Awalnya ada V pohon
        mst_weight = 0  # Inisialisasi bobot MST

        while num_trees > 1:
            cheapest = [None] * num_vertices  # Inisialisasi array cheapest untuk setiap komponen

            # Mencari edge termurah untuk setiap komponen
            for weight, u, v in self.edges:
                set_u = self.find_parent(parent, vertex_map[u])
                set_v = self.find_parent(parent, vertex_map[v])

                if set_u != set_v:  # Hanya mempertimbangkan edge yang menghubungkan pohon yang berbeda
                    if cheapest[set_u] is None or cheapest[set_u][0] > weight:
                        cheapest[set_u] = (weight, u, v)
                    if cheapest[set_v] is None or cheapest[set_v][0] > weight:
                        cheapest[set_v] = (weight, u, v)

            # Menambahkan edge termurah ke MST
            for i in range(num_vertices):
                if cheapest[i] is not None:
                    weight, u, v = cheapest[i]
                    set_u = self.find_parent(parent, vertex_map[u])
                    set_v = self.find_parent(parent, vertex_map[v])

                    if set_u != set_v:  # Jika mereka tidak berada di pohon yang sama
                        mst_weight += weight
                        self.union(parent, rank, set_u, set_v)
                        print(f"Edge {u} - {v} with weight {weight} included in MST")  # Menampilkan edge yang ditambahkan ke MST

            num_trees -= 1  # Mengurangi jumlah pohon

        print(f"Total weight of MST is {mst_weight}")  # Menampilkan total bobot MST

    def find_shortest_path(self, start, end):
        from collections import deque
        
        # Membuat representasi graf untuk pencarian rute terpendek
        adj_list = {vertex: [] for weight, u, v in self.edges for vertex in (u, v)}  # Inisialisasi adj_list dengan semua vertex
        
        for weight, u, v in self.edges:
            adj_list[u].append((v, weight))  # Menambahkan edge ke daftar adjacency
            adj_list[v].append((u, weight))

        # Melakukan BFS untuk menemukan rute terpendek
        queue = deque([start])
        visited = {start: None}  # Melacak node yang dikunjungi dan orang tua mereka

        while queue:
            current = queue.popleft()
            if current == end:  # Jika mencapai node tujuan
                break
            
            for neighbor, _ in adj_list[current]:
                if neighbor not in visited:  # Jika neighbor belum dikunjungi
                    visited[neighbor] = current
                    queue.append(neighbor)

        # Membangun rute dari akhir ke awal
        path = []
        while end is not None:
            path.append(end)
            end = visited.get(end)  # Menggunakan get untuk menghindari KeyError
        
        path.reverse()  # Balik untuk mendapatkan dari awal ke akhir
        return path

def main():
    g = Graph()
    
    # Menambahkan edges berdasarkan data yang diberikan
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

    print("Minimum Spanning Tree:")
    g.boruvka_mst()  # Menampilkan MST

    start_node = 'A'
    end_node = 'P'
    
    shortest_path = g.find_shortest_path(start_node, end_node)  # Mencari rute terpendek
    
    print(f"Shortest path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")  # Menampilkan rute terpendek
    
    total_cost = sum(weight for weight, u, v in g.edges if (u in shortest_path and v in shortest_path) and (shortest_path.index(u) + 1 == shortest_path.index(v) or shortest_path.index(v) + 1 == shortest_path.index(u)))
    
    print(f"Total cost of shortest path: {total_cost}")  # Menampilkan total biaya rute terpendek

main()
