# ==============================================================================
# DATA PETA DAN HEURISTIK 
# ==============================================================================

graph = {
    'Cilegon': {'Tangerang': 81},
    'Tangerang': {'Cilegon': 81, 'Jakarta': 29},
    'Jakarta': {'Tangerang': 29, 'Depok': 25, 'Bekasi': 22},
    'Depok': {'Jakarta': 25, 'Bogor': 44},
    'Bogor': {'Depok': 44, 'Sukabumi': 57},
    'Bekasi': {'Jakarta': 22, 'Subang': 95},
    'Sukabumi': {'Bogor': 57, 'Bandung': 89},
    'Subang': {'Bekasi': 95, 'Indramayu': 56, 'Bandung': 61},
    'Bandung': {'Sukabumi': 89, 'Subang': 61, 'Cirebon': 106, 'Tasikmalaya': 83},
    'Indramayu': {'Subang': 56, 'Cirebon': 56},
    'Cirebon': {'Indramayu': 56, 'Bandung': 106, 'Tegal': 71},
    'Tasikmalaya': {'Bandung': 83, 'Purwokerto': 113, 'Cilacap': 96},
    'Tegal': {'Cirebon': 71, 'Pekalongan': 70, 'Purwokerto': 65},
    'Pekalongan': {'Tegal': 70, 'Semarang': 83},
    'Purwokerto': {'Tasikmalaya': 113, 'Tegal': 65, 'Cilacap': 42, 'Kebumen': 51, 'Magelang': 107},
    'Cilacap': {'Tasikmalaya': 96, 'Purwokerto': 42, 'Kebumen': 70},
    'Kebumen': {'Purwokerto': 51, 'Cilacap': 70, 'Yogyakarta': 81},
    'Semarang': {'Pekalongan': 83, 'Ambarawa': 37, 'Kudus': 50},
    'Ambarawa': {'Semarang': 37, 'Magelang': 35, 'Surakarta': 70},
    'Magelang': {'Purwokerto': 107, 'Ambarawa': 35, 'Yogyakarta': 40},
    'Kudus': {'Semarang': 50, 'Rembang': 62},
    'Yogyakarta': {'Kebumen': 81, 'Magelang': 40, 'Surakarta': 75, 'Pacitan': 107},
    'Rembang': {'Kudus': 62, 'Tuban': 93},
    'Surakarta': {'Ambarawa': 70, 'Yogyakarta': 75, 'Ngawi': 83},
    'Tuban': {'Rembang': 93, 'Bojonegoro': 36},
    'Ngawi': {'Surakarta': 83, 'Bojonegoro': 73, 'Nganjuk': 73},
    'Pacitan': {'Yogyakarta': 107, 'Trenggalek': 108},
    'Bojonegoro': {'Tuban': 36, 'Ngawi': 73, 'Surabaya': 111},
    'Nganjuk': {'Ngawi': 73, 'Surabaya': 118, 'Kepanjen': 98},
    'Trenggalek': {'Pacitan': 108, 'Kepanjen': 114},
    'Surabaya': {'Bojonegoro': 111, 'Nganjuk': 118, 'Sidoarjo': 36},
    'Sidoarjo': {'Surabaya': 36, 'Probolinggo': 56},
    'Kepanjen': {'Nganjuk': 98, 'Trenggalek': 114, 'Lumajang': 108},
    'Probolinggo': {'Sidoarjo': 56, 'Situbondo': 100, 'Lumajang': 75},
    'Lumajang': {'Kepanjen': 108, 'Probolinggo': 75, 'Jember': 65},
    'Situbondo': {'Probolinggo': 100, 'Banyuwangi': 88},
    'Jember': {'Lumajang': 65, 'Banyuwangi': 100},
    'Banyuwangi': {'Situbondo': 88, 'Jember': 100}
}


heuristics = {
    'Cilegon': 950, 'Tangerang': 882, 'Jakarta': 861, 'Bekasi': 840,
    'Depok': 858, 'Bogor': 852, 'Sukabumi': 832, 'Bandung': 780,
    'Subang': 750, 'Indramayu': 700, 'Cirebon': 662, 'Tasikmalaya': 684,
    'Tegal': 595, 'Purwokerto': 571, 'Cilacap': 592, 'Pekalongan': 537,
    'Kebumen': 521, 'Magelang': 463, 'Semarang': 455, 'Ambarawa': 445,
    'Yogyakarta': 440, 'Kudus': 416, 'Surakarta': 396, 'Rembang': 373,
    'Ngawi': 334, 'Pacitan': 357, 'Bojonegoro': 298, 'Tuban': 295,
    'Nganjuk': 276, 'Trenggalek': 289, 'Surabaya': 210, 'Sidoarjo': 196,
    'Kepanjen': 197, 'Probolinggo': 132, 'Lumajang': 122, 'Situbondo': 70,
    'Jember': 71, 'Banyuwangi': 0
}

# ==============================================================================
# ALGORITMA PENCAIRAN
# ==============================================================================

def ucs(graph, start, goal):
    frontier = [(0, [start])]
    explored = set()
    while frontier:
        lowest_cost_index = 0
        for i in range(len(frontier)):
            if frontier[i][0] < frontier[lowest_cost_index][0]:
                lowest_cost_index = i
        cost, path = frontier.pop(lowest_cost_index)
        current_node = path[-1]
        if current_node == goal: return path, cost
        if current_node in explored: continue
        explored.add(current_node)
        for neighbor, distance in graph[current_node].items():
            if neighbor not in explored:
                new_cost = cost + distance
                new_path = path + [neighbor]
                frontier.append((new_cost, new_path))
    return None, float('inf')

def gbfs(graph, start, goal, heuristics):
    frontier = [(heuristics[start], [start])]
    explored = set()
    while frontier:
        best_h_index = 0
        for i in range(len(frontier)):
            if frontier[i][0] < frontier[best_h_index][0]:
                best_h_index = i
        h_val, path = frontier.pop(best_h_index)
        current_node = path[-1]
        if current_node == goal:
            total_cost = 0
            for i in range(len(path) - 1): total_cost += graph[path[i]][path[i+1]]
            return path, total_cost
        if current_node in explored: continue
        explored.add(current_node)
        for neighbor in graph[current_node].keys():
            if neighbor not in explored:
                new_path = path + [neighbor]
                frontier.append((heuristics[neighbor], new_path))
    return None, float('inf')

def a_star(graph, start, goal, heuristics):
    frontier = [(heuristics[start], 0, [start])]
    explored = set()
    while frontier:
        best_f_index = 0
        for i in range(len(frontier)):
            if frontier[i][0] < frontier[best_f_index][0]:
                best_f_index = i
        f_cost, g_cost, path = frontier.pop(best_f_index)
        current_node = path[-1]
        if current_node == goal: return path, g_cost
        if current_node in explored: continue
        explored.add(current_node)
        for neighbor, distance in graph[current_node].items():
            if neighbor not in explored:
                new_g_cost = g_cost + distance
                new_f_cost = new_g_cost + heuristics[neighbor]
                new_path = path + [neighbor]
                frontier.append((new_f_cost, new_g_cost, new_path))
    return None, float('inf')

def ids(graph, start, goal):
    def dls(start, goal, limit, path):
        if start == goal: return path
        if limit <= 0: return None
        for neighbor in graph[start].keys():
            if neighbor not in path:
                new_path = path + [neighbor]
                result = dls(neighbor, goal, limit - 1, new_path)
                if result is not None: return result
        return None
    depth = 1
    while True:
        result_path = dls(start, goal, depth, [start])
        if result_path is not None:
            total_cost = 0
            for i in range(len(result_path) - 1): total_cost += graph[result_path[i]][result_path[i+1]]
            return result_path, total_cost
        depth += 1

# ==============================================================================
# EKSEKUSI PROGRAM
# ==============================================================================

print("--- Uniform Cost Search (UCS) Tanpa Library ---")
ucs_path, ucs_cost = ucs(graph, 'Cilegon', 'Banyuwangi')
print(f"Rute: {' -> '.join(ucs_path)}")
print(f"Total Jarak: {ucs_cost} km")

print("\n--- Iterative Deepening Search (IDS) ---")
ids_path, ids_cost = ids(graph, 'Cilegon', 'Banyuwangi')
print(f"Rute: {' -> '.join(ids_path)}")
print(f"Total Jarak: {ids_cost} km (ditemukan pada kedalaman {len(ids_path)})")

print("\n--- Greedy Best-First Search (GBFS) Tanpa Library ---")
gbfs_path, gbfs_cost = gbfs(graph, 'Cilegon', 'Banyuwangi', heuristics)
print(f"Rute: {' -> '.join(gbfs_path)}")
print(f"Total Jarak: {gbfs_cost} km")

print("\n--- A* Search Tanpa Library ---")
astar_path, astar_cost = a_star(graph, 'Cilegon', 'Banyuwangi', heuristics)
print(f"Rute: {' -> '.join(astar_path)}")
print(f"Total Jarak: {astar_cost} km")