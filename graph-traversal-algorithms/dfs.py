def dfs(adj_matrix, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(start)
    order.append(start)
    for neighbor, connected in enumerate(adj_matrix[start]):
        if connected and neighbor not in visited:
            dfs(adj_matrix, neighbor, visited, order)
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
    result = dfs(adj_matrix, 0)
    print("DFS traversal (indices):", result)
