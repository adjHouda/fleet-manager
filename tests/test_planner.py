from sim.grid import Grid
from robots.planner import astar


def test_straight_line():
    g = Grid(5, 5)
    path = astar(g, (0, 0), (4, 0))
    assert path[0] == (0, 0) and path[-1] == (4, 0)
    assert len(path) == 5


def test_goes_around_wall():
    g = Grid(5, 5)
    g.add_obstacle_rect(2, 0, 2, 3)  # wall with a gap at y=4
    path = astar(g, (0, 0), (4, 0))
    assert path is not None
    assert all(g.is_free(c) for c in path)
    assert len(path) - 1 == 12  # must detour through the gap


def test_no_path():
    g = Grid(5, 5)
    g.add_obstacle_rect(2, 0, 2, 4)  # full wall
    assert astar(g, (0, 0), (4, 0)) is None


def test_start_equals_goal():
    g = Grid(3, 3)
    assert astar(g, (1, 1), (1, 1)) == [(1, 1)]


def test_goal_is_obstacle():
    g = Grid(3, 3, obstacles=[(2, 2)])
    assert astar(g, (0, 0), (2, 2)) is None
