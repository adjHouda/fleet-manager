import heapq


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    """Return the list of cells from start to goal (inclusive),
    or None if no path exists."""
    if not grid.is_free(start) or not grid.is_free(goal):
        return None
    if start == goal:
        return [start]

    counter = 0  # tie-breaker so the heap never compares cells
    open_heap = [(manhattan(start, goal), counter, start)]
    came_from = {}
    g_cost = {start: 0}

    while open_heap:
        _, _, current = heapq.heappop(open_heap)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for nxt in grid.neighbors(current):
            new_g = g_cost[current] + 1
            if new_g < g_cost.get(nxt, float("inf")):
                g_cost[nxt] = new_g
                came_from[nxt] = current
                counter += 1
                f = new_g + manhattan(nxt, goal)
                heapq.heappush(open_heap, (f, counter, nxt))
    return None
