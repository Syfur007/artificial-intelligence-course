def ucs(adj_matrix, start, goal):
    import heapq
    queue = [(0, start)]
    visited = set()
    costs = {start: 0}
    parent = {start: None}
    while queue:
        cost, node = heapq.heappop(queue)
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in enumerate(adj_matrix[node]):
            if weight and neighbor not in visited:
                new_cost = cost + weight
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    parent[neighbor] = node
                    heapq.heappush(queue, (new_cost, neighbor))
    return None, float('inf')

# Example usage:
if __name__ == "__main__":
    # 0:A, 1:B, 2:C, 3:D, 4:E, 5:F
    adj_matrix = [
        [0, 1, 4, 0, 0, 0],  # A
        [0, 0, 0, 2, 5, 0],  # B
        [0, 0, 0, 0, 0, 3],  # C
        [0, 0, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 1],  # E
        [0, 0, 0, 0, 0, 0],  # F
    ]
    path, cost = ucs(adj_matrix, 0, 5)
    print(f"UCS path (indices): {path}, cost: {cost}")
