import sys


def read_circle(file_path):
    with open(file_path, 'r') as f:
        x, y = map(float, f.readline().split())
        r = float(f.readline().strip())
    return (x, y, r)


def read_points(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def point_position(xc, yc, r, x, y):
    distance_squared = (x - xc) ** 2 + (y - yc) ** 2
    radius_squared = r ** 2
    if distance_squared == radius_squared:
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Usage: python task2.py <circle_file> <points_file>")
        return

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    xc, yc, r = read_circle(circle_file)
    points = read_points(points_file)

    results = [point_position(xc, yc, r, x, y) for x, y in points]

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
