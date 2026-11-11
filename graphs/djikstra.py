

def djikstra(n, start, edges):
    distances = [float("inf")] * n
    distances[start] = 0
    
    minHeap = [(0,start)]
    graph = {i : [] for i in range(n)}
    
    for w, u, v in edges:
        graph[u].append((w, v))

    while minHeap:
        w, node = heapq.heappop(minHeap)
        if w > distances[node]:
            continue
        for dist, neighbor in graph[node]:
            if w + dist < distances[neighbor]:
                distances[neighbor] = w + dist
                heapq.heappush(minHeap, (dist + w, neighbor)
    return distances
