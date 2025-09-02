from collections import deque

def bfs(adj_matrix, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            for neighbor, connected in enumerate(adj_matrix[vertex]):
                if connected and neighbor not in visited:
                    queue.append(neighbor)
    return order

# Example usage:
if __name__ == "__main__":
    # 0:A, 1:B, 2:C, 3:D, 4:E, 5:F
    adj_matrix = [
        [0, 1, 1, 0, 0, 0],  # A
        [0, 0, 0, 1, 1, 0],  # B
        [0, 0, 0, 0, 0, 1],  # C
        [0, 0, 0, 0, 0, 0],  # D
        [0, 0, 0, 0, 0, 1],  # E
        [0, 0, 0, 0, 0, 0],  # F
    ]
    result = bfs(adj_matrix, 0)
    print("BFS traversal (indices):", result)
