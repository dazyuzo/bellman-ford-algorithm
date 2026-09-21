def bellman_ford():
    # 1. Đọc dòng đầu tiên: V, E, source
    try:
        first_line = input().strip().split()
        if not first_line:
            return
        V = int(first_line[0])
        E = int(first_line[1])
        source = int(first_line[2])
    except EOFError:
        return

    edges = []
    # 2. Đọc E dòng tiếp theo: u, v, w
    for _ in range(E):
        u, v, w = map(int, input().strip().split())
        edges.append((u, v, w))

    # Khởi tạo khoảng cách và mảng lưu vết đường đi (parent)
    dist = [float('inf')] * V
    parent = [-1] * V
    dist[source] = 0

    # 3. Relax các cạnh (V - 1) lần
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # 4. Chạy thêm 1 lần (lần thứ V) để phát hiện chu trình âm
    cycle_start = -1
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            cycle_start = v
            parent[v] = u  # Cập nhật parent để truy vết đúng vào chu trình
            break

    # 5. Xử lý kết quả
    if cycle_start != -1:
        print("\nCảnh báo: Đồ thị chứa chu trình âm!")
        
        # Đi ngược V bước để đảm bảo chắc chắn ta đang đứng bên trong chu trình
        curr = cycle_start
        for _ in range(V):
            curr = parent[curr]
            
        # Truy vết để lấy danh sách đỉnh trong chu trình
        cycle = []
        start_node = curr
        while True:
            cycle.append(curr)
            curr = parent[curr]
            if curr == start_node:
                break
                
        # Thêm đỉnh đầu vào cuối mảng để khép kín chu trình
        cycle.append(start_node)
        # Đảo ngược mảng vì ta vừa đi lùi (từ con lên cha)
        cycle.reverse()
        
        print("Chu trình âm: " + " -> ".join(map(str, cycle)))
    else:
        print(f"\nKhoang cach ngan nhat tu dinh {source}:")
        for i in range(V):
            if dist[i] == float('inf'):
                print(f"Đỉnh {i}: Khoảng cách = Vô cực (Không có đường đi)")
            else:
                # Truy vết đường đi từ đỉnh i ngược về source
                path = []
                curr = i
                while curr != -1:
                    path.append(curr)
                    curr = parent[curr]
                path.reverse()
                
                path_str = " -> ".join(map(str, path))
                print(f"Đỉnh {i}: Khoảng cách = {dist[i]}, Đường đi: {path_str}")

if __name__ == "__main__":
    bellman_ford()
    pass