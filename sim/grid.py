class Grid:
    """2D warehouse grid. 0 = free, 1 = obstacle."""

    def __init__(self, width, height, obstacles=()):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)  # set of (x, y)

    def in_bounds(self, cell):
        x, y = cell
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, cell):
        return self.in_bounds(cell) and cell not in self.obstacles

    def neighbors(self, cell):
        x, y = cell
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):  # 4-connected
            nxt = (x + dx, y + dy)
            if self.is_free(nxt):
                yield nxt

    def add_obstacle_rect(self, x0, y0, x1, y1):
        """Add a filled rectangle of obstacles (shelves)."""
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                self.obstacles.add((x, y))
