import pytest
from pprint import pprint


def test_part_one():
    wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    assert 159 == find_distance(wire1, wire2)

    wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    assert 135 == find_distance(wire1, wire2)


def find_distance(wire1, wire2):
    return 0


def create_grid(x, y):
    return [[0 for i in range(x)] for j in range(y)]


def draw_wire(grid):
    wire1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    wire2 = "U62,R66,U55,R34,D71,R55,D58,R83"

    curs_pos = (0, 0)

    for move in wire1.split(","):
        direction = move[0]
        magnitude = int(move[1:])
        print("Dir: {}, Mag: {}".format(direction, magnitude))

        for tick in range(magnitude):
            print(curs_pos)
            if direction == "U":
                curs_pos = (curs_pos[0] + 1, curs_pos[1])
            elif direction == "D":
                curs_pos = (curs_pos[0] - 1, curs_pos[1])
            elif direction == "L":
                curs_pos = (curs_pos[0], curs_pos[1] - 1)
            elif direction == "R":
                curs_pos = (curs_pos[0], curs_pos[1] + 1)
            else:
                raise Exception("Unknown direction: {}".format(direction))

            grid[curs_pos[0]][curs_pos[1]] += 1

            # TODO: Turn this into a CSV

    return grid


if __name__ == "__main__":
    grid = create_grid(500, 500)
    grid = draw_wire(grid)
    pprint(grid)
