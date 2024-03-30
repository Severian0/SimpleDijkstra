import heapq

def main():
    def dijkstra(graph, start):
        # Initialize distances to all nodes as infinity except the start node
        distances = {node: float('infinity') for node in graph}
        distances[start] = 0
        
        # Priority queue to store nodes and their tentative distances
        prio_queue = [(0, start)]
        
        while prio_queue:
            curr_dist, current_node = heapq.heappop(prio_queue)
            
            # Skip if we have already found a shorter path to this node
            if curr_dist > distances[current_node]:
                continue
            
            # Explore neighbors of the current node
            for neighbor, weight in graph[current_node].items():
                distance = curr_dist + weight
                # If we find a shorter path to a neighbor, update its distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(prio_queue, (distance, neighbor))
        
        return distances

    # Example graph
    graph = {
        'A': {'B': 12, 'C': 33},
        'B': {'A': 52, 'C': 28, 'D': 6},
        'C': {'A': 53, 'B': 52, 'D': 3, 'E': 4},
        'D': {'B': 11, 'C': 84, 'E': 2},
        'E': {'C': 25, 'D': 16}
    }

    start_node = 'B'
    distances = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node)
    for node, distance in distances.items():
        print("Node:", node, "Distance:", distance)


if __name__ == '__main__':
    main()