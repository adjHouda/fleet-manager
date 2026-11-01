import matplotlib.pyplot as plt
from sim.grid import Grid
from robots.planner import astar

g = Grid(20, 12)
g.add_obstacle_rect(5, 2, 5, 9)     # shelf 1
g.add_obstacle_rect(10, 0, 10, 7)   # shelf 2
g.add_obstacle_rect(14, 4, 14, 11)  # shelf 3

start, goal = (1, 5), (18, 6)
path = astar(g, start, goal)
print("Path length:", len(path) - 1 if path else "no path")

fig, ax = plt.subplots(figsize=(10, 6))
ox, oy = zip(*g.obstacles)
ax.scatter(ox, oy, marker="s", s=300, c="dimgray", label="shelves")
if path:
    px, py = zip(*path)
    ax.plot(px, py, "-o", c="tab:blue", label="A* path")
ax.scatter(*start, c="green", s=150, label="start", zorder=3)
ax.scatter(*goal, c="red", s=150, label="goal", zorder=3)
ax.set_xlim(-1, g.width)
ax.set_ylim(-1, g.height)
ax.set_aspect("equal")
ax.invert_yaxis()
ax.grid(True, alpha=0.3)
ax.legend()
plt.savefig("stage1.png", dpi=120)
print("saved stage1.png")
