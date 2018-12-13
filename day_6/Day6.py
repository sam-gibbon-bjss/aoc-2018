from parse import compile
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plot


def read_input():
    with open('input.txt') as f:
        return f.readlines()


coord_format = compile("{}, {}\n")
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


def part1():
    raw_coordinates = read_input()
    coordinates = list(map(parse_coord, raw_coordinates))
    # coordinates = [[0.5, 0.5], [0, 1], [1, 0], [1, 1], [1, 2], [1.5, 0.5], [2, 1], [1.5, 1.5]]

    vor = Voronoi(coordinates)
    voronoi_plot_2d(vor)

    finite_regions_index = list(filter(lambda region: len(region) != 0 and -1 not in region, vor.regions))

    # vor.regions gives points as indices into the vor.vertices list
    finite_regions = list(map(lambda region: [vor.vertices[i] for i in region], finite_regions_index))

    regions = {i: finite_regions[i] for i in range(len(finite_regions))}
    print("{} finite regions: {}".format(len(regions), regions))

    region_areas = {i: area_from_points(regions[i]) for i in range(len(finite_regions))}
    print("Region areas: {}".format(region_areas))

    plot.show()


if __name__ == '__main__':
    part1()
