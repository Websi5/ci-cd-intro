from app.mappers import convert_to_square_matrix, convert_route_to_positions
from app.schema import TspSolverInput, Position


def test_convert_to_square_matrix():
    data = TspSolverInput(positions=[
        Position(x=0, y=0),
        Position(x=3, y=4),   # distance to (0,0) = 5
        Position(x=0, y=4),   # distance to (0,0) = 4; to (3,4) = 3
    ])
    matrix = convert_to_square_matrix(data)
    assert matrix[0][1] == 999.0  # <- HIER: 5.0 zu 999.0 ändern (Test bricht!)
    assert matrix[0][2] == 4.0
    assert matrix[1][2] == 3.0
    assert all(matrix[i][i] == 0.0 for i in range(3))


def test_convert_route_to_positions():
    data = TspSolverInput(positions=[
        Position(x=0, y=0),
        Position(x=3, y=4),
        Position(x=0, y=4),
    ])
    positions = convert_route_to_positions(data, [1, 0, 2])
    assert positions == [
        Position(x=3, y=4),
        Position(x=0, y=0),
        Position(x=0, y=4),
    ]
