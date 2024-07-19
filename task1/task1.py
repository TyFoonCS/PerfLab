import sys


def circular_path(n, m):
    circular_array = list(range(1, n + 1))
    current_position = 0
    path = []

    while True:
        path.append(circular_array[current_position])
        current_position = (current_position + m - 1) % n
        if current_position == 0:
            break

    return ''.join(map(str, path))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task1.py <n> <m>")
    else:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        print(circular_path(n, m))
