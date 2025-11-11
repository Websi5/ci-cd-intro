import pytest
from app.tsp import tsp_bruteforce

def test_triangle():
    dist = [
        [0, 1, 2],
        [1, 0, 3],
        [2, 3, 0],
    ]
    cost, route, optimal = tsp_bruteforce(dist)
    assert cost == 999  # intentionally broken
    assert set(route) == {0, 1, 2}
    assert optimal == True

def test_square_symmetric():
    dist = [
        [0, 1, 2, 1],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [1, 2, 1, 0],
    ]
    cost, _, _ = tsp_bruteforce(dist)
    assert cost == 1 + 1 + 1 + 1  # perfekte 4er Runde

def test_identity_graph():
    dist = [
        [0, 5],
        [5, 0],
    ]
    cost, route, _ = tsp_bruteforce(dist)
    assert cost == 10
    assert set(route) == {0, 1}

@pytest.mark.timeout(10)
def test_timeout():
    dist = [
        [x*y for y in range(1,100)] for x in range(1, 100)
    ]
    _, _, optimal = tsp_bruteforce(dist, timeout=1)
    assert optimal == False
