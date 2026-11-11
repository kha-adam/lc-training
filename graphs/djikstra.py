

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
                heapq.heappush(minHeap, (w+dist, neighbor))
    return distances

def netw_delay(n, k, times):
    
    distances = [float("inf")] * n

    graph = {i: [] for i in range(n)}
    
    minHeap = [(0, k)]
    distances[k] = 0

    for u, v, w in times:
        graph[u].append((w, v))

    while minHeap:
        w, node = heapq.heappop(minHeap)
        if w > distance[node]:
            continue
        for dist, neighbor in graph[node]:
            if w + dist < distances[neighbor]:
                distances[neighbor] = w+dist
                heapq.heappush(minHeap, (w+dist, neighbor))
    res = max(distances)
    return res if res != float("inf") else -1
