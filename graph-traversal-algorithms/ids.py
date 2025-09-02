def ids(adj_matrix, start, max_depth):
    def dls(node, depth, visited, order):
        if depth == 0:
            order.append(node)
            return
        visited.add(node)
        order.append(node)
        for neighbor, connected in enumerate(adj_matrix[node]):
            if connected and neighbor not in visited:
                dls(neighbor, depth - 1, visited, order)

    for depth in range(max_depth + 1):
        visited = set()
        order = []
        dls(start, depth, visited, order)
        print(f"Depth {depth}: {order}")

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
    ids(adj_matrix, 0, 3)
