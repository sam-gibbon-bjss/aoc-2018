from parse import compile
import numpy


def read_input():
    with open('input.txt') as f:
        return f.readlines()


coord_format = compile("{:d}, {:d}\n")
def parse_coord(coord):
    parsed = coord_format.parse(coord)
    return tuple(parsed)


# this assumes that the points describe a non-intersecting polygon.
# algorithm from http://geomalgorithms.com/a01-_area.html
def area_from_points(points):
    if len(points) < 3:
        return 0

    # automatically wrapping the list
    num_points = len(points)
    points.append(points[0])

    area = 0

    for i in range(1, num_points):
        area += points[i][0] * (points[i+1][1] - points[i-1][1])
        pass

    area += points[num_points][0] * (points[1][1] - points[num_points-1][1])

    return abs(area / 2.0)

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def part1():
    raw_coordinates = read_input()
    coordinates = list(map(parse_coord, raw_coordinates))
    # coordinates = [[1, 1], [1, 6], [8, 3], [3, 4], [5, 5], [8, 9]]

    x_coords, y_coords = zip(*coordinates)
    max_x = max(x_coords)
    max_y = max(y_coords)

    grid_size = max(max_x, max_y) + 1  # top left corner is 0,0
    empty_space = len(coordinates)  # numpy requires non-negative integers, this is guaranteed to not be used

    print("{} coordinates provided. Coordinate file requires {}x{} grid ({} spaces, {} total iterations)"
          .format(len(coordinates), grid_size, grid_size, (grid_size**2), (grid_size**2 * len(coordinates))))

    grid = numpy.empty((grid_size, grid_size), dtype=numpy.int16)
    grid.fill(empty_space)

    # place initial coordinates
    for i in range(len(coordinates)):
        coord = coordinates[i]
        grid[coord[1]][coord[0]] = i

    # for each grid space, compute distance to each coordinate and attach it to the nearest
    for x in range(grid_size):
        for y in range(grid_size):
            is_dupe = False
            smallest_coord = None
            smallest_distance = grid_size * 2  # max possible distance in the grid
            for coord in coordinates:
                distance = manhattan_distance([x, y], coord)
                if distance == smallest_distance:
                    is_dupe = True
                elif distance < smallest_distance:
                    is_dupe = False
                    smallest_distance = distance
                    smallest_coord = coord

            if not is_dupe:
                grid[y][x] = grid[smallest_coord[1]][smallest_coord[0]]

    print(grid)

    # if a region touches the edge, it is infinite and should not be considered
    print("Top row: {}".format(grid[0]))
    print("Bottom row: {}".format(grid[max_y]))
    print("Left column: {}".format(grid[..., 0]))
    print("Right column: {}".format(grid[..., max_x]))

    infinite_areas = {*grid[0], *grid[max_y], *grid[..., 0], *grid[..., max_x]}

    areas = numpy.bincount(grid.flatten())
    finite_areas = {i: areas[i] for i in range(empty_space) if i not in infinite_areas}
    print("Finite areas: {}".format(finite_areas))

    print("Largest finite area: {}".format(max(finite_areas.values())))


if __name__ == '__main__':
    part1()
